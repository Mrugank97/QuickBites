"""
Script to enforce one-to-one relationship between outlets and managers
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

def enforce_one_to_one():
    """Enforce one-to-one relationship between outlets and managers"""
    conn = None
    cursor = None
    
    try:
        # Connect to the database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        
        # First, clear all existing assignments
        cursor.execute("DELETE FROM outlet_manager")
        logging.info("Cleared all existing outlet-manager assignments")
        
        # Get all outlets
        cursor.execute("SELECT * FROM outlet ORDER BY outlet_id")
        outlets = cursor.fetchall()
        
        # Get all managers (users with Manager role)
        cursor.execute("""
            SELECT m.ID, m.UserName
            FROM cs432cims.members m
            JOIN cs432cims.Login l ON m.ID = l.MemberID
            WHERE l.Role = 'Manager' OR l.Role LIKE '%manager%'
            ORDER BY m.ID
        """)
        managers = cursor.fetchall()
        
        logging.info(f"Found {len(outlets)} outlets and {len(managers)} managers")
        
        # Assign one manager to each outlet
        assignments = []
        for i in range(min(len(outlets), len(managers))):
            outlet = outlets[i]
            manager = managers[i]
            
            assignments.append({
                'outlet_id': outlet['outlet_id'],
                'outlet_name': outlet['name'],
                'manager_id': manager['ID'],
                'manager_name': manager['UserName']
            })
            
            # Insert the assignment
            cursor.execute("""
                INSERT INTO outlet_manager (member_id, outlet_id)
                VALUES (%s, %s)
            """, (manager['ID'], outlet['outlet_id']))
            
            logging.info(f"Assigned manager {manager['UserName']} (ID: {manager['ID']}) to outlet {outlet['name']} (ID: {outlet['outlet_id']})")
        
        # If there are more outlets than managers, create new manager accounts
        if len(outlets) > len(managers):
            logging.info(f"Need to create {len(outlets) - len(managers)} more managers")
            
            for i in range(len(managers), len(outlets)):
                outlet = outlets[i]
                
                # Create a new manager account
                username = f"manager_{outlet['outlet_id']}"
                password = "password"  # Default password
                
                # Check if username already exists
                cursor.execute("""
                    SELECT ID FROM cs432cims.members
                    WHERE UserName = %s
                """, (username,))
                existing = cursor.fetchone()
                
                if existing:
                    manager_id = existing['ID']
                    logging.info(f"Manager {username} already exists with ID: {manager_id}")
                else:
                    # Insert into members table
                    cursor.execute("""
                        INSERT INTO cs432cims.members (UserName, emailID, DoB)
                        VALUES (%s, %s, %s)
                    """, (username, f"{username}@example.com", '1990-01-01'))
                    
                    # Get the newly created member ID
                    cursor.execute("""
                        SELECT ID FROM cs432cims.members
                        WHERE UserName = %s
                    """, (username,))
                    result = cursor.fetchone()
                    manager_id = result['ID']
                    
                    # Create login entry
                    import hashlib
                    hashed_password = hashlib.md5(password.encode()).hexdigest()
                    
                    cursor.execute("""
                        INSERT INTO cs432cims.Login (MemberID, Password, Role)
                        VALUES (%s, %s, %s)
                    """, (manager_id, hashed_password, 'Manager'))
                    
                    logging.info(f"Created new manager {username} (ID: {manager_id})")
                
                # Assign to outlet
                cursor.execute("""
                    INSERT INTO outlet_manager (member_id, outlet_id)
                    VALUES (%s, %s)
                """, (manager_id, outlet['outlet_id']))
                
                assignments.append({
                    'outlet_id': outlet['outlet_id'],
                    'outlet_name': outlet['name'],
                    'manager_id': manager_id,
                    'manager_name': username
                })
                
                logging.info(f"Assigned manager {username} (ID: {manager_id}) to outlet {outlet['name']} (ID: {outlet['outlet_id']})")
        
        # Commit the changes
        conn.commit()
        
        # Print summary of assignments
        logging.info("Final outlet-manager assignments:")
        for assignment in assignments:
            logging.info(f"  Outlet: {assignment['outlet_name']} (ID: {assignment['outlet_id']}) -> Manager: {assignment['manager_name']} (ID: {assignment['manager_id']})")
        
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
    enforce_one_to_one()
