"""
Script to update menu items in the database with the new comprehensive menu
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

def update_menu():
    """Update menu items in the database"""
    conn = None
    cursor = None

    try:
        # Connect to the database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # First, check if we need to update the outlets
        cursor.execute("SELECT outlet_id, name FROM outlet")
        existing_outlets = cursor.fetchall()
        logging.info(f"Found {len(existing_outlets)} existing outlets")
        
        # Map of outlet IDs to names
        outlet_map = {outlet_id: name for outlet_id, name in existing_outlets}
        
        # Check if we need to update outlets
        outlets_to_update = []
        if 1 not in outlet_map or outlet_map[1] != 'Dawat':
            outlets_to_update.append((1, 'Dawat', 'H-Hostel, Ground Floor'))
        if 2 not in outlet_map or outlet_map[2] != 'Just Chill':
            outlets_to_update.append((2, 'Just Chill', 'B-Hostel, Ground Floor'))
        if 3 not in outlet_map or outlet_map[3] != 'Tea Post':
            outlets_to_update.append((3, 'Tea Post', 'E-Hostel, Ground Floor'))
        if 4 not in outlet_map or outlet_map[4] != 'AS FastFood':
            outlets_to_update.append((4, 'AS FastFood', 'I-Hostel, Ground Floor'))
        if 5 not in outlet_map or outlet_map[5] != 'VS Fastfood':
            outlets_to_update.append((5, 'VS Fastfood', 'H-Hostel, Ground Floor'))
        if 6 not in outlet_map or outlet_map[6] != 'Madurai Chaat & More':
            outlets_to_update.append((6, 'Madurai Chaat & More', 'Near Sports Complex'))
        
        # Update outlets if needed
        if outlets_to_update:
            logging.info(f"Updating {len(outlets_to_update)} outlets")
            for outlet_id, name, location in outlets_to_update:
                cursor.execute("""
                    INSERT INTO outlet (outlet_id, name, location) 
                    VALUES (%s, %s, %s)
                    ON DUPLICATE KEY UPDATE name = %s, location = %s
                """, (outlet_id, name, location, name, location))
            conn.commit()
        
        # Now check the menu items for each outlet
        for outlet_id in range(1, 7):
            cursor.execute("SELECT COUNT(*) FROM menu WHERE outlet_id = %s", (outlet_id,))
            count = cursor.fetchone()[0]
            logging.info(f"Found {count} menu items for outlet {outlet_id}")
            
            # If there are fewer than 10 items, we'll update the menu
            if count < 10:
                logging.info(f"Updating menu for outlet {outlet_id}")
                
                # First, delete existing menu items for this outlet
                cursor.execute("DELETE FROM menu WHERE outlet_id = %s", (outlet_id,))
                
                # Now add the new menu items based on outlet_id
                if outlet_id == 1:  # Dawat
                    menu_items = [
                        ('Chicken Shawarma (7in Roll)', 100, True),
                        ('Chicken Lollypop (4pcs)', 120, True),
                        ('Chicken Lollypop (2pcs)', 70, True),
                        ('Chicken Hakka Noodles (300gm)', 90, True),
                        ('Chicken Manchurian Noodles (350gm)', 100, True),
                        ('Chicken Biryani Boneless (300gm)', 140, True),
                        ('Chicken Biryani Bone (2-Pcs) (300gm)', 70, True),
                        ('Chicken Fried Rice (250gm)', 70, True),
                        ('Chicken Sezwan Fried Rice (250gm)', 80, True),
                        ('Chicken Chilly Dry (5-PCS)', 140, True),
                        ('Chicken Curry Thali (Chi-Curry, Rice, 4-Chapati)', 130, True),
                        ('Butter Chicken Thali (Butter Chi, Rice, 4-Chapati)', 150, True),
                        ('Chinese Combo (1 PCS Lollipop, Chicken Fried Rice, Chicken Noodles)', 140, True),
                        ('Chicken Curry (3-pcs) (300gm)', 110, True),
                        ('Butter Chicken Boneless (350gm)', 140, True),
                        ('Egg Biryani (2-Egg) (250gm)', 65, True),
                        ('Egg Fried Rice (250gm)', 65, True),
                        ('Egg Curry / Masala', 60, True),
                        ('Egg Curry Thali (2-Egg) (Egg Curry, Rice, 4-Chapati)', 90, True),
                        ('Egg Kheema (2-Egg)', 60, True),
                        ('Egg Bhurji (2-Egg) (250gm)', 65, True),
                        ('Boil Egg (2pcs)', 30, True),
                        ('Masala Omelette', 40, True),
                        ('Fish Fried (1pcs)', 60, True),
                        ('Fish Biryani (1pcs)', 100, True),
                        ('Fish Fried Rice (250gm)', 100, True),
                        ('Fish Masala (1pcs)', 120, True),
                        ('Chapati', 7, True),
                        ('Plain Rice (300gm)', 40, True)
                    ]
                elif outlet_id == 2:  # Just Chill
                    menu_items = [
                        ('Manchow Soup', 35, True),
                        ('Manchurian Soup', 35, True),
                        ('Tomato-Basil Soup', 35, True),
                        ('Lemon-Coriander Soup', 35, True),
                        ('Veg Manchurian (Gravy/Dry) Half', 45, True),
                        ('Veg Manchurian (Gravy/Dry) Full', 65, True),
                        ('Veg Hakka Noodles Half', 45, True),
                        ('Veg Hakka Noodles Full', 65, True),
                        ('Manchurian Noodles Half', 45, True),
                        ('Manchurian Noodles Full', 65, True),
                        ('Schezwan Noodles Half', 45, True),
                        ('Schezwan Noodles Full', 65, True),
                        ('Paneer Chilli', 90, True),
                        ('Veg Fried Rice Half', 45, True),
                        ('Veg Fried Rice Full', 65, True),
                        ('Manchurian Rice Half', 50, True),
                        ('Manchurian Rice Full', 70, True),
                        ('Schezwan Rice Half', 50, True),
                        ('Schezwan Rice Full', 70, True),
                        ('Spring Roll', 50, True)
                    ]
                elif outlet_id == 3:  # Tea Post
                    menu_items = [
                        ('Hot Tea (50ml)', 12.00, True),
                        ('Hot Tea (100ml)', 24.00, True),
                        ('Sugar Free Tea (100ml)', 32.00, True),
                        ('Elaichi Tea (100ml)', 32.00, True),
                        ('Ginger Tea (100ml)', 32.00, True),
                        ('Indian Masala Tea (100ml)', 32.00, True),
                        ('Gud Wali Chai (100ml)', 42.00, True),
                        ('Lemon Ice Tea (250ml)', 63.00, True),
                        ('Blueberry Rose Mint Ice Tea (250ml)', 63.00, True),
                        ('Peach Ice Tea (250ml)', 63.00, True),
                        ('Black Tea (160ml)', 32.00, True),
                        ('Kavo Tea (160ml)', 32.00, True),
                        ('Green Tea (160ml)', 32.00, True),
                        ('Hot Coffee (100ml)', 30.00, True),
                        ('Hot Vanilla Coffee (100ml)', 42.00, True),
                        ('Black Coffee (160ml)', 32.00, True),
                        ('Cold Coffee (250ml)', 74.00, True),
                        ('Cappuccino (250ml)', 79.00, True),
                        ('Hazelnut Coffee (250ml)', 79.00, True),
                        ('Hot Milk (160ml)', 25.00, True)
                    ]
                elif outlet_id == 4:  # AS FastFood
                    menu_items = [
                        ('Bred Butter (Regular)', 30, True),
                        ('Veg Sandwich (Regular)', 50, True),
                        ('Veg Cheese Sandwich (Regular)', 60, True),
                        ('Aloo Mutter Sandwich (Regular)', 50, True),
                        ('Aloo Veg Sandwich', 50, True),
                        ('Cheese Sandwich (Regular)', 50, True),
                        ('Cheese Chutney Sandwich (Regular)', 50, True),
                        ('Butter Jam Sandwich (Regular)', 40, True),
                        ('Cheese Jam Sandwich (Regular)', 50, True),
                        ('Chocolate Sandwich (Regular)', 40, True),
                        ('Cheese Chocolate Sandwich (Regular)', 60, True),
                        ('Corn Capsicum Sandwich (Grill)', 100, True),
                        ('Panjabi Tadka Sandwich (Grill)', 100, True),
                        ('A.S SPL Club Sandwich (Grill)', 110, True),
                        ('Vada Pav', 30, True),
                        ('Peri Peri Vada Pav', 40, True),
                        ('Cheese Vada Pav', 50, True),
                        ('Maska Bun', 35, True),
                        ('Jam Maska Bun', 40, True),
                        ('Chocolate Maska Bun', 40, True)
                    ]
                elif outlet_id == 5:  # VS Fastfood
                    menu_items = [
                        ('Bread Butter (Reg)', 25.00, True),
                        ('Bread Butter (Grill)', 35.00, True),
                        ('Butter Jam (Reg)', 35.00, True),
                        ('Butter Jam (Grill)', 45.00, True),
                        ('Vegetable Sandwich (Reg)', 30.00, True),
                        ('Vegetable Sandwich (Grill)', 45.00, True),
                        ('Aloo Matar Sandwich (Reg)', 35.00, True),
                        ('Aloo Matar Sandwich (Grill)', 50.00, True),
                        ('Veg Cheese Sandwich (Reg)', 50.00, True),
                        ('Veg Cheese Sandwich (Grill)', 60.00, True),
                        ('Aloo Cheese Sandwich (Reg)', 50.00, True),
                        ('Aloo Cheese Sandwich (Grill)', 60.00, True),
                        ('Cheese Sandwich (Reg)', 45.00, True),
                        ('Cheese Sandwich (Grill)', 55.00, True),
                        ('Cheese Chutney Sandwich (Reg)', 50.00, True),
                        ('Cheese Chutney Sandwich (Grill)', 60.00, True),
                        ('Cheese Jam Sandwich (Reg)', 45.00, True),
                        ('Cheese Jam Sandwich (Grill)', 55.00, True),
                        ('Chocolate Sandwich (Reg)', 55.00, True),
                        ('Chocolate Sandwich (Grill)', 70.00, True)
                    ]
                elif outlet_id == 6:  # Madurai Chaat & More
                    menu_items = [
                        ('Pani Puri (6)', 20, True),
                        ('Sev Puri (6)', 50, True),
                        ('Bhel Puri', 50, True),
                        ('Chutney Puri (6)', 60, True),
                        ('Kachori (2)', 40, True),
                        ('Samosa (2)', 40, True),
                        ('Pyaaz Kachori (2)', 50, True),
                        ('Dahi Puri (6)', 60, True),
                        ('Samosa Chaat', 70, True),
                        ('Kachori Chaat', 70, True),
                        ('Pyaaz Kachori Chaat', 80, True),
                        ('Raj Kachori', 80, True),
                        ('Chole Tikki', 80, True),
                        ('Chole Samosa', 80, True),
                        ('Dahi Bhalla', 90, True),
                        ('Ragda Pattice', 90, True),
                        ('Idli (2 pcs)', 50, True),
                        ('Medu Vada (2 pcs)', 50, True),
                        ('Idli Vada Combo', 60, True),
                        ('Mini Idli (10 pcs)', 70, True)
                    ]
                
                # Insert the menu items
                for item_name, price, available in menu_items:
                    cursor.execute("""
                        INSERT INTO menu (item_name, price, available, outlet_id)
                        VALUES (%s, %s, %s, %s)
                    """, (item_name, price, available, outlet_id))
                
                conn.commit()
                logging.info(f"Added {len(menu_items)} menu items for outlet {outlet_id}")
        
        logging.info("Menu update completed successfully")

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
    update_menu()
