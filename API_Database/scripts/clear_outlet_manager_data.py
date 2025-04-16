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

def clear_outlet_manager_data():
    """Remove all data from the outlet_manager table"""
    try:
        # Connect to project database
        conn = get_db_connection(False)
        cursor = conn.cursor()
        
        # Check current data in outlet_manager table
        cursor.execute("SELECT COUNT(*) FROM outlet_manager")
        count = cursor.fetchone()[0]
        logging.info(f"Found {count} records in outlet_manager table")
        
        if count > 0:
            # Delete all data from outlet_manager table
            cursor.execute("DELETE FROM outlet_manager")
            conn.commit()
            logging.info(f"Deleted {count} records from outlet_manager table")
            
            # Verify deletion
            cursor.execute("SELECT COUNT(*) FROM outlet_manager")
            new_count = cursor.fetchone()[0]
            logging.info(f"Now there are {new_count} records in outlet_manager table")
        else:
            logging.info("No records to delete in outlet_manager table")
        
        # Close connection
        cursor.close()
        conn.close()
        
        logging.info("Outlet manager data clearing completed")
        
    except Exception as e:
        logging.error(f"Error clearing outlet manager data: {str(e)}")

if __name__ == "__main__":
    clear_outlet_manager_data()
