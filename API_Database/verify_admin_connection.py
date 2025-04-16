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

def verify_admin_connection():
    """Verify that the admin table is correctly connected to cs432cims.members"""
    try:
        # Connect to project database
        conn = get_db_connection(False)
        cursor = conn.cursor(dictionary=True)
        
        # Check if members_view exists
        cursor.execute("SHOW TABLES LIKE 'members_view'")
        view_exists = cursor.fetchone()
        
        if view_exists:
            logging.info("members_view exists in project database.")
            
            # Check members_view structure
            cursor.execute("DESCRIBE members_view")
            columns = cursor.fetchall()
            logging.info("members_view structure:")
            for column in columns:
                logging.info(f"  {column['Field']} ({column['Type']}), Null: {column['Null']}, Key: {column['Key']}, Default: {column['Default']}")
            
            # Get sample records from members_view
            cursor.execute("SELECT * FROM members_view LIMIT 5")
            view_records = cursor.fetchall()
            logging.info("Sample records from members_view:")
            for record in view_records:
                logging.info(f"  {record}")
        else:
            logging.warning("members_view does not exist in project database.")
        
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
            
            # Join admin table with members_view
            cursor.execute("""
                SELECT a.member_id, a.access_level, a.date_of_joining, m.Name, m.Email
                FROM admin a
                JOIN members_view m ON a.member_id = m.MemberID
                LIMIT 5
            """)
            joined_records = cursor.fetchall()
            logging.info("Joined records from admin and members_view:")
            for record in joined_records:
                logging.info(f"  {record}")
            
            # Join admin table with cs432cims.members directly
            cursor.execute("""
                SELECT a.member_id, a.access_level, a.date_of_joining, m.UserName, m.emailID
                FROM admin a
                JOIN cs432cims.members m ON a.member_id = m.ID
                LIMIT 5
            """)
            direct_joined_records = cursor.fetchall()
            logging.info("Joined records from admin and cs432cims.members directly:")
            for record in direct_joined_records:
                logging.info(f"  {record}")
        else:
            logging.warning("admin table does not exist in project database.")
        
        # Close connection
        cursor.close()
        conn.close()
        
    except Exception as e:
        logging.error(f"Error verifying admin connection: {str(e)}")

if __name__ == "__main__":
    verify_admin_connection()
