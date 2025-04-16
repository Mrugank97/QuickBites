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

def check_database_schema():
    """Check the database schema and tables"""
    try:
        # Connect to project database
        conn = get_db_connection(False)
        cursor = conn.cursor(dictionary=True)
        
        # Get all tables
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        
        # Extract table names
        table_names = [list(table.values())[0] for table in tables]
        
        logging.info("Tables in the database:")
        for table in table_names:
            logging.info(f"  - {table}")
        
        # Check for tables that might need to be connected to admin
        potential_admin_related_tables = ['admin_permissions', 'admin_logs', 'admin_actions']
        for table in potential_admin_related_tables:
            if table in table_names:
                logging.info(f"Found potential admin-related table: {table}")
                
                # Check table structure
                cursor.execute(f"DESCRIBE {table}")
                columns = cursor.fetchall()
                logging.info(f"{table} table structure:")
                for column in columns:
                    logging.info(f"  {column['Field']} ({column['Type']}), Null: {column['Null']}, Key: {column['Key']}, Default: {column['Default']}")
                
                # Check for foreign key constraints
                cursor.execute(f"""
                    SELECT CONSTRAINT_NAME, COLUMN_NAME, REFERENCED_TABLE_NAME, REFERENCED_COLUMN_NAME
                    FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
                    WHERE TABLE_NAME = '{table}'
                    AND REFERENCED_TABLE_NAME IS NOT NULL
                    AND CONSTRAINT_SCHEMA = 'cs432g11'
                """)
                constraints = cursor.fetchall()
                
                if constraints:
                    logging.info(f"Foreign key constraints on {table} table:")
                    for constraint in constraints:
                        logging.info(f"  {constraint['CONSTRAINT_NAME']}: {constraint['COLUMN_NAME']} -> {constraint['REFERENCED_TABLE_NAME']}({constraint['REFERENCED_COLUMN_NAME']})")
                else:
                    logging.warning(f"No foreign key constraints found on {table} table.")
        
        # Check for admin role in CIMS Login table
        cims_conn = get_db_connection(True)
        cims_cursor = cims_conn.cursor(dictionary=True)
        
        cims_cursor.execute("SELECT COUNT(*) as count FROM Login WHERE Role = 'admin'")
        admin_count = cims_cursor.fetchone()['count']
        logging.info(f"Number of admin records in CIMS Login table: {admin_count}")
        
        if admin_count > 0:
            cims_cursor.execute("SELECT MemberID, Role FROM Login WHERE Role = 'admin' LIMIT 5")
            admins = cims_cursor.fetchall()
            logging.info("Sample admin records from CIMS Login table:")
            for admin in admins:
                logging.info(f"  MemberID: {admin['MemberID']}, Role: {admin['Role']}")
        
        # Close connections
        cursor.close()
        conn.close()
        cims_cursor.close()
        cims_conn.close()
        
    except Exception as e:
        logging.error(f"Error checking database schema: {str(e)}")

if __name__ == "__main__":
    check_database_schema()
