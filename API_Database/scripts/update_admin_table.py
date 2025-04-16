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

def update_admin_table():
    """Update the admin table to match the SQL schema"""
    conn = None
    cursor = None
    
    try:
        # Connect to project database
        conn = get_db_connection(False)
        cursor = conn.cursor(dictionary=True)
        
        # Check if admin table exists
        cursor.execute("SHOW TABLES LIKE 'admin'")
        admin_exists = cursor.fetchone()
        
        if not admin_exists:
            logging.warning("admin table does not exist. Creating it...")
            
            # Create admin table
            cursor.execute("""
                CREATE TABLE admin (
                    member_id INT PRIMARY KEY,
                    access_level ENUM('SuperAdmin', 'Moderator') NOT NULL,
                    date_of_joining DATE NOT NULL,
                    FOREIGN KEY (member_id) REFERENCES Member(MemberID) ON DELETE CASCADE
                )
            """)
            conn.commit()
            logging.info("admin table created successfully.")
        else:
            logging.info("admin table exists. Checking structure...")
            
            # Check if the table has the correct structure
            cursor.execute("DESCRIBE admin")
            columns = cursor.fetchall()
            
            # Check if the primary key column is named correctly
            primary_key_column = next((col for col in columns if col['Key'] == 'PRI'), None)
            if primary_key_column and primary_key_column['Field'] != 'member_id':
                logging.warning(f"Primary key column is named {primary_key_column['Field']} instead of member_id.")
                
                # Rename the column if needed
                try:
                    cursor.execute(f"ALTER TABLE admin CHANGE {primary_key_column['Field']} member_id INT NOT NULL")
                    conn.commit()
                    logging.info(f"Renamed primary key column from {primary_key_column['Field']} to member_id.")
                except Exception as e:
                    logging.error(f"Error renaming primary key column: {str(e)}")
            
            # Check if the foreign key constraint exists
            cursor.execute("""
                SELECT CONSTRAINT_NAME
                FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
                WHERE TABLE_NAME = 'admin'
                AND REFERENCED_TABLE_NAME = 'Member'
                AND CONSTRAINT_SCHEMA = 'cs432g11'
            """)
            constraint = cursor.fetchone()
            
            if not constraint:
                logging.warning("Foreign key constraint to Member table does not exist. Adding it...")
                
                # Add foreign key constraint
                try:
                    cursor.execute("""
                        ALTER TABLE admin
                        ADD CONSTRAINT admin_member_fk
                        FOREIGN KEY (member_id) REFERENCES Member(MemberID) ON DELETE CASCADE
                    """)
                    conn.commit()
                    logging.info("Foreign key constraint added successfully.")
                except Exception as e:
                    logging.error(f"Error adding foreign key constraint: {str(e)}")
            else:
                logging.info(f"Foreign key constraint {constraint['CONSTRAINT_NAME']} already exists.")
        
        # Check if there are any admin records in the CIMS Login table that should be in the admin table
        cims_conn = get_db_connection(True)
        cims_cursor = cims_conn.cursor(dictionary=True)
        
        cims_cursor.execute("SELECT MemberID, Role FROM Login WHERE Role = 'admin' OR Role = 'Admin'")
        admin_records = cims_cursor.fetchall()
        
        if admin_records:
            logging.info(f"Found {len(admin_records)} admin records in CIMS Login table.")
            
            # Check which admin records are not in the admin table
            for admin in admin_records:
                member_id = admin['MemberID']
                
                cursor.execute("SELECT * FROM admin WHERE member_id = %s", (member_id,))
                existing_record = cursor.fetchone()
                
                if not existing_record:
                    logging.info(f"Adding admin record for member_id {member_id}...")
                    
                    # Add record to admin table
                    try:
                        cursor.execute("""
                            INSERT INTO admin (member_id, access_level, date_of_joining)
                            VALUES (%s, 'SuperAdmin', CURDATE())
                        """, (member_id,))
                        conn.commit()
                        logging.info(f"Added admin record for member_id {member_id}.")
                    except Exception as e:
                        logging.error(f"Error adding admin record for member_id {member_id}: {str(e)}")
        
        # Close connections
        cims_cursor.close()
        cims_conn.close()
        
        # Verify the admin table structure
        cursor.execute("DESCRIBE admin")
        columns = cursor.fetchall()
        logging.info("admin table structure:")
        for column in columns:
            logging.info(f"  {column['Field']} ({column['Type']}), Null: {column['Null']}, Key: {column['Key']}, Default: {column['Default']}")
        
        # Verify foreign key constraints
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
        
        # Close connection
        cursor.close()
        conn.close()
        
        logging.info("admin table update completed.")
        
    except Exception as e:
        logging.error(f"Error updating admin table: {str(e)}")
        if conn:
            conn.rollback()
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    update_admin_table()
