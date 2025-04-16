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

def check_tables():
    """Check all tables in the database with exact case"""
    try:
        # Connect to project database
        conn = get_db_connection(False)
        cursor = conn.cursor()
        
        # Get all tables with exact case
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        
        # Extract table names
        table_names = [table[0] for table in tables]
        
        logging.info("Tables in the database (with exact case):")
        for table in table_names:
            logging.info(f"  - {table}")
        
        # Check for specific tables
        for table in ["OutletManager", "Student", "student", "outlet_manager"]:
            if table in table_names:
                logging.info(f"Table '{table}' exists.")
                
                # Check for foreign key constraints
                cursor.execute(f"""
                    SELECT CONSTRAINT_NAME, TABLE_NAME, COLUMN_NAME, REFERENCED_TABLE_NAME, REFERENCED_COLUMN_NAME
                    FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
                    WHERE TABLE_NAME = '{table}'
                    AND REFERENCED_TABLE_NAME IS NOT NULL
                    AND CONSTRAINT_SCHEMA = 'cs432g11'
                """)
                constraints = cursor.fetchall()
                
                if constraints:
                    logging.info(f"Foreign key constraints on '{table}' table:")
                    for constraint in constraints:
                        logging.info(f"  {constraint[0]}: {constraint[1]}.{constraint[2]} -> {constraint[3]}.{constraint[4]}")
                else:
                    logging.info(f"No foreign key constraints found on '{table}' table.")
                
                # Check for tables referencing this table
                cursor.execute(f"""
                    SELECT CONSTRAINT_NAME, TABLE_NAME, COLUMN_NAME, REFERENCED_TABLE_NAME, REFERENCED_COLUMN_NAME
                    FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
                    WHERE REFERENCED_TABLE_NAME = '{table}'
                    AND CONSTRAINT_SCHEMA = 'cs432g11'
                """)
                references = cursor.fetchall()
                
                if references:
                    logging.info(f"Tables referencing '{table}' table:")
                    for ref in references:
                        logging.info(f"  {ref[0]}: {ref[1]}.{ref[2]} -> {ref[3]}.{ref[4]}")
                else:
                    logging.info(f"No tables referencing '{table}' table.")
            else:
                logging.info(f"Table '{table}' does not exist.")
        
        # Close connection
        cursor.close()
        conn.close()
        
    except Exception as e:
        logging.error(f"Error checking tables: {str(e)}")

if __name__ == "__main__":
    check_tables()
