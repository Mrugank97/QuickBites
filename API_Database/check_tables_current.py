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
    """Check the current state of the tables"""
    try:
        # Connect to project database
        conn = get_db_connection(False)
        cursor = conn.cursor(dictionary=True)
        
        # Check if Member table exists
        cursor.execute("SHOW TABLES LIKE 'Member'")
        member_exists = cursor.fetchone()
        
        if member_exists:
            logging.info("Member table exists in project database.")
            
            # Check Member table structure
            cursor.execute("DESCRIBE Member")
            columns = cursor.fetchall()
            logging.info("Member table structure:")
            for column in columns:
                logging.info(f"  {column['Field']} ({column['Type']}), Null: {column['Null']}, Key: {column['Key']}, Default: {column['Default']}")
            
            # Check for foreign key constraints referencing Member table
            cursor.execute("""
                SELECT CONSTRAINT_NAME, TABLE_NAME, COLUMN_NAME, REFERENCED_TABLE_NAME, REFERENCED_COLUMN_NAME
                FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
                WHERE REFERENCED_TABLE_NAME = 'Member'
                AND CONSTRAINT_SCHEMA = 'cs432g11'
            """)
            references = cursor.fetchall()
            
            if references:
                logging.info("Tables referencing Member table:")
                for ref in references:
                    logging.info(f"  {ref['CONSTRAINT_NAME']}: {ref['TABLE_NAME']}.{ref['COLUMN_NAME']} -> {ref['REFERENCED_TABLE_NAME']}.{ref['REFERENCED_COLUMN_NAME']}")
            else:
                logging.info("No tables referencing Member table.")
        else:
            logging.info("Member table does not exist in project database.")
        
        # Check admin table
        cursor.execute("SHOW TABLES LIKE 'admin'")
        admin_exists = cursor.fetchone()
        
        if admin_exists:
            logging.info("admin table exists in project database.")
            
            # Check admin table structure
            cursor.execute("DESCRIBE admin")
            columns = cursor.fetchall()
            logging.info("admin table structure:")
            for column in columns:
                logging.info(f"  {column['Field']} ({column['Type']}), Null: {column['Null']}, Key: {column['Key']}, Default: {column['Default']}")
            
            # Check for foreign key constraints
            cursor.execute("""
                SELECT CONSTRAINT_NAME, COLUMN_NAME, REFERENCED_TABLE_NAME, REFERENCED_COLUMN_NAME
                FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
                WHERE TABLE_NAME = 'admin'
                AND REFERENCED_TABLE_NAME IS NOT NULL
                AND CONSTRAINT_SCHEMA = 'cs432g11'
            """)
            constraints = cursor.fetchall()
            
            if constraints:
                logging.info("Foreign key constraints on admin table:")
                for constraint in constraints:
                    logging.info(f"  {constraint['CONSTRAINT_NAME']}: {constraint['COLUMN_NAME']} -> {constraint['REFERENCED_TABLE_NAME']}({constraint['REFERENCED_COLUMN_NAME']})")
            else:
                logging.info("No foreign key constraints found on admin table.")
        else:
            logging.info("admin table does not exist in project database.")
        
        # Check members table in CIMS database
        cims_conn = get_db_connection(True)
        cims_cursor = cims_conn.cursor(dictionary=True)
        
        cims_cursor.execute("DESCRIBE members")
        columns = cims_cursor.fetchall()
        logging.info("members table structure in CIMS database:")
        for column in columns:
            logging.info(f"  {column['Field']} ({column['Type']}), Null: {column['Null']}, Key: {column['Key']}, Default: {column['Default']}")
        
        # Close connections
        cursor.close()
        conn.close()
        cims_cursor.close()
        cims_conn.close()
        
    except Exception as e:
        logging.error(f"Error checking tables: {str(e)}")

if __name__ == "__main__":
    check_tables()
