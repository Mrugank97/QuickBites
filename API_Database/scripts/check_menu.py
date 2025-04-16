"""
Script to check if there are any menu items in the database
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

def check_menu():
    """Check if there are any menu items in the database"""
    conn = None
    cursor = None

    try:
        # Connect to the database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)

        # Check if menu table exists
        cursor.execute("""
            SELECT COUNT(*) as count FROM information_schema.tables
            WHERE table_schema = 'cs432g11' AND table_name = 'menu'
        """)
        result = cursor.fetchone()
        if result and result['count'] > 0:
            logging.info("menu table exists")
        else:
            logging.warning("menu table does not exist")
            return

        # Check if there are any menu items
        cursor.execute("SELECT COUNT(*) as count FROM menu")
        result = cursor.fetchone()
        logging.info(f"Found {result['count']} menu items")

        # Check if there are any outlets
        cursor.execute("SELECT COUNT(*) as count FROM outlet")
        result = cursor.fetchone()
        logging.info(f"Found {result['count']} outlets")

        # Get all outlets
        cursor.execute("SELECT * FROM outlet")
        outlets = cursor.fetchall()
        for outlet in outlets:
            logging.info(f"Outlet: {outlet['name']} (ID: {outlet['outlet_id']})")

            # Get menu items for this outlet
            cursor.execute("SELECT * FROM menu WHERE outlet_id = %s", (outlet['outlet_id'],))
            menu_items = cursor.fetchall()
            if menu_items:
                for item in menu_items:
                    logging.info(f"  - {item['item_name']} (₹{item['price']}) - Available: {item['available']}")
            else:
                logging.warning(f"  No menu items found for outlet {outlet['name']}")

    except mysql.connector.Error as e:
        logging.error(f"Database error: {str(e)}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    check_menu()
