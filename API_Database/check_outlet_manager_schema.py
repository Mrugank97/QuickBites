import mysql.connector
import logging

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
        print(f"Database connection failed: {str(e)}")
        raise

def check_outlet_manager_schema():
    """Check the outlet_manager table schema and data"""
    try:
        conn = get_db_connection(False)  # Use project database
        cursor = conn.cursor(dictionary=True)
        
        # Check table structure
        print("=== OUTLET_MANAGER TABLE STRUCTURE ===")
        cursor.execute("DESCRIBE outlet_manager")
        columns = cursor.fetchall()
        for column in columns:
            print(column)
        
        # Check existing data
        print("\n=== OUTLET_MANAGER DATA ===")
        cursor.execute("SELECT * FROM outlet_manager")
        data = cursor.fetchall()
        for row in data:
            print(row)
        
        # Check outlet table structure
        print("\n=== OUTLET TABLE STRUCTURE ===")
        cursor.execute("DESCRIBE outlet")
        columns = cursor.fetchall()
        for column in columns:
            print(column)
        
        # Check outlet data
        print("\n=== OUTLET DATA ===")
        cursor.execute("SELECT * FROM outlet")
        data = cursor.fetchall()
        for row in data:
            print(row)
        
        # Check manager data in CIMS
        print("\n=== MANAGER DATA IN CIMS ===")
        cims_conn = get_db_connection(True)
        cims_cursor = cims_conn.cursor(dictionary=True)
        cims_cursor.execute("SELECT ID, UserName, emailID FROM members WHERE ID IN (SELECT MemberID FROM Login WHERE Role = 'Manager' OR Role LIKE '%manager%')")
        managers = cims_cursor.fetchall()
        for manager in managers:
            print(manager)
        
        # Check if there are any unassigned managers
        print("\n=== UNASSIGNED MANAGERS ===")
        query = """
        SELECT m.ID, m.UserName, m.emailID 
        FROM cs432cims.members m
        JOIN cs432cims.Login l ON m.ID = l.MemberID
        WHERE (l.Role = 'Manager' OR l.Role LIKE '%manager%')
        AND m.ID NOT IN (SELECT member_id FROM outlet_manager)
        """
        cursor.execute(query)
        unassigned = cursor.fetchall()
        for manager in unassigned:
            print(manager)
        
        # Check if there are any outlets without managers
        print("\n=== OUTLETS WITHOUT MANAGERS ===")
        query = """
        SELECT * FROM outlet 
        WHERE outlet_id NOT IN (SELECT outlet_id FROM outlet_manager)
        """
        cursor.execute(query)
        unassigned_outlets = cursor.fetchall()
        for outlet in unassigned_outlets:
            print(outlet)
        
        cursor.close()
        conn.close()
        cims_cursor.close()
        cims_conn.close()
        
    except Exception as e:
        print(f"Error checking schema: {str(e)}")

if __name__ == "__main__":
    check_outlet_manager_schema()
