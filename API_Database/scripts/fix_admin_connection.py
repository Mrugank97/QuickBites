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

def fix_admin_connection():
    """Drop the Member table and modify the admin table to connect to cs432cims.members"""
    conn = None
    cursor = None
    
    try:
        # Connect to project database
        conn = get_db_connection(False)
        cursor = conn.cursor()
        
        # First, drop the foreign key constraint on the admin table
        logging.info("Dropping foreign key constraint on admin table...")
        cursor.execute("""
            ALTER TABLE admin
            DROP FOREIGN KEY admin_member_fk
        """)
        conn.commit()
        logging.info("Foreign key constraint dropped successfully.")
        
        # Drop the Member table
        logging.info("Dropping Member table...")
        cursor.execute("DROP TABLE IF EXISTS Member")
        conn.commit()
        logging.info("Member table dropped successfully.")
        
        # Modify the admin table to connect to cs432cims.members
        logging.info("Adding foreign key constraint to connect admin table to cs432cims.members...")
        cursor.execute("""
            ALTER TABLE admin
            ADD CONSTRAINT admin_members_fk
            FOREIGN KEY (member_id) REFERENCES cs432cims.members(ID)
            ON DELETE CASCADE
        """)
        conn.commit()
        logging.info("Foreign key constraint added successfully.")
        
        # Verify the changes
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
                logging.info(f"  {constraint[0]}: {constraint[1]} -> {constraint[2]}({constraint[3]})")
        else:
            logging.warning("No foreign key constraints found on admin table.")
        
        # Check if the constraint is working by joining the tables
        logging.info("Testing the constraint by joining admin and cs432cims.members...")
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
        logging.error(f"Error fixing admin connection: {str(e)}")
        if conn:
            conn.rollback()
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    fix_admin_connection()
