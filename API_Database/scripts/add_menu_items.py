"""
Script to add sample menu items to the database
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

def add_menu_items():
    """Add sample menu items to the database"""
    conn = None
    cursor = None

    try:
        # Connect to the database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Check if there are already menu items
        cursor.execute("SELECT COUNT(*) FROM menu")
        count = cursor.fetchone()[0]
        
        if count > 0:
            logging.info(f"There are already {count} menu items in the database")
            return
        
        # Insert sample menu items for each outlet
        # Outlet 1: Dawat
        cursor.execute("""
            INSERT INTO menu (item_name, price, available, outlet_id) VALUES
            ('Veg Biryani', 120.00, TRUE, 1),
            ('Chicken Biryani', 180.00, TRUE, 1),
            ('Paneer Butter Masala', 150.00, TRUE, 1),
            ('Butter Naan', 30.00, TRUE, 1),
            ('Jeera Rice', 80.00, TRUE, 1)
        """)
        logging.info("Added menu items for Dawat")

        # Outlet 2: Just Chill
        cursor.execute("""
            INSERT INTO menu (item_name, price, available, outlet_id) VALUES
            ('Cold Coffee', 60.00, TRUE, 2),
            ('Chocolate Shake', 80.00, TRUE, 2),
            ('Vanilla Ice Cream', 50.00, TRUE, 2),
            ('Mango Shake', 70.00, TRUE, 2),
            ('Oreo Shake', 90.00, TRUE, 2)
        """)
        logging.info("Added menu items for Just Chill")

        # Outlet 3: Tea Post
        cursor.execute("""
            INSERT INTO menu (item_name, price, available, outlet_id) VALUES
            ('Masala Chai', 20.00, TRUE, 3),
            ('Lemon Tea', 25.00, TRUE, 3),
            ('Green Tea', 30.00, TRUE, 3),
            ('Biscuits', 10.00, TRUE, 3),
            ('Samosa', 15.00, TRUE, 3)
        """)
        logging.info("Added menu items for Tea Post")

        # Outlet 4: AS FastFood
        cursor.execute("""
            INSERT INTO menu (item_name, price, available, outlet_id) VALUES
            ('Pani Puri', 40.00, TRUE, 4),
            ('Bhel Puri', 50.00, TRUE, 4),
            ('Dahi Puri', 60.00, TRUE, 4),
            ('Sev Puri', 45.00, TRUE, 4),
            ('Masala Dosa', 80.00, TRUE, 4)
        """)
        logging.info("Added menu items for AS FastFood")

        # Outlet 5: VS Fastfood
        cursor.execute("""
            INSERT INTO menu (item_name, price, available, outlet_id) VALUES
            ('Veg Burger', 70.00, TRUE, 5),
            ('Chicken Burger', 90.00, TRUE, 5),
            ('French Fries', 50.00, TRUE, 5),
            ('Veg Sandwich', 60.00, TRUE, 5),
            ('Chicken Sandwich', 80.00, TRUE, 5)
        """)
        logging.info("Added menu items for VS Fastfood")

        # Outlet 6: Madurai Chaat & More
        cursor.execute("""
            INSERT INTO menu (item_name, price, available, outlet_id) VALUES
            ('Veg Manchurian', 100.00, TRUE, 6),
            ('Hakka Noodles', 90.00, TRUE, 6),
            ('Fried Rice', 80.00, TRUE, 6),
            ('Chilli Paneer', 120.00, TRUE, 6),
            ('Spring Rolls', 60.00, TRUE, 6)
        """)
        logging.info("Added menu items for Madurai Chaat & More")

        # Commit the changes
        conn.commit()
        logging.info("All menu items added successfully")

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
    add_menu_items()
