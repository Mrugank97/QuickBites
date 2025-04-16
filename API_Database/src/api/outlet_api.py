import logging
import mysql.connector
from flask import jsonify, request

def register_outlet_api(app):
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

    # API endpoint to get outlet for a manager
    @app.route('/api/outlet/manager/<int:manager_id>', methods=['GET'])
    @require_valid_session
    def get_outlet_for_manager(manager_id, user_id=None, **kwargs):
        try:
            # Check if user is the manager or an admin
            if str(manager_id) != str(user_id) and kwargs.get('user_role') != 'admin':
                return jsonify({"error": "Unauthorized. You can only view your own outlet"}), 403

            conn = get_db_connection(False)  # Use project database
            cursor = conn.cursor(dictionary=True)

            # Get manager's assigned outlet
            query = """
            SELECT o.*
            FROM outlet_manager om
            JOIN outlet o ON om.outlet_id = o.outlet_id
            WHERE om.member_id = %s
            """
            cursor.execute(query, (manager_id,))
            outlet = cursor.fetchone()

            cursor.close()
            conn.close()

            if not outlet:
                return jsonify({"error": "No outlet assigned to this manager"}), 404

            return jsonify(outlet), 200
        except Exception as e:
            logging.error(f"Error in get_manager_outlet: {str(e)}")
            return jsonify({"error": f"Internal server error: {str(e)}"}), 500

    # API endpoint to get all outlets
    @app.route('/api/outlets', methods=['GET'])
    @require_valid_session
    def get_outlets(user_id=None, **kwargs):
        try:
            include_assignments = request.args.get('include_assignments', 'false').lower() == 'true'

            conn = get_db_connection(False)  # Use project database
            cursor = conn.cursor(dictionary=True)

            # Get all outlets
            query = "SELECT * FROM outlet ORDER BY name"
            cursor.execute(query)
            outlets = cursor.fetchall()

            # If requested, include manager assignments
            if include_assignments:
                for outlet in outlets:
                    # Get manager assignment for this outlet
                    query = """
                    SELECT om.member_id, om.outlet_id, om.auto_assigned,
                           IFNULL(m.UserName, 'Unknown') as manager_name
                    FROM outlet_manager om
                    LEFT JOIN cs432cims.members m ON om.member_id = m.ID
                    WHERE om.outlet_id = %s
                    """
                    cursor.execute(query, (outlet['outlet_id'],))
                    manager = cursor.fetchone()

                    # Log the raw manager data for debugging
                    logging.info(f"Raw manager data for outlet {outlet['outlet_id']}: {manager}")

                    if manager:
                        # Always use the outlet_manager.member_id directly
                        outlet_manager_id = manager['member_id']

                        # Create a manager object with proper structure
                        outlet['assigned'] = True
                        outlet['manager'] = {
                            'member_id': outlet_manager_id,  # This is the outlet_manager ID
                            'manager_name': manager['manager_name'],
                            'auto_assigned': bool(manager['auto_assigned'])
                        }

                        # Also keep the old format for backward compatibility
                        outlet['manager_id'] = outlet_manager_id
                        outlet['manager_name'] = manager['manager_name']

                        logging.info(f"Outlet {outlet['outlet_id']} ({outlet['name']}) is assigned to manager {outlet_manager_id} ({manager['manager_name']})")
                    else:
                        outlet['assigned'] = False
                        outlet['manager'] = None
                        outlet['manager_id'] = None
                        outlet['manager_name'] = None

                        logging.info(f"Outlet {outlet['outlet_id']} ({outlet['name']}) has no manager assigned")

            cursor.close()
            conn.close()

            return jsonify(outlets), 200
        except Exception as e:
            logging.error(f"Error in get_outlets: {str(e)}")
            return jsonify({"error": f"Internal server error: {str(e)}"}), 500

    # API endpoint to get a specific outlet
    @app.route('/api/outlets/<int:outlet_id>', methods=['GET'])
    @require_valid_session
    def get_outlet(outlet_id, user_id=None, **kwargs):
        try:
            conn = get_db_connection(False)  # Use project database
            cursor = conn.cursor(dictionary=True)

            # Get outlet
            query = "SELECT * FROM outlet WHERE outlet_id = %s"
            cursor.execute(query, (outlet_id,))
            outlet = cursor.fetchone()

            if not outlet:
                cursor.close()
                conn.close()
                return jsonify({"error": "Outlet not found"}), 404

            # Get manager assignment for this outlet
            query = """
            SELECT om.member_id, om.outlet_id, om.auto_assigned,
                   IFNULL(m.UserName, 'Unknown') as manager_name
            FROM outlet_manager om
            LEFT JOIN cs432cims.members m ON om.member_id = m.ID
            WHERE om.outlet_id = %s
            """
            cursor.execute(query, (outlet_id,))
            manager = cursor.fetchone()

            # Log the raw manager data for debugging
            logging.info(f"Raw manager data for outlet {outlet_id}: {manager}")

            if manager:
                # Always use the outlet_manager.member_id directly
                outlet_manager_id = manager['member_id']

                # Create a manager object with proper structure
                outlet['assigned'] = True
                outlet['manager'] = {
                    'member_id': outlet_manager_id,  # This is the outlet_manager ID
                    'manager_name': manager['manager_name'],
                    'auto_assigned': bool(manager.get('auto_assigned', False))
                }

                # Also keep the old format for backward compatibility
                outlet['manager_id'] = outlet_manager_id
                outlet['manager_name'] = manager['manager_name']

                logging.info(f"Outlet {outlet_id} ({outlet['name']}) is assigned to manager {outlet_manager_id} ({manager['manager_name']})")
            else:
                outlet['assigned'] = False
                outlet['manager'] = None
                outlet['manager_id'] = None
                outlet['manager_name'] = None

            cursor.close()
            conn.close()

            return jsonify(outlet), 200
        except Exception as e:
            logging.error(f"Error in get_outlet: {str(e)}")
            return jsonify({"error": f"Internal server error: {str(e)}"}), 500
