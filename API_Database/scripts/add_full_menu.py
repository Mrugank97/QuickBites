"""
Script to add the full menu items to the database
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

def add_full_menu():
    """Add the full menu items to the database"""
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
        
        # Now add the full menu for each outlet
        # First, clear existing menu items
        for outlet_id in range(1, 7):
            cursor.execute("DELETE FROM menu WHERE outlet_id = %s", (outlet_id,))
            logging.info(f"Deleted existing menu items for outlet {outlet_id}")
        
        # Dawat menu
        dawat_menu = [
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
        
        # Just Chill menu
        just_chill_menu = [
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
            ('Spring Roll', 50, True),
            ('Dal Fry Half', 50, True),
            ('Dal Fry Full', 70, True),
            ('Paneer Masala Half', 80, True),
            ('Paneer Masala Full', 110, True),
            ('Paneer Butter Masala Half', 90, True),
            ('Paneer Butter Masala Full', 120, True),
            ('Paneer Kali Mirch Half', 110, True),
            ('Paneer Kali Mirch Full', 140, True),
            ('Kaju-Paneer Mix Masala Half', 110, True),
            ('Kaju-Paneer Mix Masala Full', 140, True),
            ('Chicken Dana Half', 50, True),
            ('Chicken Dana Full', 100, True),
            ('Chicken Lollipop (Dry/Gravy)', 90, True),
            ('Chicken Chilly Half', 100, True),
            ('Chicken Chilly Full', 150, True),
            ('Chicken Masala Half', 90, True),
            ('Chicken Masala Full', 140, True),
            ('Chicken Korma Half', 100, True),
            ('Chicken Korma Full', 150, True),
            ('Butter Chicken Half', 100, True),
            ('Butter Chicken Full', 150, True),
            ('Chicken Bhuna Masala Half', 120, True),
            ('Chicken Bhuna Masala Full', 170, True),
            ('Chicken Kolhapuri Half', 120, True),
            ('Chicken Kolhapuri Full', 170, True),
            ('Chicken Ghee Roast Half', 130, True),
            ('Chicken Ghee Roast Full', 180, True),
            ('Afghani Malai Chicken Half', 140, True),
            ('Afghani Malai Chicken Full', 190, True),
            ('Chicken Soup', 40, True),
            ('Chicken Fried Rice Half', 65, True),
            ('Chicken Fried Rice Full', 80, True),
            ('Chicken Schezwan Rice Half', 65, True),
            ('Chicken Schezwan Rice Full', 80, True),
            ('Chicken Noodles Half', 65, True),
            ('Chicken Noodles Full', 80, True),
            ('Chicken Schezwan Noodles Half', 65, True),
            ('Chicken Schezwan Noodles Full', 80, True),
            ('Chicken Triple Rice (Soup+Omelette+Rice+Noodle)', 85, True),
            ('Boiled Egg Half', 12, True),
            ('Boiled Egg Full', 20, True),
            ('Omelette + 2 Bread Half', 30, True),
            ('Omelette + 2 Bread Full', 40, True),
            ('Egg Burji + 2 Bread Half', 30, True),
            ('Egg Burji + 2 Bread Full', 40, True),
            ('Half-Fry + 2 Bread Half', 30, True),
            ('Half-Fry + 2 Bread Full', 40, True),
            ('Egg Masala (2 eggs)', 65, True),
            ('Egg Makhanwala (2 eggs)', 75, True),
            ('Egg Fried Rice Half', 50, True),
            ('Egg Fried Rice Full', 65, True),
            ('Egg Noodles Half', 45, True),
            ('Egg Noodles Full', 70, True),
            ('Chai (Elaichi Flavour) Small', 10, True),
            ('Chai (Elaichi Flavour) Large', 20, True),
            ('Special Chai (Chocolate, Almond, Pan, Rose, Vanilla) Small', 15, True),
            ('Special Chai (Chocolate, Almond, Pan, Rose, Vanilla) Large', 30, True),
            ('Bread', 5, True),
            ('Chapati', 10, True),
            ('Malabar Paratha', 20, True),
            ('Aloo Paratha', 35, True),
            ('Cheese Paratha', 40, True),
            ('Paneer Paratha', 50, True),
            ('Plain Rice', 40, True),
            ('Jeera Rice', 50, True),
            ('Special Kolhapuri Misal', 50, True),
            ('Special Kolhapuri Chicken Plate', 150, True),
            ('Vadapav', 20, True),
            ('Vada Sambhar', 40, True)
        ]
        
        # Tea Post menu
        tea_post_menu = [
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
            ('Hot Milk (160ml)', 25.00, True),
            ('Haldi Milk (160ml)', 32.00, True),
            ('Bournvita Hot (160ml)', 42.00, True),
            ('Bournvita Cold (160ml)', 42.00, True),
            ('Hot Chocolate (160ml)', 84.00, True),
            ('Chocolate Milk Shake (250ml)', 74.00, True),
            ('Rose Milk Shake (250ml)', 74.00, True),
            ('Strawberry Milk Shake (250ml)', 74.00, True),
            ('Fruit Punch (250ml)', 37.00, True),
            ('Lemon Ginger (250ml)', 37.00, True),
            ('Mojito (250ml)', 42.00, True),
            ('Poha (125gm)', 25.00, True),
            ('Upma (200gm)', 35.00, True),
            ('Thepla with Pickle (3 pieces)', 30.00, True),
            ('Khichu (250gm)', 35.00, True),
            ('Maskabun (With Butter, 110gm)', 30.00, True),
            ('Jam Bun (110gm)', 35.00, True),
            ('Spicy Bun', 45.00, True),
            ('Veggie Fingers (5 pieces)', 40.00, True),
            ('Cheese Garlic Bread (3 pieces)', 74.00, True),
            ('French Fries (120gm)', 68.00, True),
            ('French Fries-Peri Peri Sprinkle (120gm)', 78.00, True),
            ('French Fries-Deep Cheezy (140gm)', 95.00, True),
            ('Bread Butter (2 slices)', 32.00, True),
            ('Jam Butter (2 slices)', 32.00, True),
            ('Cheese Butter Sandwich (2 slices)', 53.00, True),
            ('Cheese Chutney Sandwich (2 slices)', 63.00, True),
            ('Mexican Cheese Sandwich (2 slices)', 84.00, True),
            ('Tandoori Paneer Sandwich (2 slices)', 84.00, True),
            ('Cheese Chilli Sandwich (2 slices)', 84.00, True),
            ('Peri Peri Sandwich (2 slices)', 84.00, True),
            ('Schezuan Paneer Sandwich (2 slices)', 84.00, True),
            ('Masala Noodles (150gm)', 42.00, True),
            ('Tadka Noodles (200gm)', 53.00, True),
            ('Extra Vegetable', 10.00, True),
            ('Extra Cheese', 25.00, True),
            ('Extra Namkeen', 5.00, True),
            ('Aluminum Foil Wrapping Charge', 5.00, True),
            ('Aloo Puff', 25.00, True),
            ('Chinese Puff', 30.00, True),
            ('Mexican Puff', 30.00, True)
        ]
        
        # AS FastFood menu
        as_fastfood_menu = [
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
            ('Chocolate Maska Bun', 40, True),
            ('Poha', 30, True),
            ('Samosa (1pc)', 25, True),
            ('Dalal Street Bhel', 60, True),
            ('Cheese Bhel', 70, True),
            ('A.S SPL Bhel', 80, True)
        ]
        
        # VS Fastfood menu
        vs_fastfood_menu = [
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
            ('Chocolate Sandwich (Grill)', 70.00, True),
            ('Mexican Sandwich (Reg)', 55.00, True),
            ('Mexican Sandwich (Grill)', 70.00, True),
            ('Chocolate Cheese Sandwich (Reg)', 60.00, True),
            ('Chocolate Cheese Sandwich (Grill)', 75.00, True),
            ('Three in One Sandwich (Grill)', 80.00, True),
            ('Club Sandwich (Grill)', 100.00, True),
            ('Burger Sandwich (Grill)', 110.00, True),
            ('Junglee Sandwich (Grill)', 100.00, True),
            ('Paneer Sandwich (Grill)', 100.00, True),
            ('Butter Slice (Reg)', 20.00, True),
            ('Butter Slice (Grill)', 30.00, True),
            ('Butter Jam Slice (Reg)', 25.00, True),
            ('Butter Jam Slice (Grill)', 35.00, True),
            ('Jam Sing Sev Slice (Reg)', 30.00, True),
            ('Jam Sing Sev Slice (Grill)', 40.00, True),
            ('Garlic Slice (Reg)', 25.00, True),
            ('Garlic Slice (Grill)', 35.00, True),
            ('Special Slice (Reg)', 30.00, True),
            ('Special Slice (Grill)', 40.00, True),
            ('Chocolate Slice (Reg)', 25.00, True),
            ('Chocolate Slice (Grill)', 35.00, True),
            ('Cheese Jam Slice (Grill)', 35.00, True),
            ('Cheese Slices (Grill)', 35.00, True),
            ('Chocolate Milkshake', 50.00, True),
            ('Butterscotch Milkshake', 50.00, True),
            ('Strawberry Milkshake', 50.00, True),
            ('Mango Milkshake', 50.00, True),
            ('Pineapple Milkshake', 50.00, True),
            ('Salted French Fries (Reg)', 40.00, True),
            ('Salted French Fries (Cheese)', 60.00, True),
            ('Chat Masala French Fries (Reg)', 50.00, True),
            ('Chat Masala French Fries (Cheese)', 70.00, True),
            ('Dabeli (Oil)', 20.00, True),
            ('Dabeli (Butter)', 30.00, True),
            ('Dabeli (Cheese)', 50.00, True),
            ('Vadapav (Oil)', 25.00, True),
            ('Vadapav (Butter)', 35.00, True),
            ('Vadapav (Cheese)', 55.00, True),
            ('Italian Pizza (Reg)', 70.00, True),
            ('Italian Pizza (Cheese)', 90.00, True),
            ('Jain Pizza (Reg)', 70.00, True),
            ('Jain Pizza (Cheese)', 90.00, True),
            ('Coconut Pizza (Reg)', 80.00, True),
            ('Coconut Pizza (Cheese)', 100.00, True),
            ('Margherita Pizza (Reg)', 90.00, True),
            ('Margherita Pizza (Cheese)', 110.00, True),
            ('Cheese Corn Pizza (Cheese)', 110.00, True),
            ('Paneer Pizza (Cheese)', 100.00, True),
            ('Butter Maskabun (Reg)', 30.00, True),
            ('Butter Maskabun (Cheese)', 45.00, True),
            ('Butter Jam Maskabun (Reg)', 35.00, True),
            ('Butter Jam Maskabun (Cheese)', 50.00, True),
            ('Chocolate Maskabun (Reg)', 40.00, True),
            ('Chocolate Maskabun (Cheese)', 60.00, True),
            ('Aloo Tikki Burger (Reg)', 40.00, True),
            ('Aloo Tikki Burger (Cheese)', 55.00, True),
            ('Vegetable Burger (Reg)', 50.00, True),
            ('Vegetable Burger (Cheese)', 65.00, True),
            ('Mexican Burger (Reg)', 60.00, True),
            ('Mexican Burger (Cheese)', 75.00, True),
            ('Maggi (Reg)', 25.00, True),
            ('Maggi (Masala)', 35.00, True),
            ('Maggi (Cheese)', 50.00, True),
            ('Vegetable Maggi (Reg)', 30.00, True),
            ('Vegetable Maggi (Masala)', 45.00, True),
            ('Vegetable Maggi (Cheese)', 60.00, True),
            ('Bread Pakoda', 30.00, True),
            ('Batata Vada (4 Pieces)', 30.00, True),
            ('Poha (Reg)', 25.00, True),
            ('Poha (Cheese)', 40.00, True),
            ('Samosa (1 Piece)', 15.00, True),
            ('Kulladh Tea', 15.00, True),
            ('Kulladh Coffee', 20.00, True),
            ('Thepla (4 pieces) + Dahi', 40.00, True),
            ('Kutchi Bowl (Reg)', 50.00, True),
            ('Kutchi Bowl (Cheese)', 60.00, True)
        ]
        
        # Madurai Chaat & More menu
        madurai_menu = [
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
            ('Mini Idli (10 pcs)', 70, True),
            ('Plain Dosa', 70, True),
            ('Butter Dosa', 80, True),
            ('Masala Dosa', 90, True),
            ('Butter Masala Dosa', 100, True),
            ('Mysore Masala Dosa', 110, True),
            ('Cheese Masala Dosa', 120, True),
            ('Onion Uttapam', 90, True),
            ('Tomato Uttapam', 90, True),
            ('Cheese Uttapam', 120, True),
            ('Podi Dosa', 100, True),
            ('Idli Sambar', 70, True),
            ('Vada Sambar', 70, True),
            ('Dosa Combo (Plain + Masala)', 150, True),
            ('Uttapam Combo (Onion + Tomato)', 150, True),
            ('Filter Coffee', 30, True),
            ('Masala Tea', 30, True),
            ('Lassi (Sweet)', 50, True),
            ('Lassi (Salted)', 50, True),
            ('Buttermilk', 40, True),
            ('Jal Jeera', 40, True)
        ]
        
        # Insert menu items for each outlet
        for outlet_id, menu_items in [
            (1, dawat_menu),
            (2, just_chill_menu),
            (3, tea_post_menu),
            (4, as_fastfood_menu),
            (5, vs_fastfood_menu),
            (6, madurai_menu)
        ]:
            for item_name, price, available in menu_items:
                cursor.execute("""
                    INSERT INTO menu (item_name, price, available, outlet_id)
                    VALUES (%s, %s, %s, %s)
                """, (item_name, price, available, outlet_id))
            
            conn.commit()
            logging.info(f"Added {len(menu_items)} menu items for outlet {outlet_id}")
        
        logging.info("Full menu update completed successfully")

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
    add_full_menu()
