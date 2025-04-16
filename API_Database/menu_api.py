from flask import jsonify, request
import logging
import mysql.connector
from session_validator import require_valid_session

def get_db_connection(cims=True):
    """Get a database connection"""
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

def register_menu_api(app):
    """Register menu API endpoints"""

    # API endpoint to get menu items for an outlet
    @app.route('/api/menu/outlet/<int:outlet_id>', methods=['GET'])
    @require_valid_session
    def get_outlet_menu(outlet_id, user_id=None, **kwargs):
        try:
            conn = get_db_connection(False)  # Use project database
            cursor = conn.cursor(dictionary=True)

            # Get menu items for the outlet
            query = """
            SELECT menu_id, outlet_id, item_name, price, available
            FROM menu
            WHERE outlet_id = %s
            ORDER BY item_name
            """
            cursor.execute(query, (outlet_id,))
            menu_items = cursor.fetchall()

            cursor.close()
            conn.close()

            # Convert Decimal objects to float for JSON serialization
            serializable_items = []
            for item in menu_items:
                serializable_item = {}
                for key, value in item.items():
                    if isinstance(value, (int, float, str, bool, type(None))):
                        serializable_item[key] = value
                    elif str(type(value)) == "<class 'decimal.Decimal'>":
                        serializable_item[key] = float(value)
                    else:
                        serializable_item[key] = str(value)
                serializable_items.append(serializable_item)

            logging.info(f"Retrieved {len(menu_items)} menu items for outlet {outlet_id}")
            return jsonify(serializable_items), 200
        except Exception as e:
            logging.error(f"Error in get_outlet_menu: {str(e)}")
            return jsonify({"error": f"Internal server error: {str(e)}"}), 500

    # API endpoint to get a specific menu item
    @app.route('/api/menu/<int:menu_id>', methods=['GET'])
    @require_valid_session
    def get_menu_item(menu_id, user_id=None, **kwargs):
        try:
            conn = get_db_connection(False)  # Use project database
            cursor = conn.cursor(dictionary=True)

            # Get menu item
            query = """
            SELECT menu_id, outlet_id, item_name, price, available
            FROM menu
            WHERE menu_id = %s
            """
            cursor.execute(query, (menu_id,))
            menu_item = cursor.fetchone()

            cursor.close()
            conn.close()

            if not menu_item:
                return jsonify({"error": "Menu item not found"}), 404

            # Convert Decimal objects to float for JSON serialization
            serializable_item = {}
            for key, value in menu_item.items():
                if isinstance(value, (int, float, str, bool, type(None))):
                    serializable_item[key] = value
                elif str(type(value)) == "<class 'decimal.Decimal'>":
                    serializable_item[key] = float(value)
                else:
                    serializable_item[key] = str(value)

            return jsonify(serializable_item), 200
        except Exception as e:
            logging.error(f"Error in get_menu_item: {str(e)}")
            return jsonify({"error": f"Internal server error: {str(e)}"}), 500

    # API endpoint to create a new menu item
    @app.route('/api/menu', methods=['POST'])
    @require_valid_session
    def create_menu_item(user_id=None, **kwargs):
        try:
            # Check if user is an outlet manager
            user_role = kwargs.get('user_role', '').lower()
            if 'manager' not in user_role and user_role != 'admin':
                return jsonify({"error": "Unauthorized. Only outlet managers can create menu items"}), 403

            data = request.json
            if not data:
                return jsonify({"error": "No data provided"}), 400

            # Validate required fields
            required_fields = ['outlet_id', 'item_name', 'price']
            for field in required_fields:
                if field not in data:
                    return jsonify({"error": f"Missing required field: {field}"}), 400

            # Get outlet ID for the manager
            conn = get_db_connection(False)  # Use project database
            cursor = conn.cursor(dictionary=True)

            # Check if the user is assigned to the outlet
            query = """
            SELECT outlet_id FROM outlet_manager
            WHERE member_id = %s AND outlet_id = %s
            """
            cursor.execute(query, (user_id, data['outlet_id']))
            outlet = cursor.fetchone()

            if not outlet:
                cursor.close()
                conn.close()
                return jsonify({"error": "You are not authorized to manage this outlet"}), 403

            # Create menu item
            query = """
            INSERT INTO menu (outlet_id, item_name, price, available)
            VALUES (%s, %s, %s, %s)
            """
            cursor.execute(query, (
                data['outlet_id'],
                data['item_name'],
                data['price'],
                data.get('available', True)
            ))

            menu_id = cursor.lastrowid
            conn.commit()

            cursor.close()
            conn.close()

            return jsonify({
                "message": "Menu item created successfully",
                "menu_id": menu_id
            }), 201
        except Exception as e:
            logging.error(f"Error in create_menu_item: {str(e)}")
            return jsonify({"error": f"Internal server error: {str(e)}"}), 500

    # API endpoint to update a menu item
    @app.route('/api/menu/<int:menu_id>', methods=['PUT'])
    @require_valid_session
    def update_menu_item(menu_id, user_id=None, **kwargs):
        try:
            # Check if user is an outlet manager
            user_role = kwargs.get('user_role', '').lower()
            if 'manager' not in user_role and user_role != 'admin':
                return jsonify({"error": "Unauthorized. Only outlet managers can update menu items"}), 403

            data = request.json
            if not data:
                return jsonify({"error": "No data provided"}), 400

            conn = get_db_connection(False)  # Use project database
            cursor = conn.cursor(dictionary=True)

            # Get the menu item to check if it exists and belongs to the manager's outlet
            query = """
            SELECT m.outlet_id
            FROM menu m
            JOIN outlet_manager om ON m.outlet_id = om.outlet_id
            WHERE m.menu_id = %s AND om.member_id = %s
            """
            cursor.execute(query, (menu_id, user_id))
            menu_item = cursor.fetchone()

            if not menu_item:
                cursor.close()
                conn.close()
                return jsonify({"error": "Menu item not found or you are not authorized to update it"}), 404

            # Update menu item
            query = """
            UPDATE menu
            SET item_name = %s, price = %s, available = %s
            WHERE menu_id = %s
            """
            cursor.execute(query, (
                data['item_name'],
                data['price'],
                data.get('available', True),
                menu_id
            ))

            conn.commit()

            cursor.close()
            conn.close()

            return jsonify({"message": "Menu item updated successfully"}), 200
        except Exception as e:
            logging.error(f"Error in update_menu_item: {str(e)}")
            return jsonify({"error": f"Internal server error: {str(e)}"}), 500

    # API endpoint to delete a menu item
    @app.route('/api/menu/<int:menu_id>', methods=['DELETE'])
    @require_valid_session
    def delete_menu_item(menu_id, user_id=None, **kwargs):
        try:
            # Check if user is an outlet manager
            user_role = kwargs.get('user_role', '').lower()
            if 'manager' not in user_role and user_role != 'admin':
                return jsonify({"error": "Unauthorized. Only outlet managers can delete menu items"}), 403

            conn = get_db_connection(False)  # Use project database
            cursor = conn.cursor(dictionary=True)

            # Get the menu item to check if it exists and belongs to the manager's outlet
            query = """
            SELECT m.outlet_id
            FROM menu m
            JOIN outlet_manager om ON m.outlet_id = om.outlet_id
            WHERE m.menu_id = %s AND om.member_id = %s
            """
            cursor.execute(query, (menu_id, user_id))
            menu_item = cursor.fetchone()

            if not menu_item:
                cursor.close()
                conn.close()
                return jsonify({"error": "Menu item not found or you are not authorized to delete it"}), 404

            # Delete menu item
            query = "DELETE FROM menu WHERE menu_id = %s"
            cursor.execute(query, (menu_id,))

            conn.commit()

            cursor.close()
            conn.close()

            return jsonify({"message": "Menu item deleted successfully"}), 200
        except Exception as e:
            logging.error(f"Error in delete_menu_item: {str(e)}")
            return jsonify({"error": f"Internal server error: {str(e)}"}), 500

    # API endpoint to get menu items for the current manager's outlet
    @app.route('/api/manager/menu', methods=['GET'])
    @require_valid_session
    def get_manager_menu(user_id=None, **kwargs):
        try:
            # Check if user is an outlet manager
            user_role = kwargs.get('user_role', '').lower()
            if 'manager' not in user_role and user_role != 'admin':
                return jsonify({"error": "Unauthorized. Only outlet managers can access this endpoint"}), 403

            conn = get_db_connection(False)  # Use project database
            cursor = conn.cursor(dictionary=True)

            # Get the outlet ID for the manager
            query = """
            SELECT outlet_id FROM outlet_manager
            WHERE member_id = %s
            """
            cursor.execute(query, (user_id,))
            outlet = cursor.fetchone()

            if not outlet:
                cursor.close()
                conn.close()
                return jsonify({"error": "You are not assigned to any outlet"}), 404

            outlet_id = outlet['outlet_id']

            # Get menu items for the outlet
            query = """
            SELECT menu_id, outlet_id, item_name, price, available
            FROM menu
            WHERE outlet_id = %s
            ORDER BY item_name
            """
            cursor.execute(query, (outlet_id,))
            menu_items = cursor.fetchall()

            cursor.close()
            conn.close()

            # Convert Decimal objects to float for JSON serialization
            serializable_items = []
            for item in menu_items:
                serializable_item = {}
                for key, value in item.items():
                    if isinstance(value, (int, float, str, bool, type(None))):
                        serializable_item[key] = value
                    elif str(type(value)) == "<class 'decimal.Decimal'>":
                        serializable_item[key] = float(value)
                    else:
                        serializable_item[key] = str(value)
                serializable_items.append(serializable_item)

            logging.info(f"Retrieved {len(menu_items)} menu items for manager {user_id} (outlet {outlet_id})")
            return jsonify(serializable_items), 200
        except Exception as e:
            logging.error(f"Error in get_manager_menu: {str(e)}")
            return jsonify({"error": f"Internal server error: {str(e)}"}), 500
