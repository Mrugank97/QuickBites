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

def check_outlet_manager_assignments():
    """Check all outlet manager assignments in the database"""
    try:
        # Connect to project database
        conn = get_db_connection(False)
        cursor = conn.cursor(dictionary=True)
        
        # Get all outlet manager assignments
        query = """
        SELECT om.*, o.name as outlet_name, m.UserName as manager_name, m.ID as member_id
        FROM outlet_manager om
        JOIN outlet o ON om.outlet_id = o.outlet_id
        LEFT JOIN cs432cims.members m ON om.member_id = m.ID
        """
        cursor.execute(query)
        assignments = cursor.fetchall()
        
        logging.info(f"Found {len(assignments)} outlet manager assignments:")
        for assignment in assignments:
            logging.info(f"Outlet: {assignment['outlet_name']} (ID: {assignment['outlet_id']}), " +
                         f"Manager: {assignment['manager_name'] or 'Unknown'} (ID: {assignment['member_id']})")
            
            # Check if the manager exists in the members table
            if assignment['manager_name'] is None:
                logging.warning(f"Manager with ID {assignment['member_id']} not found in members table!")
        
        # Get all outlets without managers
        query = """
        SELECT o.*
        FROM outlet o
        LEFT JOIN outlet_manager om ON o.outlet_id = om.outlet_id
        WHERE om.outlet_id IS NULL
        """
        cursor.execute(query)
        unassigned_outlets = cursor.fetchall()
        
        logging.info(f"Found {len(unassigned_outlets)} outlets without managers:")
        for outlet in unassigned_outlets:
            logging.info(f"Outlet: {outlet['name']} (ID: {outlet['outlet_id']})")
        
        # Close connection
        cursor.close()
        conn.close()
        
    except Exception as e:
        logging.error(f"Error checking outlet manager assignments: {str(e)}")

if __name__ == "__main__":
    check_outlet_manager_assignments()
