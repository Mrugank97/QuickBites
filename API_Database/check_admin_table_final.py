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

def check_admin_table_final():
    """Check the admin table and its relationships"""
    try:
        # Connect to project database
        conn = get_db_connection(False)
        cursor = conn.cursor(dictionary=True)
        
        # Check admin table structure
        cursor.execute("DESCRIBE admin")
        columns = cursor.fetchall()
        logging.info("admin table structure:")
        for column in columns:
            logging.info(f"  {column['Field']} ({column['Type']}), Null: {column['Null']}, Key: {column['Key']}, Default: {column['Default']}")
        
        # Check foreign key constraints
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
            logging.warning("No foreign key constraints found on admin table.")
        
        # Count records in admin table
        cursor.execute("SELECT COUNT(*) as count FROM admin")
        admin_count = cursor.fetchone()['count']
        logging.info(f"Number of records in admin table: {admin_count}")
        
        # Get sample records from admin table
        cursor.execute("SELECT * FROM admin LIMIT 5")
        admin_records = cursor.fetchall()
        logging.info("Sample records from admin table:")
        for record in admin_records:
            logging.info(f"  {record}")
        
        # Join admin and Member tables to verify the relationship
        cursor.execute("""
            SELECT a.member_id, a.access_level, a.date_of_joining, m.Name, m.Email, m.Role
            FROM admin a
            JOIN Member m ON a.member_id = m.MemberID
            LIMIT 5
        """)
        joined_records = cursor.fetchall()
        logging.info("Joined records from admin and Member tables:")
        for record in joined_records:
            logging.info(f"  {record}")
        
        # Close connection
        cursor.close()
        conn.close()
        
    except Exception as e:
        logging.error(f"Error checking admin table: {str(e)}")

if __name__ == "__main__":
    check_admin_table_final()
