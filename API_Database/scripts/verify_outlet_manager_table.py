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

def check_outlet_manager_table():
    """Check the outlet_manager table structure and data"""
    try:
        # Connect to project database
        conn = get_db_connection(False)
        cursor = conn.cursor(dictionary=True)
        
        # Check outlet_manager table structure
        cursor.execute("DESCRIBE outlet_manager")
        columns = cursor.fetchall()
        
        logging.info("outlet_manager table structure:")
        for column in columns:
            logging.info(f"  {column['Field']} ({column['Type']}), Null: {column['Null']}, Key: {column['Key']}, Default: {column['Default']}")
        
        # Check outlet_manager data
        cursor.execute("""
            SELECT om.*, o.name as outlet_name, m.UserName as manager_name
            FROM outlet_manager om
            JOIN outlet o ON om.outlet_id = o.outlet_id
            JOIN cs432cims.members m ON om.member_id = m.ID
            LIMIT 10
        """)
        assignments = cursor.fetchall()
        
        logging.info(f"Sample outlet_manager data (up to 10 rows):")
        for assignment in assignments:
            logging.info(f"  Manager: {assignment['manager_name']} (ID: {assignment['member_id']}), Outlet: {assignment['outlet_name']} (ID: {assignment['outlet_id']}), Auto-assigned: {assignment['auto_assigned']}")
        
        # Close connection
        cursor.close()
        conn.close()
        
    except Exception as e:
        logging.error(f"Error checking outlet_manager table: {str(e)}")

if __name__ == "__main__":
    check_outlet_manager_table()
