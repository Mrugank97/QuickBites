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

def fix_outlet_manager_role():
    """Fix the role for outlet managers"""
    try:
        # Connect to project database
        proj_conn = get_db_connection(False)
        proj_cursor = proj_conn.cursor(dictionary=True)
        
        # Get all outlet managers
        proj_cursor.execute("""
            SELECT member_id, outlet_id
            FROM outlet_manager
        """)
        managers = proj_cursor.fetchall()
        
        logging.info(f"Found {len(managers)} outlet managers")
        
        # Connect to CIMS database
        cims_conn = get_db_connection(True)
        cims_cursor = cims_conn.cursor(dictionary=True)
        
        # Update roles for all outlet managers
        for manager in managers:
            member_id = manager['member_id']
            outlet_id = manager['outlet_id']
            
            # Get outlet name
            proj_cursor.execute("SELECT name FROM outlet WHERE outlet_id = %s", (outlet_id,))
            outlet = proj_cursor.fetchone()
            outlet_name = outlet['name'] if outlet else 'Unknown'
            
            # Get user information
            cims_cursor.execute("SELECT UserName FROM members WHERE ID = %s", (member_id,))
            member = cims_cursor.fetchone()
            username = member['UserName'] if member else 'Unknown'
            
            logging.info(f"Updating role for manager {username} (ID: {member_id}) of outlet {outlet_name} (ID: {outlet_id})")
            
            # Update role in Login table
            try:
                cims_cursor.execute("""
                    UPDATE Login
                    SET Role = 'manager'
                    WHERE MemberID = %s
                """, (str(member_id),))
                cims_conn.commit()
                logging.info(f"Updated role for user ID {member_id} to 'manager'")
            except Exception as e:
                logging.error(f"Error updating role for user ID {member_id}: {str(e)}")
        
        # Close connections
        proj_cursor.close()
        proj_conn.close()
        cims_cursor.close()
        cims_conn.close()
        
    except Exception as e:
        logging.error(f"Error fixing outlet manager roles: {str(e)}")

if __name__ == "__main__":
    fix_outlet_manager_role()
