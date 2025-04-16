import mysql.connector
import logging

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

def check_piyush_assignment():
    """Check outlet manager assignment for user 'piyush'"""
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
        
        # Check if there's an entry in the outlet_manager table
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
            logging.warning(f"No outlet assignment found for user ID {user['ID']} in outlet_manager table")
            
            # Insert a new assignment for AS FastFood (outlet_id = 4)
            try:
                proj_cursor.execute("""
                    INSERT INTO outlet_manager (member_id, outlet_id)
                    VALUES (%s, 4)
                """, (user['ID'],))
                proj_conn.commit()
                logging.info(f"Created new outlet assignment for user ID {user['ID']} to outlet ID 4 (AS FastFood)")
            except Exception as e:
                logging.error(f"Error creating outlet assignment: {str(e)}")
        
        # Close connections
        cims_cursor.close()
        cims_conn.close()
        proj_cursor.close()
        proj_conn.close()
        
    except Exception as e:
        logging.error(f"Error checking outlet manager assignment: {str(e)}")

if __name__ == "__main__":
    check_piyush_assignment()
