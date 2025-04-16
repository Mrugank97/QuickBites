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

def check_outlet_manager_structure():
    """Check the outlet_manager table structure and data"""
    try:
        # Connect to project database
        conn = get_db_connection(False)
        cursor = conn.cursor(dictionary=True)
        
        # Check table structure
        cursor.execute("DESCRIBE outlet_manager")
        columns = cursor.fetchall()
        
        logging.info("outlet_manager table structure:")
        for column in columns:
            logging.info(f"  {column['Field']} ({column['Type']}), Null: {column['Null']}, Key: {column['Key']}, Default: {column['Default']}")
        
        # Check data
        cursor.execute("""
            SELECT om.*, o.name as outlet_name
            FROM outlet_manager om
            JOIN outlet o ON om.outlet_id = o.outlet_id
        """)
        assignments = cursor.fetchall()
        
        logging.info(f"Found {len(assignments)} outlet manager assignments:")
        for assignment in assignments:
            logging.info(f"  Raw assignment data: {assignment}")
            
            # Check if the manager exists in the members table
            cims_conn = get_db_connection(True)
            cims_cursor = cims_conn.cursor(dictionary=True)
            
            cims_cursor.execute("SELECT ID, UserName, emailID FROM members WHERE ID = %s", (assignment['member_id'],))
            manager = cims_cursor.fetchone()
            
            if manager:
                logging.info(f"  Manager found in members table: {manager['UserName']} (ID: {manager['ID']}, Email: {manager['emailID']})")
            else:
                logging.warning(f"  Manager with ID {assignment['member_id']} not found in members table!")
            
            cims_cursor.close()
            cims_conn.close()
        
        # Close connection
        cursor.close()
        conn.close()
        
    except Exception as e:
        logging.error(f"Error checking outlet_manager structure: {str(e)}")

if __name__ == "__main__":
    check_outlet_manager_structure()
