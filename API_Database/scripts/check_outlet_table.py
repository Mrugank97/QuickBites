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

def check_outlet_table():
    """Check the Outlet table and its relationships"""
    try:
        # Connect to project database
        conn = get_db_connection(False)
        cursor = conn.cursor()
        
        # Check if Outlet table exists
        cursor.execute("SHOW TABLES LIKE 'Outlet'")
        outlet_exists = cursor.fetchone()
        
        if not outlet_exists:
            logging.info("Outlet table does not exist.")
            return
        
        logging.info("Outlet table exists.")
        
        # Check table structure
        cursor.execute("DESCRIBE Outlet")
        columns = cursor.fetchall()
        logging.info("Outlet table structure:")
        for column in columns:
            logging.info(f"  {column[0]} ({column[1]}), Null: {column[2]}, Key: {column[3]}, Default: {column[4]}")
        
        # Check for foreign key constraints
        cursor.execute("""
            SELECT CONSTRAINT_NAME, COLUMN_NAME, REFERENCED_TABLE_NAME, REFERENCED_COLUMN_NAME
            FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
            WHERE TABLE_NAME = 'Outlet'
            AND REFERENCED_TABLE_NAME IS NOT NULL
            AND CONSTRAINT_SCHEMA = 'cs432g11'
        """)
        constraints = cursor.fetchall()
        
        if constraints:
            logging.info("Foreign key constraints on Outlet table:")
            for constraint in constraints:
                logging.info(f"  {constraint[0]}: {constraint[1]} -> {constraint[2]}({constraint[3]})")
        else:
            logging.info("No foreign key constraints found on Outlet table.")
        
        # Check for tables referencing Outlet table
        cursor.execute("""
            SELECT CONSTRAINT_NAME, TABLE_NAME, COLUMN_NAME, REFERENCED_TABLE_NAME, REFERENCED_COLUMN_NAME
            FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
            WHERE REFERENCED_TABLE_NAME = 'Outlet'
            AND CONSTRAINT_SCHEMA = 'cs432g11'
        """)
        references = cursor.fetchall()
        
        if references:
            logging.info("Tables referencing Outlet table:")
            for ref in references:
                logging.info(f"  {ref[0]}: {ref[1]}.{ref[2]} -> {ref[3]}.{ref[4]}")
        else:
            logging.info("No tables referencing Outlet table.")
        
        # Check for data in the table
        cursor.execute("SELECT COUNT(*) FROM Outlet")
        count = cursor.fetchone()[0]
        logging.info(f"Outlet table has {count} records.")
        
        if count > 0:
            cursor.execute("SELECT * FROM Outlet LIMIT 5")
            rows = cursor.fetchall()
            logging.info("Sample data from Outlet table:")
            for row in rows:
                logging.info(f"  {row}")
        
        # Close connection
        cursor.close()
        conn.close()
        
    except Exception as e:
        logging.error(f"Error checking Outlet table: {str(e)}")

if __name__ == "__main__":
    check_outlet_table()
