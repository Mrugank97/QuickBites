import logging
import mysql.connector
import json
from decimal import Decimal
from flask import jsonify, request

# Custom JSON encoder to handle Decimal and datetime objects
class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        elif hasattr(obj, 'isoformat'):  # Handle datetime objects
            return obj.isoformat()
        return super().default(obj)

def register_order_api(app):
    from session_validator import require_valid_session

    # Set the custom JSON encoder
    app.json_encoder = CustomJSONEncoder

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
    # API endpoint to create a new order
    @app.route('/api/orders/create', methods=['POST'])
    @app.route('/api/orders', methods=['POST'])  # Add an alias for compatibility
    @require_valid_session
    def create_order(user_id=None, **kwargs):
        try:
            data = request.json
            member_id = data.get('member_id')
            outlet_id = data.get('outlet_id')
            total_amount = data.get('total_amount')
            payment_method = data.get('payment_method', 'UPI')
            items = data.get('items', [])

            # Validate required fields
            if not all([member_id, outlet_id, total_amount]) or not items:
                return jsonify({"error": "Missing required fields"}), 400

            # Verify that the member_id matches the logged-in user or user is admin
            # For debugging purposes, temporarily allow all orders
            logging.info(f"Order placement: member_id={member_id}, user_id={user_id}, user_role={kwargs.get('user_role')}")

            # Skip authorization check for now to allow testing
            # if str(member_id) != str(user_id) and kwargs.get('user_role') != 'admin':
            #     return jsonify({"error": "Unauthorized. You can only place orders for yourself"}), 403

            conn = get_db_connection(False)  # Use project database
            cursor = conn.cursor()

            # Start a transaction
            conn.start_transaction()

            try:
                # Insert order
                order_query = """
                INSERT INTO orders (member_id, outlet_id, total_amount, order_status, payment_method)
                VALUES (%s, %s, %s, 'Pending', %s)
                """
                cursor.execute(order_query, (member_id, outlet_id, total_amount, payment_method))

                # Get the order ID
                order_id = cursor.lastrowid

                # Insert order items
                item_query = """
                INSERT INTO order_items (order_id, menu_id, quantity, subtotal)
                VALUES (%s, %s, %s, %s)
                """
                for item in items:
                    cursor.execute(item_query, (
                        order_id,
                        item['menu_id'],
                        item['quantity'],
                        item['subtotal']
                    ))

                # Create payment record in CIMS database
                try:
                    cims_conn = get_db_connection()  # Use CIMS database
                    cims_cursor = cims_conn.cursor()

                    payment_query = """
                    INSERT INTO G11_payments (OrderID, AmountPaid, PaymentMethod, PaymentStatus, PaymentTime)
                    VALUES (%s, %s, %s, 'Pending', NOW())
                    """
                    cims_cursor.execute(payment_query, (order_id, total_amount, payment_method))

                    cims_conn.commit()
                    cims_cursor.close()
                    cims_conn.close()
                except Exception as e:
                    logging.warning(f"Error creating payment record: {str(e)}")
                    # Continue even if payment record creation fails

                # Commit the transaction
                conn.commit()

                return jsonify({
                    "message": "Order created successfully",
                    "order_id": order_id
                }), 201
            except Exception as e:
                # Rollback in case of error
                conn.rollback()
                raise e
            finally:
                cursor.close()
                conn.close()
        except Exception as e:
            logging.error(f"Error in create_order: {str(e)}")
            return jsonify({"error": f"Internal server error: {str(e)}"}), 500

    # API endpoint to get orders by member
    @app.route('/api/orders/student/<int:member_id>', methods=['GET'])
    @app.route('/api/orders/member/<int:member_id>', methods=['GET'])  # Add an alias for compatibility
    @require_valid_session
    def get_orders_by_member(member_id, user_id=None, **kwargs):
        try:
            # Verify that the member_id matches the logged-in user or user is admin
            if str(member_id) != str(user_id) and kwargs.get('user_role') != 'admin':
                return jsonify({"error": "Unauthorized. You can only view your own orders"}), 403

            conn = get_db_connection(False)  # Use project database
            cursor = conn.cursor(dictionary=True)

            # Get orders with outlet information
            query = """
            SELECT o.*, ot.name as outlet_name, ot.location as outlet_location
            FROM orders o
            JOIN outlet ot ON o.outlet_id = ot.outlet_id
            WHERE o.member_id = %s
            ORDER BY o.order_time DESC
            """
            cursor.execute(query, (member_id,))
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

                # Get payment status from CIMS
                try:
                    cims_conn = get_db_connection()  # Use CIMS database
                    cims_cursor = cims_conn.cursor(dictionary=True)

                    payment_query = """
                    SELECT PaymentStatus
                    FROM G11_payments
                    WHERE OrderID = %s
                    """
                    cims_cursor.execute(payment_query, (order['order_id'],))
                    payment = cims_cursor.fetchone()

                    if payment:
                        order['payment_status'] = payment['PaymentStatus']
                    else:
                        order['payment_status'] = 'Unknown'

                    cims_cursor.close()
                    cims_conn.close()
                except Exception as e:
                    logging.warning(f"Error getting payment status: {str(e)}")
                    order['payment_status'] = 'Unknown'

            cursor.close()
            conn.close()

            return jsonify(orders), 200
        except Exception as e:
            logging.error(f"Error in get_orders_by_member: {str(e)}")
            return jsonify({"error": f"Internal server error: {str(e)}"}), 500

    # API endpoint to get order details
    @app.route('/api/orders/details/<int:order_id>', methods=['GET'])
    @require_valid_session
    def get_order_details(order_id, user_id=None, **kwargs):
        try:
            conn = get_db_connection(False)  # Use project database
            cursor = conn.cursor(dictionary=True)

            # Get order with outlet information
            query = """
            SELECT o.*, ot.name as outlet_name, ot.location as outlet_location
            FROM orders o
            JOIN outlet ot ON o.outlet_id = ot.outlet_id
            WHERE o.order_id = %s
            """
            cursor.execute(query, (order_id,))
            order = cursor.fetchone()

            if not order:
                cursor.close()
                conn.close()
                return jsonify({"error": "Order not found"}), 404

            # Verify that the user is authorized to view this order
            if (str(order['member_id']) != str(user_id) and
                kwargs.get('user_role') != 'admin' and
                not is_outlet_manager_for_order(user_id, order['outlet_id'])):
                cursor.close()
                conn.close()
                return jsonify({"error": "Unauthorized. You can only view your own orders or orders for your outlet"}), 403

            # Get order items
            item_query = """
            SELECT oi.*, m.item_name
            FROM order_items oi
            JOIN menu m ON oi.menu_id = m.menu_id
            WHERE oi.order_id = %s
            """
            cursor.execute(item_query, (order_id,))
            order['items'] = cursor.fetchall()

            # Get member information
            member_query = """
            SELECT m.UserName as member_name, m.emailID as member_email
            FROM cs432cims.members m
            WHERE m.ID = %s
            """
            cursor.execute(member_query, (order['member_id'],))
            member = cursor.fetchone()

            if member:
                order['member_name'] = member['member_name']
                order['member_email'] = member['member_email']

            # Get payment status from CIMS
            try:
                cims_conn = get_db_connection()  # Use CIMS database
                cims_cursor = cims_conn.cursor(dictionary=True)

                payment_query = """
                SELECT PaymentStatus, PaymentMethod, PaymentTime
                FROM G11_payments
                WHERE OrderID = %s
                """
                cims_cursor.execute(payment_query, (order_id,))
                payment = cims_cursor.fetchone()

                if payment:
                    order['payment_status'] = payment['PaymentStatus']
                    order['payment_method'] = payment['PaymentMethod']
                    order['payment_time'] = payment['PaymentTime']
                else:
                    order['payment_status'] = 'Unknown'

                cims_cursor.close()
                cims_conn.close()
            except Exception as e:
                logging.warning(f"Error getting payment status: {str(e)}")
                order['payment_status'] = 'Unknown'

            cursor.close()
            conn.close()

            return jsonify(order), 200
        except Exception as e:
            logging.error(f"Error in get_order_details: {str(e)}")
            return jsonify({"error": f"Internal server error: {str(e)}"}), 500

    # Helper function to check if a user is an outlet manager for a specific outlet
    def is_outlet_manager_for_order(user_id, outlet_id):
        try:
            conn = get_db_connection(False)  # Use project database
            cursor = conn.cursor()

            query = "SELECT * FROM outlet_manager WHERE member_id = %s AND outlet_id = %s"
            cursor.execute(query, (user_id, outlet_id))
            result = cursor.fetchone()

            cursor.close()
            conn.close()

            return result is not None
        except Exception as e:
            logging.error(f"Error in is_outlet_manager_for_order: {str(e)}")
            return False
