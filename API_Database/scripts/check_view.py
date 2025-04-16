"""
Script to check the definition of the member_profiles view
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

def check_view():
    """Check the definition of the member_profiles view"""
    conn = None
    cursor = None
    
    try:
        # Connect to the database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        
        # Get the view definition
        cursor.execute("SHOW CREATE VIEW member_profiles")
        view_def = cursor.fetchone()
        
        if view_def:
            print("\n=== member_profiles View Definition ===")
            print(view_def[1])
        else:
            print("View not found")
        
    except mysql.connector.Error as e:
        logging.error(f"Database error: {str(e)}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    check_view()
