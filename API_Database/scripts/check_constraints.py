"""
Script to check constraints on the orders table
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

def check_constraints():
    """Check constraints on the orders table"""
    conn = None
    cursor = None

    try:
        # Connect to the database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Check table structure
        cursor.execute("DESCRIBE orders")
        logging.info("Orders table structure:")
        for row in cursor:
            logging.info(row)

        # Check constraints
        cursor.execute("""
            SELECT CONSTRAINT_NAME, TABLE_NAME, COLUMN_NAME, REFERENCED_TABLE_NAME, REFERENCED_COLUMN_NAME
            FROM information_schema.KEY_COLUMN_USAGE
            WHERE TABLE_NAME = 'orders' AND CONSTRAINT_NAME != 'PRIMARY'
        """)
        logging.info("Orders table constraints:")
        for row in cursor:
            logging.info(row)

    except mysql.connector.Error as e:
        logging.error(f"Database error: {str(e)}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    check_constraints()
