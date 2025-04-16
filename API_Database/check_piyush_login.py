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

def check_piyush_login():
    """Check login information for user 'piyush'"""
    try:
        # Connect to CIMS database
        cims_conn = get_db_connection(True)
        cims_cursor = cims_conn.cursor(dictionary=True)
        
        # Get user information
        cims_cursor.execute("""
            SELECT m.ID, m.UserName, l.Role, l.MemberID
            FROM members m
            JOIN Login l ON m.ID = l.MemberID
            WHERE m.UserName = 'piyush'
        """)
        user = cims_cursor.fetchone()
        
        if not user:
            logging.error("User 'piyush' not found in the database")
            return
        
        logging.info(f"User found: ID={user['ID']}, Username={user['UserName']}, Role={user['Role']}, MemberID={user['MemberID']}")
        
        # Check if the MemberID in Login table is a string or an integer
        logging.info(f"MemberID type: {type(user['MemberID'])}")
        
        # Update the role if needed
        if user['Role'] != 'OutletManager':
            try:
                cims_cursor.execute("""
                    UPDATE Login
                    SET Role = 'OutletManager'
                    WHERE MemberID = %s
                """, (user['MemberID'],))
                cims_conn.commit()
                logging.info(f"Updated role for user ID {user['ID']} to 'OutletManager'")
            except Exception as e:
                logging.error(f"Error updating role: {str(e)}")
        
        # Close connections
        cims_cursor.close()
        cims_conn.close()
        
    except Exception as e:
        logging.error(f"Error checking login information: {str(e)}")

if __name__ == "__main__":
    check_piyush_login()
