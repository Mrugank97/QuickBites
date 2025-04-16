"""
API endpoints for outlet manager assignment
"""
from flask import request, jsonify
import logging
from session_validator import require_valid_session

def get_db_connection(cims=True):
    """Get a database connection"""
    import mysql.connector

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

def register_routes(app):
    """Register outlet manager API routes with the Flask app"""

    # API endpoint to get all outlet-manager assignments
    @app.route('/api/outlet-manager/assignments', methods=['GET'])
    @require_valid_session
    def get_outlet_manager_assignments(user_id=None, **kwargs):
        try:
            # Only allow admins to view all assignments
            user_role = kwargs.get('user_role', '')
            if user_role != 'admin':
                return jsonify({"error": "Unauthorized. Only admins can view all assignments"}), 403

            conn = get_db_connection(False)  # Use project database
            cursor = conn.cursor(dictionary=True)

            # Get all assignments with outlet and manager details
            query = """
            SELECT om.outlet_id, o.name as outlet_name, om.member_id, m.UserName as manager_name,
                   IFNULL(om.auto_assigned, 0) as auto_assigned
            FROM outlet_manager om
            JOIN outlet o ON om.outlet_id = o.outlet_id
            JOIN cs432cims.members m ON om.member_id = m.ID
            ORDER BY o.name
            """
            cursor.execute(query)
            assignments = cursor.fetchall()

            cursor.close()
            conn.close()

            return jsonify(assignments), 200
        except Exception as e:
            logging.error(f"Error in get_outlet_manager_assignments: {str(e)}")
            return jsonify({"error": f"Internal server error: {str(e)}"}), 500

    # API endpoint to get available managers (not assigned to any outlet)
    @app.route('/api/managers/available', methods=['GET'])
    @require_valid_session
    def get_available_managers(user_id=None, **kwargs):
        try:
            # Only allow admins to view available managers
            user_role = kwargs.get('user_role', '')
            if user_role != 'admin':
                return jsonify({"error": "Unauthorized. Only admins can view available managers"}), 403

            conn = get_db_connection()  # Use CIMS database
            cursor = conn.cursor(dictionary=True)

            # Get all managers (users with Manager role)
            query = """
            SELECT m.ID as member_id, m.UserName as username, m.emailID as email
            FROM members m
            JOIN Login l ON m.ID = l.MemberID
            WHERE l.Role = 'Manager' OR l.Role LIKE '%manager%'
            ORDER BY m.UserName
            """
            cursor.execute(query)
            managers = cursor.fetchall()

            # Get assigned managers
            proj_conn = get_db_connection(False)  # Use project database
            proj_cursor = proj_conn.cursor(dictionary=True)

            query = """
            SELECT om.member_id, o.outlet_id, o.name
            FROM outlet_manager om
            JOIN outlet o ON om.outlet_id = o.outlet_id
            """
            proj_cursor.execute(query)
            assignments = proj_cursor.fetchall()

            # Create a map of member_id to assigned outlet
            assignment_map = {}
            for assignment in assignments:
                assignment_map[assignment['member_id']] = {
                    'outlet_id': assignment['outlet_id'],
                    'name': assignment['name']
                }

            # Add assignment info to managers
            for manager in managers:
                if manager['member_id'] in assignment_map:
                    manager['assigned'] = True
                    manager['assigned_outlet'] = assignment_map[manager['member_id']]
                else:
                    manager['assigned'] = False
                    manager['assigned_outlet'] = None

            proj_cursor.close()
            proj_conn.close()
            cursor.close()
            conn.close()

            return jsonify(managers), 200
        except Exception as e:
            logging.error(f"Error in get_available_managers: {str(e)}")
            return jsonify({"error": f"Internal server error: {str(e)}"}), 500

    # API endpoint to assign a manager to an outlet
    @app.route('/api/outlet-manager/assign', methods=['POST'])
    @require_valid_session
    def assign_outlet_manager(user_id=None, **kwargs):
        try:
            # Only allow admins to assign managers
            user_role = kwargs.get('user_role', '')
            if user_role != 'admin':
                return jsonify({"error": "Unauthorized. Only admins can assign managers"}), 403

            data = request.json
            outlet_id = data.get('outlet_id')
            manager_id = data.get('manager_id')

            # Validate required fields
            if not all([outlet_id, manager_id]):
                return jsonify({"error": "Missing required fields"}), 400

            conn = get_db_connection(False)  # Use project database
            cursor = conn.cursor(dictionary=True)

            # Check if outlet exists
            query = "SELECT * FROM outlet WHERE outlet_id = %s"
            cursor.execute(query, (outlet_id,))
            outlet = cursor.fetchone()

            if not outlet:
                cursor.close()
                conn.close()
                return jsonify({"error": "Outlet not found"}), 404

            # Check if manager exists
            cims_conn = get_db_connection()  # Use CIMS database
            cims_cursor = cims_conn.cursor(dictionary=True)

            query = "SELECT * FROM members WHERE ID = %s"
            cims_cursor.execute(query, (manager_id,))
            manager = cims_cursor.fetchone()

            # If manager_id is undefined or not found, try to find by username
            if not manager and 'username' in data:
                username = data.get('username')
                logging.info(f"Manager ID {manager_id} not found, trying to find by username: {username}")
                query = "SELECT * FROM members WHERE UserName = %s"
                cims_cursor.execute(query, (username,))
                manager = cims_cursor.fetchone()

                if manager:
                    # Update manager_id with the found ID
                    manager_id = manager['ID']
                    logging.info(f"Found manager by username: {username}, ID: {manager_id}")

            cims_cursor.close()
            cims_conn.close()

            if not manager:
                cursor.close()
                conn.close()
                return jsonify({"error": "Manager not found. Please check the manager ID or username."}), 404

            # Check if outlet already has a manager
            query = "SELECT * FROM outlet_manager WHERE outlet_id = %s"
            cursor.execute(query, (outlet_id,))
            existing_assignment = cursor.fetchone()

            if existing_assignment:
                cursor.close()
                conn.close()
                return jsonify({"error": "Outlet already has a manager assigned"}), 409

            # Check if manager is already assigned to an outlet
            query = "SELECT * FROM outlet_manager WHERE member_id = %s"
            cursor.execute(query, (manager_id,))
            manager_assignment = cursor.fetchone()

            if manager_assignment:
                cursor.close()
                conn.close()
                return jsonify({"error": "Manager is already assigned to an outlet"}), 409

            # Create the assignment (set auto_assigned to false for manual assignments)
            query = "INSERT INTO outlet_manager (outlet_id, member_id, auto_assigned) VALUES (%s, %s, %s)"
            cursor.execute(query, (outlet_id, manager_id, False))
            conn.commit()

            cursor.close()
            conn.close()

            return jsonify({"message": "Manager assigned to outlet successfully"}), 201
        except Exception as e:
            logging.error(f"Error in assign_outlet_manager: {str(e)}")
            return jsonify({"error": f"Internal server error: {str(e)}"}), 500

    # API endpoint to unassign a manager from an outlet
    @app.route('/api/outlet-manager/unassign', methods=['POST'])
    @require_valid_session
    def unassign_outlet_manager(user_id=None, **kwargs):
        try:
            # Only allow admins to unassign managers
            user_role = kwargs.get('user_role', '')
            if user_role != 'admin':
                return jsonify({"error": "Unauthorized. Only admins can unassign managers"}), 403

            data = request.json
            if not data:
                return jsonify({"error": "No data provided"}), 400

            # Get and validate outlet_id
            try:
                outlet_id = int(data.get('outlet_id'))
                if outlet_id <= 0:
                    return jsonify({"error": "Invalid outlet ID"}), 400
            except (TypeError, ValueError):
                return jsonify({"error": "outlet_id must be a valid integer"}), 400

            # Manager ID is optional - we'll find the manager by outlet ID
            manager_id = None
            username = None

            # If manager_id is provided, try to use it for logging purposes
            if 'manager_id' in data:
                try:
                    manager_id = int(data.get('manager_id'))
                    logging.info(f"Manager ID provided: {manager_id}")
                except (TypeError, ValueError):
                    logging.info(f"Invalid manager ID format: {data.get('manager_id')}")
                    manager_id = None

            # If username is provided, log it for reference
            if 'username' in data:
                username = data.get('username')
                logging.info(f"Username provided: {username}")

            logging.info(f"Unassigning manager from outlet {outlet_id}")

            conn = get_db_connection(False)  # Use project database
            cursor = conn.cursor()

            # Always try to find the assignment by outlet_id first
            check_query = "SELECT * FROM outlet_manager WHERE outlet_id = %s"
            cursor.execute(check_query, (outlet_id,))
            assignment = cursor.fetchone()

            if not assignment:
                cursor.close()
                conn.close()
                return jsonify({"error": "No assignment found for this outlet"}), 404

            # Get the manager_id from the assignment
            db_manager_id = assignment[1]  # member_id is the second column
            logging.info(f"Found assignment for outlet {outlet_id} with manager {db_manager_id}")

            # If we have a valid manager_id from the request, verify it matches
            if manager_id and manager_id > 0 and db_manager_id != manager_id:
                logging.warning(f"Requested to remove manager {manager_id} but outlet {outlet_id} is assigned to manager {db_manager_id}")

                # Check if the manager exists in the members table
                cims_conn = get_db_connection(True)  # Use CIMS database
                cims_cursor = cims_conn.cursor(dictionary=True)

                cims_cursor.execute("SELECT ID, UserName FROM members WHERE ID = %s", (db_manager_id,))
                db_manager = cims_cursor.fetchone()

                cims_cursor.execute("SELECT ID, UserName FROM members WHERE ID = %s", (manager_id,))
                req_manager = cims_cursor.fetchone()

                cims_cursor.close()
                cims_conn.close()

                logging.info(f"DB Manager: {db_manager}, Requested Manager: {req_manager}")

            # Delete the assignment using only the outlet_id
            query = "DELETE FROM outlet_manager WHERE outlet_id = %s"
            cursor.execute(query, (outlet_id,))

            # Log the deletion
            logging.info(f"Deleted assignment for outlet {outlet_id} (previously assigned to manager {db_manager_id})")

            conn.commit()
            cursor.close()
            conn.close()

            logging.info(f"Successfully unassigned manager {manager_id} from outlet {outlet_id}")
            return jsonify({"message": "Manager unassigned from outlet successfully"}), 200
        except Exception as e:
            logging.error(f"Error in unassign_outlet_manager: {str(e)}")
            return jsonify({"error": f"Internal server error: {str(e)}"}), 500
