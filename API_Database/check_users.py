"""
Script to check available users in the database
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
    "database": "cs432cims"  # Use CIMS database
}

def check_users():
    """Check available users in the database"""
    conn = None
    cursor = None
    
    try:
        # Connect to the database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        
        # Check users in the members table
        cursor.execute("""
            SELECT m.ID, m.UserName, l.Role
            FROM members m
            JOIN Login l ON m.ID = l.MemberID
            LIMIT 10
        """)
        users = cursor.fetchall()
        
        logging.info(f"Found {len(users)} users:")
        for user in users:
            logging.info(f"  ID: {user['ID']}, Username: {user['UserName']}, Role: {user['Role']}")
        
    except mysql.connector.Error as e:
        logging.error(f"Database error: {str(e)}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    check_users()
