"""
Script to set up the outlet_manager table and relationships
"""
import mysql.connector
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Database configuration
db_config = {
    "host": "10.0.116.125",
    "user": "cs432g11",
    "password": "pXqJ5NYz",
    "database": "cs432g11"
}

def setup_outlet_manager_table():
    """Set up the outlet_manager table and relationships"""
    conn = None
    cursor = None
    
    try:
        # Connect to the database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        
        # Check if outlet table exists
        cursor.execute("""
            SELECT COUNT(*) as count FROM information_schema.tables
            WHERE table_schema = 'cs432g11' AND table_name = 'outlet'
        """)
        result = cursor.fetchone()
        
        if result and result[0] == 0:
            logging.info("Creating outlet table...")
            cursor.execute("""
                CREATE TABLE outlet (
                    outlet_id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    location VARCHAR(255),
                    status VARCHAR(20) DEFAULT 'Active'
                )
            """)
            logging.info("Outlet table created successfully")
            
            # Insert sample outlets
            logging.info("Inserting sample outlets...")
            outlets = [
                ("Dawat", "Academic Area", "Active"),
                ("Just Chill", "Near Library", "Active"),
                ("Tea Post", "Near Hostel Complex", "Active"),
                ("AS FastFood", "Academic Block", "Active"),
                ("VS Fastfood", "Near Sports Complex", "Active"),
                ("Madurai Chaat & More", "Near Main Gate", "Active")
            ]
            
            cursor.executemany("""
                INSERT INTO outlet (name, location, status)
                VALUES (%s, %s, %s)
            """, outlets)
            logging.info(f"Inserted {len(outlets)} sample outlets")
        else:
            logging.info("Outlet table already exists")
        
        # Check if outlet_manager table exists
        cursor.execute("""
            SELECT COUNT(*) as count FROM information_schema.tables
            WHERE table_schema = 'cs432g11' AND table_name = 'outlet_manager'
        """)
        result = cursor.fetchone()
        
        if result and result[0] == 0:
            logging.info("Creating outlet_manager table...")
            cursor.execute("""
                CREATE TABLE outlet_manager (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    member_id INT NOT NULL,
                    outlet_id INT NOT NULL,
                    FOREIGN KEY (outlet_id) REFERENCES outlet(outlet_id)
                )
            """)
            logging.info("Outlet_manager table created successfully")
        else:
            logging.info("Outlet_manager table already exists")
            
        # Check if there are any outlet managers assigned
        cursor.execute("SELECT COUNT(*) as count FROM outlet_manager")
        result = cursor.fetchone()
        
        if result and result[0] == 0:
            logging.info("No outlet managers assigned. Checking for users with OutletManager role...")
            
            # Get users with OutletManager role from CIMS database
            cursor.execute("""
                SELECT m.ID as member_id, m.UserName
                FROM cs432cims.members m
                JOIN cs432cims.Login l ON m.ID = l.MemberID
                WHERE l.Role LIKE '%outlet%' OR l.Role LIKE '%manager%'
                LIMIT 6
            """)
            managers = cursor.fetchall()
            
            if managers:
                logging.info(f"Found {len(managers)} outlet managers")
                
                # Get outlets
                cursor.execute("SELECT outlet_id FROM outlet ORDER BY outlet_id LIMIT 6")
                outlets = cursor.fetchall()
                
                if outlets:
                    # Assign managers to outlets
                    assignments = []
                    for i in range(min(len(managers), len(outlets))):
                        assignments.append((managers[i][0], outlets[i][0]))
                    
                    cursor.executemany("""
                        INSERT INTO outlet_manager (member_id, outlet_id)
                        VALUES (%s, %s)
                    """, assignments)
                    
                    logging.info(f"Assigned {len(assignments)} managers to outlets")
                    
                    # Log the assignments
                    for i in range(len(assignments)):
                        logging.info(f"Assigned manager {managers[i][1]} (ID: {managers[i][0]}) to outlet ID: {outlets[i][0]}")
            else:
                logging.info("No users with OutletManager role found")
                
                # Create a test outlet manager in CIMS
                logging.info("Creating a test outlet manager in CIMS...")
                
                # Check if test manager already exists
                cursor.execute("""
                    SELECT ID FROM cs432cims.members
                    WHERE UserName = 'outlet_manager'
                """)
                existing_manager = cursor.fetchone()
                
                if existing_manager:
                    manager_id = existing_manager[0]
                    logging.info(f"Test manager already exists with ID: {manager_id}")
                else:
                    # Insert test manager into members table
                    cursor.execute("""
                        INSERT INTO cs432cims.members (UserName, Email, DOB)
                        VALUES ('outlet_manager', 'outlet_manager@example.com', '1990-01-01')
                    """)
                    manager_id = cursor.lastrowid
                    
                    # Insert login credentials
                    cursor.execute("""
                        INSERT INTO cs432cims.Login (MemberID, Password, Role)
                        VALUES (%s, 'password', 'OutletManager')
                    """)
                    
                    logging.info(f"Created test outlet manager with ID: {manager_id}")
                
                # Assign test manager to first outlet
                cursor.execute("SELECT outlet_id FROM outlet ORDER BY outlet_id LIMIT 1")
                outlet = cursor.fetchone()
                
                if outlet:
                    cursor.execute("""
                        INSERT INTO outlet_manager (member_id, outlet_id)
                        VALUES (%s, %s)
                    """, (manager_id, outlet[0]))
                    
                    logging.info(f"Assigned test manager (ID: {manager_id}) to outlet ID: {outlet[0]}")
        
        # Commit the changes
        conn.commit()
        logging.info("All changes committed successfully")
        
    except mysql.connector.Error as e:
        logging.error(f"Database error: {str(e)}")
        if conn:
            conn.rollback()
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    setup_outlet_manager_table()
