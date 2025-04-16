"""
Script to check the structure of the Login table
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
    "database": "cs432cims"  # CIMS database
}

def check_login_table():
    """Check the structure of the Login table"""
    conn = None
    cursor = None
    
    try:
        # Connect to the database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        
        # Check the structure of the Login table
        cursor.execute("DESCRIBE Login")
        columns = cursor.fetchall()
        
        logging.info("Login table structure:")
        for column in columns:
            logging.info(f"  {column[0]}: {column[1]}")
        
        # Check the current values in the Role column
        cursor.execute("SELECT DISTINCT Role FROM Login")
        roles = cursor.fetchall()
        
        logging.info("Current roles in the Login table:")
        for role in roles:
            logging.info(f"  {role[0]}")
        
    except mysql.connector.Error as e:
        logging.error(f"Database error: {str(e)}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    check_login_table()
