"""
Script to check if there's any data in the menu table
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

def check_menu_data():
    """Check if there's any data in the menu table"""
    conn = None
    cursor = None
    
    try:
        # Connect to the database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        
        # Check menu table
        cursor.execute("SELECT * FROM menu")
        menu_items = cursor.fetchall()
        
        print(f"\nFound {len(menu_items)} items in the menu table:")
        if menu_items:
            for item in menu_items:
                print(f"ID: {item['menu_id']}, Name: {item['item_name']}, Price: {item['price']}, Outlet ID: {item['outlet_id']}")
        else:
            print("No menu items found. Let's insert some sample data.")
            
            # Insert sample menu items for each outlet
            outlets = [1, 2, 3, 4, 5, 6]  # Outlet IDs
            
            # Menu items for Dawat (outlet_id = 1)
            cursor.execute("""
                INSERT INTO menu (item_name, price, available, outlet_id) VALUES
                ('Veg Biryani', 120.00, TRUE, 1),
                ('Chicken Biryani', 180.00, TRUE, 1),
                ('Paneer Butter Masala', 150.00, TRUE, 1),
                ('Butter Naan', 30.00, TRUE, 1),
                ('Jeera Rice', 80.00, TRUE, 1)
            """)
            
            # Menu items for Just Chill (outlet_id = 2)
            cursor.execute("""
                INSERT INTO menu (item_name, price, available, outlet_id) VALUES
                ('Cold Coffee', 60.00, TRUE, 2),
                ('Chocolate Shake', 80.00, TRUE, 2),
                ('Vanilla Ice Cream', 50.00, TRUE, 2),
                ('Mango Shake', 70.00, TRUE, 2),
                ('Oreo Shake', 90.00, TRUE, 2)
            """)
            
            # Menu items for Tea Post (outlet_id = 3)
            cursor.execute("""
                INSERT INTO menu (item_name, price, available, outlet_id) VALUES
                ('Masala Chai', 20.00, TRUE, 3),
                ('Lemon Tea', 25.00, TRUE, 3),
                ('Green Tea', 30.00, TRUE, 3),
                ('Biscuits', 10.00, TRUE, 3),
                ('Samosa', 15.00, TRUE, 3)
            """)
            
            # Menu items for Madurai Chaat & More (outlet_id = 4)
            cursor.execute("""
                INSERT INTO menu (item_name, price, available, outlet_id) VALUES
                ('Pani Puri', 40.00, TRUE, 4),
                ('Bhel Puri', 50.00, TRUE, 4),
                ('Dahi Puri', 60.00, TRUE, 4),
                ('Sev Puri', 45.00, TRUE, 4),
                ('Masala Dosa', 80.00, TRUE, 4)
            """)
            
            # Menu items for AS FastFood (outlet_id = 5)
            cursor.execute("""
                INSERT INTO menu (item_name, price, available, outlet_id) VALUES
                ('Veg Burger', 70.00, TRUE, 5),
                ('Chicken Burger', 90.00, TRUE, 5),
                ('French Fries', 50.00, TRUE, 5),
                ('Veg Sandwich', 60.00, TRUE, 5),
                ('Chicken Sandwich', 80.00, TRUE, 5)
            """)
            
            # Menu items for VS Fastfood (outlet_id = 6)
            cursor.execute("""
                INSERT INTO menu (item_name, price, available, outlet_id) VALUES
                ('Veg Manchurian', 100.00, TRUE, 6),
                ('Hakka Noodles', 90.00, TRUE, 6),
                ('Fried Rice', 80.00, TRUE, 6),
                ('Chilli Paneer', 120.00, TRUE, 6),
                ('Spring Rolls', 60.00, TRUE, 6)
            """)
            
            conn.commit()
            print("Sample menu items inserted successfully!")
            
            # Verify the inserted data
            cursor.execute("SELECT * FROM menu")
            menu_items = cursor.fetchall()
            print(f"\nNow there are {len(menu_items)} items in the menu table:")
            for item in menu_items:
                print(f"ID: {item['menu_id']}, Name: {item['item_name']}, Price: {item['price']}, Outlet ID: {item['outlet_id']}")
        
    except mysql.connector.Error as e:
        logging.error(f"Database error: {str(e)}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    check_menu_data()
