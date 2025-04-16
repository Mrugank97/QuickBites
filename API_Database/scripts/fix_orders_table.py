"""
Script to fix the orders table in the cs432g11 database
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

def fix_orders_table():
    """Fix the orders table to allow any member to place orders"""
    conn = None
    cursor = None

    try:
        # Connect to the database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Check if there are any orders in the table
        cursor.execute("SELECT COUNT(*) FROM orders")
        count = cursor.fetchone()[0]
        logging.info(f"Found {count} orders in the table")

        if count > 0:
            # There are orders, so we need to be careful
            logging.info("There are existing orders, so we'll create a new table")

            # Create a new orders table without the foreign key constraint
            cursor.execute("""
                CREATE TABLE new_orders (
                    order_id INT PRIMARY KEY AUTO_INCREMENT,
                    member_id INT NOT NULL,
                    outlet_id INT NOT NULL,
                    total_amount DECIMAL(10,2) NOT NULL,
                    order_status ENUM('Pending', 'Completed', 'Cancelled') DEFAULT 'Pending',
                    order_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (outlet_id) REFERENCES outlet(outlet_id) ON DELETE CASCADE
                )
            """)
            logging.info("Created new orders table without member_id foreign key constraint")

            # Copy data from old table to new table
            cursor.execute("INSERT INTO new_orders SELECT * FROM orders")
            logging.info(f"Copied {count} orders to new table")

            # Rename tables
            cursor.execute("RENAME TABLE orders TO old_orders, new_orders TO orders")
            logging.info("Renamed tables")
        else:
            # No orders, so we can just drop and recreate the table
            logging.info("No existing orders, so we'll drop and recreate the table")

            # Drop the order_items table first since it references orders
            cursor.execute("DROP TABLE IF EXISTS order_items")
            logging.info("Dropped order_items table")

            # Drop the old table
            cursor.execute("DROP TABLE orders")
            logging.info("Dropped orders table")

            # Create a new orders table without the foreign key constraint
            cursor.execute("""
                CREATE TABLE orders (
                    order_id INT PRIMARY KEY AUTO_INCREMENT,
                    member_id INT NOT NULL,
                    outlet_id INT NOT NULL,
                    total_amount DECIMAL(10,2) NOT NULL,
                    order_status ENUM('Pending', 'Completed', 'Cancelled') DEFAULT 'Pending',
                    order_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (outlet_id) REFERENCES outlet(outlet_id) ON DELETE CASCADE
                )
            """)
            logging.info("Created new orders table without member_id foreign key constraint")

            # Recreate the order_items table
            cursor.execute("""
                CREATE TABLE order_items (
                    order_item_id INT PRIMARY KEY AUTO_INCREMENT,
                    order_id INT NOT NULL,
                    menu_id INT NOT NULL,
                    quantity INT NOT NULL CHECK (quantity > 0),
                    subtotal DECIMAL(10,2) NOT NULL,
                    FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE,
                    FOREIGN KEY (menu_id) REFERENCES menu(menu_id) ON DELETE CASCADE
                )
            """)
            logging.info("Recreated order_items table")

        # Commit the changes
        conn.commit()
        logging.info("Orders table fixed successfully")

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
    fix_orders_table()
