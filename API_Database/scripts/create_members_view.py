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

def create_members_view():
    """Create a view that mirrors the cs432cims.members table"""
    conn = None
    cursor = None
    
    try:
        # Connect to project database
        conn = get_db_connection(False)
        cursor = conn.cursor()
        
        # First, drop the foreign key constraint on the admin table if it exists
        try:
            logging.info("Dropping foreign key constraint on admin table if it exists...")
            cursor.execute("""
                ALTER TABLE admin
                DROP FOREIGN KEY admin_member_fk
            """)
            conn.commit()
            logging.info("Foreign key constraint dropped successfully.")
        except mysql.connector.Error as e:
            logging.info(f"No constraint to drop or error: {str(e)}")
        
        # Drop the Member table if it exists
        logging.info("Dropping Member table if it exists...")
        cursor.execute("DROP TABLE IF EXISTS Member")
        conn.commit()
        logging.info("Member table dropped successfully.")
        
        # Create a view that mirrors the cs432cims.members table
        logging.info("Creating members_view that mirrors cs432cims.members...")
        cursor.execute("""
            CREATE OR REPLACE VIEW members_view AS
            SELECT ID as MemberID, UserName as Name, 
                   IFNULL(emailID, CONCAT('user', ID, '@example.com')) as Email,
                   DoB
            FROM cs432cims.members
        """)
        conn.commit()
        logging.info("members_view created successfully.")
        
        # Modify the admin table to use the view
        logging.info("Updating admin table to use members_view...")
        
        # First, check if there are any admin records that don't have corresponding members
        cursor.execute("""
            SELECT a.member_id
            FROM admin a
            LEFT JOIN cs432cims.members m ON a.member_id = m.ID
            WHERE m.ID IS NULL
        """)
        invalid_records = cursor.fetchall()
        
        if invalid_records:
            logging.warning(f"Found {len(invalid_records)} admin records without corresponding members. Deleting them...")
            for record in invalid_records:
                member_id = record[0]
                cursor.execute("DELETE FROM admin WHERE member_id = %s", (member_id,))
                logging.info(f"Deleted admin record for member_id {member_id}")
            conn.commit()
        
        # Now verify that all admin records have corresponding members
        cursor.execute("""
            SELECT a.member_id, a.access_level, a.date_of_joining, m.UserName, m.emailID
            FROM admin a
            JOIN cs432cims.members m ON a.member_id = m.ID
            LIMIT 5
        """)
        joined_records = cursor.fetchall()
        
        if joined_records:
            logging.info("Join successful! Sample records:")
            for record in joined_records:
                logging.info(f"  {record}")
        else:
            logging.warning("No records found in the join. This might indicate a problem.")
        
        # Close connection
        cursor.close()
        conn.close()
        
        logging.info("Admin table connection fixed successfully.")
        
    except Exception as e:
        logging.error(f"Error creating members view: {str(e)}")
        if conn:
            conn.rollback()
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    create_members_view()
