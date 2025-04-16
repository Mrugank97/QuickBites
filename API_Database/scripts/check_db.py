import mysql.connector

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

def check_outlet_manager_table():
    try:
        conn = get_db_connection(False)  # Use project database
        cursor = conn.cursor(dictionary=True)
        
        # Get table structure
        cursor.execute("DESCRIBE outlet_manager")
        columns = cursor.fetchall()
        print("Outlet Manager Table Structure:")
        for column in columns:
            print(column)
        
        # Get all records
        cursor.execute("SELECT * FROM outlet_manager")
        records = cursor.fetchall()
        print("\nOutlet Manager Records:")
        for record in records:
            print(record)
        
        # Get outlet details
        cursor.execute("SELECT * FROM outlet")
        outlets = cursor.fetchall()
        print("\nOutlet Records:")
        for outlet in outlets:
            print(outlet)
        
        # Get all assignments with outlet and manager details
        query = """
        SELECT om.outlet_id, o.name as outlet_name, om.member_id, m.UserName as manager_name
        FROM outlet_manager om
        JOIN outlet o ON om.outlet_id = o.outlet_id
        JOIN cs432cims.members m ON om.member_id = m.ID
        ORDER BY o.name
        """
        cursor.execute(query)
        assignments = cursor.fetchall()
        print("\nAssignments with Details:")
        for assignment in assignments:
            print(assignment)
        
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    check_outlet_manager_table()
