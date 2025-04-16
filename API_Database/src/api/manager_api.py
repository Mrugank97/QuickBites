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

def register_manager_api(app):
    """Register manager API endpoints"""

    # API endpoint to get the outlet assigned to a manager
    @app.route('/api/manager/assigned-outlet', methods=['GET'])
    @require_valid_session
    def get_manager_assigned_outlet(user_id=None, **kwargs):
        try:
            # Check if user is an outlet manager
            user_role = kwargs.get('user_role', '').lower()
            if 'manager' not in user_role and user_role != 'admin':
                return jsonify({"error": "Unauthorized. Only outlet managers can access this endpoint"}), 403

            conn = get_db_connection(False)  # Use project database
            cursor = conn.cursor(dictionary=True)

            # Get the outlet assigned to the manager
            query = """
            SELECT o.outlet_id, o.name, o.location
            FROM outlet o
            JOIN outlet_manager om ON o.outlet_id = om.outlet_id
            WHERE om.member_id = %s
            """
            cursor.execute(query, (user_id,))
            outlet = cursor.fetchone()

            cursor.close()
            conn.close()

            if not outlet:
                return jsonify({"error": "You are not assigned to any outlet"}), 404

            logging.info(f"Retrieved outlet {outlet['outlet_id']} for manager {user_id}")
            return jsonify(outlet), 200
        except Exception as e:
            logging.error(f"Error in get_manager_assigned_outlet: {str(e)}")
            return jsonify({"error": f"Internal server error: {str(e)}"}), 500

    # API endpoint to get outlet for a specific manager
    @app.route('/api/outlet/manager-assignment/<int:manager_id>', methods=['GET'])
    @require_valid_session
    def get_outlet_assignment_for_manager(manager_id, user_id=None, **kwargs):
        try:
            # Check if user is the manager or an admin
            user_role = kwargs.get('user_role', '').lower()
            if str(manager_id) != str(user_id) and user_role != 'admin':
                return jsonify({"error": "Unauthorized. You can only view your own outlet or you must be an admin"}), 403

            conn = get_db_connection(False)  # Use project database
            cursor = conn.cursor(dictionary=True)

            # Get the outlet assigned to the manager
            query = """
            SELECT o.outlet_id, o.name, o.location
            FROM outlet o
            JOIN outlet_manager om ON o.outlet_id = om.outlet_id
            WHERE om.member_id = %s
            """
            cursor.execute(query, (manager_id,))
            outlet = cursor.fetchone()

            cursor.close()
            conn.close()

            if not outlet:
                return jsonify({"error": "Manager is not assigned to any outlet"}), 404

            logging.info(f"Retrieved outlet {outlet['outlet_id']} for manager {manager_id}")
            return jsonify(outlet), 200
        except Exception as e:
            logging.error(f"Error in get_outlet_assignment_for_manager: {str(e)}")
            return jsonify({"error": f"Internal server error: {str(e)}"}), 500
