import mysql.connector
import logging
import jwt

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

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

def check_outlet_manager_role():
    """Check outlet manager role and assignment for user 'piyush'"""
    try:
        # Connect to CIMS database
        cims_conn = get_db_connection(True)
        cims_cursor = cims_conn.cursor(dictionary=True)
        
        # Get user information
        cims_cursor.execute("""
            SELECT m.ID, m.UserName, l.Role
            FROM members m
            JOIN Login l ON m.ID = l.MemberID
            WHERE m.UserName = 'piyush'
        """)
        user = cims_cursor.fetchone()
        
        if not user:
            logging.error("User 'piyush' not found in the database")
            return
        
        logging.info(f"User found: ID={user['ID']}, Username={user['UserName']}, Role={user['Role']}")
        
        # Check outlet manager assignment
        proj_conn = get_db_connection(False)
        proj_cursor = proj_conn.cursor(dictionary=True)
        
        proj_cursor.execute("""
            SELECT om.*, o.name as outlet_name, o.location
            FROM outlet_manager om
            JOIN outlet o ON om.outlet_id = o.outlet_id
            WHERE om.member_id = %s
        """, (user['ID'],))
        
        assignment = proj_cursor.fetchone()
        
        if assignment:
            logging.info(f"Outlet assignment found: Outlet ID={assignment['outlet_id']}, Name={assignment['outlet_name']}")
        else:
            logging.warning(f"No outlet assignment found for user ID {user['ID']}")
            
            # Check if there are any outlet managers in the database
            proj_cursor.execute("SELECT COUNT(*) as count FROM outlet_manager")
            count = proj_cursor.fetchone()['count']
            logging.info(f"Total outlet manager assignments in database: {count}")
            
            # Check all outlet managers
            proj_cursor.execute("""
                SELECT om.*, o.name as outlet_name, m.UserName
                FROM outlet_manager om
                JOIN outlet o ON om.outlet_id = o.outlet_id
                JOIN cs432cims.members m ON om.member_id = m.ID
            """)
            all_managers = proj_cursor.fetchall()
            
            for manager in all_managers:
                logging.info(f"Manager: {manager['UserName']} (ID: {manager['member_id']}) assigned to {manager['outlet_name']} (ID: {manager['outlet_id']})")
        
        # Create a test token for the user
        secret_key = "CS"  # Same as in the app
        token_payload = {
            "user": user['UserName'],
            "role": user['Role'],
            "session_id": user['ID']
        }
        
        token = jwt.encode(token_payload, secret_key, algorithm="HS256")
        logging.info(f"Test token for user: {token}")
        
        # Close connections
        cims_cursor.close()
        cims_conn.close()
        proj_cursor.close()
        proj_conn.close()
        
    except Exception as e:
        logging.error(f"Error checking outlet manager role: {str(e)}")

if __name__ == "__main__":
    check_outlet_manager_role()
