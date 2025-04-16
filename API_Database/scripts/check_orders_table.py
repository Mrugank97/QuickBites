"""
Script to check the orders table structure
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

def check_orders_table():
    """Check the orders table structure"""
    conn = None
    cursor = None

    try:
        # Connect to the database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Check if orders table exists
        cursor.execute("""
            SELECT COUNT(*) as count FROM information_schema.tables
            WHERE table_schema = 'cs432g11' AND table_name = 'orders'
        """)
        result = cursor.fetchone()
        if result and result[0] > 0:
            logging.info("orders table exists")
        else:
            logging.warning("orders table does not exist")
            return

        # Check the structure of the orders table
        cursor.execute("DESCRIBE orders")
        columns = cursor.fetchall()
        logging.info("Orders table structure:")
        for column in columns:
            logging.info(f"  {column}")

        # Check if there are any orders
        cursor.execute("SELECT COUNT(*) FROM orders")
        count = cursor.fetchone()[0]
        logging.info(f"Found {count} orders in the database")

        # Check if there are any foreign key constraints
        cursor.execute("""
            SELECT TABLE_NAME, COLUMN_NAME, CONSTRAINT_NAME, REFERENCED_TABLE_NAME, REFERENCED_COLUMN_NAME
            FROM information_schema.KEY_COLUMN_USAGE
            WHERE TABLE_SCHEMA = 'cs432g11' AND TABLE_NAME = 'orders' AND REFERENCED_TABLE_NAME IS NOT NULL
        """)
        constraints = cursor.fetchall()
        logging.info("Foreign key constraints on orders table:")
        for constraint in constraints:
            logging.info(f"  {constraint}")

        # Check if there are any order_items
        cursor.execute("SELECT COUNT(*) FROM order_items")
        count = cursor.fetchone()[0]
        logging.info(f"Found {count} order items in the database")

        # Check the structure of the order_items table
        cursor.execute("DESCRIBE order_items")
        columns = cursor.fetchall()
        logging.info("Order_items table structure:")
        for column in columns:
            logging.info(f"  {column}")

        # Check if there are any foreign key constraints on order_items
        cursor.execute("""
            SELECT TABLE_NAME, COLUMN_NAME, CONSTRAINT_NAME, REFERENCED_TABLE_NAME, REFERENCED_COLUMN_NAME
            FROM information_schema.KEY_COLUMN_USAGE
            WHERE TABLE_SCHEMA = 'cs432g11' AND TABLE_NAME = 'order_items' AND REFERENCED_TABLE_NAME IS NOT NULL
        """)
        constraints = cursor.fetchall()
        logging.info("Foreign key constraints on order_items table:")
        for constraint in constraints:
            logging.info(f"  {constraint}")

    except mysql.connector.Error as e:
        logging.error(f"Database error: {str(e)}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    check_orders_table()
