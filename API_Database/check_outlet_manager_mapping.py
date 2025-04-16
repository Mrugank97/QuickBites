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

def check_outlet_manager_mapping():
    """Check the mapping between outlet_manager and members tables"""
    try:
        # Connect to project database
        conn = get_db_connection(False)
        cursor = conn.cursor(dictionary=True)
        
        # Connect to CIMS database
        cims_conn = get_db_connection(True)
        cims_cursor = cims_conn.cursor(dictionary=True)
        
        # Get all outlet managers
        cursor.execute("""
            SELECT om.*, o.name as outlet_name
            FROM outlet_manager om
            JOIN outlet o ON om.outlet_id = o.outlet_id
        """)
        assignments = cursor.fetchall()
        
        logging.info(f"Found {len(assignments)} outlet manager assignments:")
        for assignment in assignments:
            logging.info(f"  Outlet: {assignment['outlet_name']} (ID: {assignment['outlet_id']}), Manager ID: {assignment['member_id']}")
            
            # Check if the manager exists in the members table
            cims_cursor.execute("SELECT ID, UserName, emailID FROM members WHERE ID = %s", (assignment['member_id'],))
            manager = cims_cursor.fetchone()
            
            if manager:
                logging.info(f"    Manager found in members table: {manager['UserName']} (ID: {manager['ID']}, Email: {manager['emailID']})")
            else:
                logging.warning(f"    Manager with ID {assignment['member_id']} not found in members table!")
                
                # Try to find managers with similar usernames
                cims_cursor.execute("SELECT ID, UserName, emailID FROM members WHERE UserName LIKE %s", (f"%piyush%",))
                similar_managers = cims_cursor.fetchall()
                
                if similar_managers:
                    logging.info(f"    Found {len(similar_managers)} managers with username containing 'piyush':")
                    for similar in similar_managers:
                        logging.info(f"      {similar['UserName']} (ID: {similar['ID']}, Email: {similar['emailID']})")
        
        # Check Login table for manager roles
        cims_cursor.execute("""
            SELECT l.MemberID, l.Role, m.UserName, m.emailID
            FROM Login l
            JOIN members m ON l.MemberID = m.ID
            WHERE l.Role LIKE '%manager%' OR l.Role = 'Manager' OR l.Role = 'OutletManager'
        """)
        managers = cims_cursor.fetchall()
        
        logging.info(f"Found {len(managers)} users with manager roles in Login table:")
        for manager in managers:
            logging.info(f"  {manager['UserName']} (ID: {manager['MemberID']}, Role: {manager['Role']}, Email: {manager['emailID']})")
            
            # Check if this manager is assigned to an outlet
            cursor.execute("SELECT * FROM outlet_manager WHERE member_id = %s", (manager['MemberID'],))
            assignment = cursor.fetchone()
            
            if assignment:
                logging.info(f"    Assigned to outlet ID: {assignment['outlet_id']}")
            else:
                logging.info(f"    Not assigned to any outlet")
        
        # Close connections
        cursor.close()
        conn.close()
        cims_cursor.close()
        cims_conn.close()
        
    except Exception as e:
        logging.error(f"Error checking outlet_manager mapping: {str(e)}")

if __name__ == "__main__":
    check_outlet_manager_mapping()
