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

def populate_member_table():
    """Populate the Member table with records from CIMS members table"""
    conn = None
    cursor = None
    
    try:
        # Connect to project database
        conn = get_db_connection(False)
        cursor = conn.cursor(dictionary=True)
        
        # Check if Member table exists
        cursor.execute("SHOW TABLES LIKE 'Member'")
        member_exists = cursor.fetchone()
        
        if not member_exists:
            logging.warning("Member table does not exist. Creating it...")
            
            # Create Member table
            cursor.execute("""
                CREATE TABLE Member (
                    MemberID INT PRIMARY KEY,
                    Name VARCHAR(100) NOT NULL,
                    Image VARCHAR(255) NOT NULL,
                    Age INT NOT NULL,
                    Email VARCHAR(100) NOT NULL,
                    ContactNumber VARCHAR(15) NOT NULL,
                    Role ENUM('Student', 'OutletManager', 'Admin') NOT NULL,
                    CreatedAt TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
                    UNIQUE KEY Email_UNIQUE (Email),
                    UNIQUE KEY ContactNumber_UNIQUE (ContactNumber)
                )
            """)
            conn.commit()
            logging.info("Member table created successfully.")
        
        # Get admin records from CIMS Login table
        cims_conn = get_db_connection(True)
        cims_cursor = cims_conn.cursor(dictionary=True)
        
        cims_cursor.execute("""
            SELECT l.MemberID, m.UserName, m.emailID, m.DoB, l.Role
            FROM Login l
            JOIN members m ON l.MemberID = m.ID
            WHERE l.Role = 'admin' OR l.Role = 'Admin'
        """)
        admin_records = cims_cursor.fetchall()
        
        if admin_records:
            logging.info(f"Found {len(admin_records)} admin records in CIMS Login table.")
            
            # Add each admin record to Member table
            for admin in admin_records:
                member_id = admin['MemberID']
                name = admin['UserName']
                email = admin['emailID'] or f"admin{member_id}@example.com"  # Default email if none exists
                
                # Check if member already exists in Member table
                cursor.execute("SELECT * FROM Member WHERE MemberID = %s", (member_id,))
                existing_member = cursor.fetchone()
                
                if not existing_member:
                    logging.info(f"Adding member record for member_id {member_id}...")
                    
                    # Add record to Member table
                    try:
                        cursor.execute("""
                            INSERT INTO Member (MemberID, Name, Image, Age, Email, ContactNumber, Role)
                            VALUES (%s, %s, %s, %s, %s, %s, %s)
                        """, (
                            member_id,
                            name,
                            'default-avatar.png',  # Default image
                            30,  # Default age
                            email,
                            f"9999{member_id}",  # Default contact number
                            'Admin'  # Role
                        ))
                        conn.commit()
                        logging.info(f"Added member record for member_id {member_id}.")
                    except Exception as e:
                        logging.error(f"Error adding member record for member_id {member_id}: {str(e)}")
                        conn.rollback()
                else:
                    logging.info(f"Member record for member_id {member_id} already exists.")
        
        # Close CIMS connection
        cims_cursor.close()
        cims_conn.close()
        
        # Now add admin records to admin table
        for admin in admin_records:
            member_id = admin['MemberID']
            
            # Check if admin record already exists
            cursor.execute("SELECT * FROM admin WHERE member_id = %s", (member_id,))
            existing_admin = cursor.fetchone()
            
            if not existing_admin:
                logging.info(f"Adding admin record for member_id {member_id}...")
                
                # Add record to admin table
                try:
                    cursor.execute("""
                        INSERT INTO admin (member_id, access_level, date_of_joining)
                        VALUES (%s, %s, CURDATE())
                    """, (member_id, 'SuperAdmin'))
                    conn.commit()
                    logging.info(f"Added admin record for member_id {member_id}.")
                except Exception as e:
                    logging.error(f"Error adding admin record for member_id {member_id}: {str(e)}")
                    conn.rollback()
            else:
                logging.info(f"Admin record for member_id {member_id} already exists.")
        
        # Verify the admin table
        cursor.execute("SELECT COUNT(*) as count FROM admin")
        admin_count = cursor.fetchone()['count']
        logging.info(f"Number of records in admin table: {admin_count}")
        
        # Close connection
        cursor.close()
        conn.close()
        
        logging.info("Member and admin tables populated successfully.")
        
    except Exception as e:
        logging.error(f"Error populating Member table: {str(e)}")
        if conn:
            conn.rollback()
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    populate_member_table()
