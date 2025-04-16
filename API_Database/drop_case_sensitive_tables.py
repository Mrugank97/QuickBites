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

def remove_tables():
    """Remove specified tables with case sensitivity"""
    try:
        # Connect to project database
        conn = get_db_connection(False)
        cursor = conn.cursor()
        
        # List of tables to remove (case sensitive)
        tables_to_remove = [
            "Admin", "Feedback", "Member", "Menu", "OrderItems", 
            "Orders", "Outlet", "OutletManager", "Payments", "Student"
        ]
        
        # Get all tables in the database
        cursor.execute("SHOW TABLES")
        all_tables = [table[0] for table in cursor.fetchall()]
        
        logging.info(f"Found {len(all_tables)} tables in the database")
        
        # Check which tables from our list exist
        existing_tables = [table for table in tables_to_remove if table in all_tables]
        
        if not existing_tables:
            logging.warning("None of the specified tables exist in the database")
            cursor.close()
            conn.close()
            return
        
        logging.info(f"Found {len(existing_tables)} tables to remove: {', '.join(existing_tables)}")
        
        # Temporarily disable foreign key checks to avoid constraint issues
        cursor.execute("SET FOREIGN_KEY_CHECKS = 0")
        
        # Remove tables
        for table in existing_tables:
            try:
                cursor.execute(f"DROP TABLE `{table}`")
                logging.info(f"Successfully removed table: {table}")
            except mysql.connector.Error as e:
                logging.error(f"Error removing table {table}: {str(e)}")
        
        # Re-enable foreign key checks
        cursor.execute("SET FOREIGN_KEY_CHECKS = 1")
        
        # Verify removal
        cursor.execute("SHOW TABLES")
        remaining_tables = [table[0] for table in cursor.fetchall()]
        
        for table in existing_tables:
            if table in remaining_tables:
                logging.warning(f"Table {table} was not removed")
            else:
                logging.info(f"Verified removal of table {table}")
        
        # Close connection
        cursor.close()
        conn.close()
        
        logging.info("Table removal completed")
        
    except Exception as e:
        logging.error(f"Error removing tables: {str(e)}")

if __name__ == "__main__":
    remove_tables()
