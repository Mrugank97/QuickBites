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
        logging.error(f"Database connection failed: {str(e)}")
        raise

def update_outlet_manager_table():
    """Add auto_assigned column to outlet_manager table"""
    try:
        conn = get_db_connection(False)  # Use project database
        cursor = conn.cursor(dictionary=True)
        
        # Check if auto_assigned column already exists
        cursor.execute("DESCRIBE outlet_manager")
        columns = cursor.fetchall()
        
        column_exists = any(col['Field'] == 'auto_assigned' for col in columns)
        
        if not column_exists:
            print("Adding auto_assigned column to outlet_manager table...")
            cursor.execute("ALTER TABLE outlet_manager ADD COLUMN auto_assigned BOOLEAN DEFAULT FALSE")
            conn.commit()
            print("Column added successfully!")
        else:
            print("auto_assigned column already exists in outlet_manager table")
        
        # Set all existing assignments to manual (auto_assigned = FALSE)
        cursor.execute("UPDATE outlet_manager SET auto_assigned = FALSE WHERE auto_assigned IS NULL")
        conn.commit()
        print("Updated existing assignments to manual (auto_assigned = FALSE)")
        
        cursor.close()
        conn.close()
        
        print("Database schema update completed successfully!")
    except Exception as e:
        print(f"Error updating database schema: {str(e)}")

if __name__ == "__main__":
    update_outlet_manager_table()
