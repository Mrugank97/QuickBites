import logging
import mysql.connector
from flask import jsonify, request

def register_order_management_api(app):
    from session_validator import require_valid_session

    # Define get_db_connection function
    def get_db_connection(cims=True):
        db_config_proj = {
            "host": "10.0.116.125",
            "user": "cs432g11",
            "password": "pXqJ5NYz",
            "database": "cs432g11"  # Use cs432g11 for project-specific tables
        }

        db_config_cism = {
            "host": "10.0.116.125",
            "user": "cs432g11",
            "password": "pXqJ5NYz",
            "database": "cs432cims"
        }

        try:
            if cims:
                return mysql.connector.connect(**db_config_cism)
            else:
                return mysql.connector.connect(**db_config_proj)
        except mysql.connector.Error as e:
            logging.error(f"Database connection failed: {str(e)}")
            raise
    # API endpoint to get orders by outlet
    @app.route('/api/orders/outlet/<int:outlet_id>', methods=['GET'])
    @require_valid_session
    def get_orders_by_outlet(outlet_id, user_id=None, **kwargs):
        try:
            # Check if user is an outlet manager or admin
            user_role = kwargs.get('user_role', '').lower()
            if not (user_role == 'admin' or 'manager' in user_role):
                return jsonify({"error": "Unauthorized. Only outlet managers and admins can view outlet orders"}), 403

            # If user is an outlet manager, verify they manage this outlet
            if 'manager' in user_role and user_role != 'admin':
                conn = get_db_connection(False)  # Use project database
                cursor = conn.cursor(dictionary=True)

                query = "SELECT outlet_id FROM outlet_manager WHERE member_id = %s"
                cursor.execute(query, (user_id,))
                result = cursor.fetchone()

                cursor.close()
                conn.close()

                if not result:
                    logging.warning(f"User {user_id} with role {user_role} is not assigned to any outlet")
                    return jsonify({"error": "You are not assigned to any outlet"}), 403

                if result['outlet_id'] != outlet_id:
                    logging.warning(f"User {user_id} with role {user_role} is trying to access orders for outlet {outlet_id} but is assigned to outlet {result['outlet_id']}")
                    return jsonify({"error": "Unauthorized. You can only view orders for your assigned outlet"}), 403

                logging.info(f"User {user_id} with role {user_role} is accessing orders for their assigned outlet {outlet_id}")

            conn = get_db_connection(False)  # Use project database
            cursor = conn.cursor(dictionary=True)

            # Get orders with member information
            query = """
            SELECT o.*, m.UserName as member_name
            FROM orders o
            LEFT JOIN cs432cims.members m ON o.member_id = m.ID
            WHERE o.outlet_id = %s
            ORDER BY o.order_time DESC
            """
            cursor.execute(query, (outlet_id,))
            orders = cursor.fetchall()

            # Get order items for each order
            for order in orders:
                item_query = """
                SELECT oi.*, m.item_name
                FROM order_items oi
                JOIN menu m ON oi.menu_id = m.menu_id
                WHERE oi.order_id = %s
                """
                cursor.execute(item_query, (order['order_id'],))
                order['items'] = cursor.fetchall()

                # Add default payment status for UI compatibility
                order['payment_status'] = 'Pending'
                if order['order_status'] == 'Completed':
                    order['payment_status'] = 'Completed'
                elif order['order_status'] == 'Cancelled':
                    order['payment_status'] = 'Failed'

            cursor.close()
            conn.close()

            return jsonify(orders), 200
        except Exception as e:
            logging.error(f"Error in get_orders_by_outlet: {str(e)}")
            return jsonify({"error": f"Internal server error: {str(e)}"}), 500

    # API endpoint to update order status
    @app.route('/api/orders/<int:order_id>/status', methods=['PUT'])
    @require_valid_session
    def update_order_status(order_id, user_id=None, **kwargs):
        try:
            # Check if user is an outlet manager or admin
            user_role = kwargs.get('user_role', '').lower()
            if not (user_role == 'admin' or 'manager' in user_role):
                return jsonify({"error": "Unauthorized. Only outlet managers and admins can update order status"}), 403

            data = request.json
            new_status = data.get('status')

            # Validate status
            if new_status not in ['Pending', 'Completed', 'Cancelled']:
                return jsonify({"error": "Invalid status. Must be 'Pending', 'Completed', or 'Cancelled'"}), 400

            # Get the order to check outlet_id
            conn = get_db_connection(False)  # Use project database
            cursor = conn.cursor(dictionary=True)

            query = "SELECT * FROM orders WHERE order_id = %s"
            cursor.execute(query, (order_id,))
            order = cursor.fetchone()

            if not order:
                cursor.close()
                conn.close()
                return jsonify({"error": "Order not found"}), 404

            # If user is an outlet manager, verify they manage this outlet
            if 'manager' in user_role and user_role != 'admin':
                query = "SELECT outlet_id FROM outlet_manager WHERE member_id = %s"
                cursor.execute(query, (user_id,))
                result = cursor.fetchone()

                if not result or result['outlet_id'] != order['outlet_id']:
                    cursor.close()
                    conn.close()
                    return jsonify({"error": "Unauthorized. You can only update orders for your assigned outlet"}), 403

            # Update order status
            update_query = "UPDATE orders SET order_status = %s WHERE order_id = %s"
            cursor.execute(update_query, (new_status, order_id))

            # If order is completed or cancelled, update payment status in CIMS
            if new_status in ['Completed', 'Cancelled']:
                payment_status = 'Completed' if new_status == 'Completed' else 'Failed'

                try:
                    payment_query = "UPDATE cs432cims.G11_payments SET PaymentStatus = %s WHERE OrderID = %s"
                    cursor.execute(payment_query, (payment_status, order_id))
                except Exception as e:
                    logging.warning(f"Error updating payment status: {str(e)}")
                    # Continue even if payment update fails

            conn.commit()
            cursor.close()
            conn.close()

            return jsonify({"message": f"Order status updated to {new_status}"}), 200
        except Exception as e:
            logging.error(f"Error in update_order_status: {str(e)}")
            return jsonify({"error": f"Internal server error: {str(e)}"}), 500

    # API endpoint to get manager's assigned outlet
    @app.route('/api/manager/outlet', methods=['GET'])
    @require_valid_session
    def get_manager_outlet(user_id=None, **kwargs):
        try:
            # Check if user is an outlet manager
            user_role = kwargs.get('user_role', '').lower()
            if not ('manager' in user_role):
                return jsonify({"error": "Unauthorized. Only outlet managers can access this endpoint"}), 403

            conn = get_db_connection(False)  # Use project database
            cursor = conn.cursor(dictionary=True)

            # Get manager's assigned outlet
            query = """
            SELECT o.*
            FROM outlet_manager om
            JOIN outlet o ON om.outlet_id = o.outlet_id
            WHERE om.member_id = %s
            """
            cursor.execute(query, (user_id,))
            outlet = cursor.fetchone()

            cursor.close()
            conn.close()

            if not outlet:
                return jsonify({"error": "No outlet assigned to this manager"}), 404

            return jsonify(outlet), 200
        except Exception as e:
            logging.error(f"Error in get_manager_outlet: {str(e)}")
            return jsonify({"error": f"Internal server error: {str(e)}"}), 500

    # API endpoint to get order statistics for outlet
    @app.route('/api/orders/outlet/<int:outlet_id>/stats', methods=['GET'])
    @require_valid_session
    def get_outlet_order_stats(outlet_id, user_id=None, **kwargs):
        try:
            # Check if user is an outlet manager or admin
            user_role = kwargs.get('user_role', '').lower()
            if not (user_role == 'admin' or 'manager' in user_role):
                return jsonify({"error": "Unauthorized. Only outlet managers and admins can view outlet statistics"}), 403

            # If user is an outlet manager, verify they manage this outlet
            if 'manager' in user_role and user_role != 'admin':
                conn = get_db_connection(False)  # Use project database
                cursor = conn.cursor(dictionary=True)

                query = "SELECT outlet_id FROM outlet_manager WHERE member_id = %s"
                cursor.execute(query, (user_id,))
                result = cursor.fetchone()

                cursor.close()
                conn.close()

                if not result or result['outlet_id'] != outlet_id:
                    return jsonify({"error": "Unauthorized. You can only view statistics for your assigned outlet"}), 403

            conn = get_db_connection(False)  # Use project database
            cursor = conn.cursor(dictionary=True)

            # Get total orders
            query = "SELECT COUNT(*) as total_orders FROM orders WHERE outlet_id = %s"
            cursor.execute(query, (outlet_id,))
            total_orders = cursor.fetchone()['total_orders']

            # Get orders by status
            query = """
            SELECT order_status, COUNT(*) as count
            FROM orders
            WHERE outlet_id = %s
            GROUP BY order_status
            """
            cursor.execute(query, (outlet_id,))
            status_counts = cursor.fetchall()

            # Get total revenue
            query = """
            SELECT SUM(total_amount) as total_revenue
            FROM orders
            WHERE outlet_id = %s AND order_status = 'Completed'
            """
            cursor.execute(query, (outlet_id,))
            result = cursor.fetchone()
            total_revenue = float(result['total_revenue']) if result['total_revenue'] else 0

            # Get popular items
            query = """
            SELECT m.item_name, SUM(oi.quantity) as total_quantity
            FROM order_items oi
            JOIN orders o ON oi.order_id = o.order_id
            JOIN menu m ON oi.menu_id = m.menu_id
            WHERE o.outlet_id = %s AND o.order_status = 'Completed'
            GROUP BY m.item_name
            ORDER BY total_quantity DESC
            LIMIT 5
            """
            cursor.execute(query, (outlet_id,))
            popular_items = cursor.fetchall()

            cursor.close()
            conn.close()

            # Format status counts into a dictionary
            status_dict = {}
            for status in status_counts:
                status_dict[status['order_status']] = status['count']

            stats = {
                'total_orders': total_orders,
                'status_counts': status_dict,
                'total_revenue': total_revenue,
                'popular_items': popular_items
            }

            return jsonify(stats), 200
        except Exception as e:
            logging.error(f"Error in get_outlet_order_stats: {str(e)}")
            return jsonify({"error": f"Internal server error: {str(e)}"}), 500
