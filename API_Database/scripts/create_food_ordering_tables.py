"""
Script to create and check the necessary tables for the food ordering system
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

db_config_cims = {
    "host": "10.0.116.125",
    "user": "cs432g11",
    "password": "pXqJ5NYz",
    "database": "cs432cims"
}

def create_food_ordering_tables():
    """Create the necessary tables for the food ordering system"""
    conn = None
    cims_conn = None
    
    try:
        # Connect to the database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        
        # Connect to CIMS database
        cims_conn = mysql.connector.connect(**db_config_cims)
        cims_cursor = cims_conn.cursor()
        
        # Create roles table if it doesn't exist
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS roles (
            id INT AUTO_INCREMENT PRIMARY KEY,
            role_name VARCHAR(50) NOT NULL,
            description VARCHAR(255)
        )
        """)
        print("Roles table created or already exists")
        
        # Check if roles exist, if not insert default roles
        cursor.execute("SELECT COUNT(*) FROM roles")
        role_count = cursor.fetchone()[0]
        
        if role_count == 0:
            cursor.execute("""
            INSERT INTO roles (role_name, description) VALUES
            ('Admin', 'System administrator with full access'),
            ('Student', 'Student user who can place orders'),
            ('OutletManager', 'Manager of a food outlet')
            """)
            conn.commit()
            print("Default roles inserted")
        
        # Create user_roles_mapping table if it doesn't exist
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_roles_mapping (
            mapping_id INT AUTO_INCREMENT PRIMARY KEY,
            member_id INT NOT NULL,
            role_id INT NOT NULL,
            FOREIGN KEY (role_id) REFERENCES roles(id)
        )
        """)
        print("User roles mapping table created or already exists")
        
        # Create student table if it doesn't exist
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS student (
            student_id INT AUTO_INCREMENT PRIMARY KEY,
            member_id INT NOT NULL,
            roll_number VARCHAR(20),
            hostel_name VARCHAR(50),
            department VARCHAR(100)
        )
        """)
        print("Student table created or already exists")
        
        # Create outlet table if it doesn't exist
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS outlet (
            outlet_id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            location VARCHAR(255),
            description TEXT,
            opening_time TIME,
            closing_time TIME,
            is_active BOOLEAN DEFAULT TRUE
        )
        """)
        print("Outlet table created or already exists")
        
        # Create outlet_manager table if it doesn't exist
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS outlet_manager (
            manager_id INT AUTO_INCREMENT PRIMARY KEY,
            member_id INT NOT NULL,
            assigned_outlet_id INT,
            FOREIGN KEY (assigned_outlet_id) REFERENCES outlet(outlet_id)
        )
        """)
        print("Outlet manager table created or already exists")
        
        # Create menu table if it doesn't exist
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS menu (
            menu_id INT AUTO_INCREMENT PRIMARY KEY,
            outlet_id INT NOT NULL,
            item_name VARCHAR(100) NOT NULL,
            price DECIMAL(10, 2) NOT NULL,
            description TEXT,
            category VARCHAR(50),
            available BOOLEAN DEFAULT TRUE,
            FOREIGN KEY (outlet_id) REFERENCES outlet(outlet_id)
        )
        """)
        print("Menu table created or already exists")
        
        # Create orders table if it doesn't exist
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            order_id INT AUTO_INCREMENT PRIMARY KEY,
            member_id INT NOT NULL,
            outlet_id INT NOT NULL,
            total_amount DECIMAL(10, 2) NOT NULL,
            order_status ENUM('Pending', 'Completed', 'Cancelled') DEFAULT 'Pending',
            order_time DATETIME NOT NULL,
            FOREIGN KEY (outlet_id) REFERENCES outlet(outlet_id)
        )
        """)
        print("Orders table created or already exists")
        
        # Create order_items table if it doesn't exist
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS order_items (
            item_id INT AUTO_INCREMENT PRIMARY KEY,
            order_id INT NOT NULL,
            menu_id INT NOT NULL,
            quantity INT NOT NULL,
            subtotal DECIMAL(10, 2) NOT NULL,
            FOREIGN KEY (order_id) REFERENCES orders(order_id),
            FOREIGN KEY (menu_id) REFERENCES menu(menu_id)
        )
        """)
        print("Order items table created or already exists")
        
        # Create feedback table if it doesn't exist
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS feedback (
            feedback_id INT AUTO_INCREMENT PRIMARY KEY,
            order_id INT NOT NULL,
            rating INT NOT NULL,
            comments TEXT,
            feedback_time DATETIME NOT NULL,
            FOREIGN KEY (order_id) REFERENCES orders(order_id)
        )
        """)
        print("Feedback table created or already exists")
        
        # Create G11_payments table in CIMS if it doesn't exist
        cims_cursor.execute("""
        CREATE TABLE IF NOT EXISTS G11_payments (
            PaymentID INT AUTO_INCREMENT PRIMARY KEY,
            OrderID INT NOT NULL,
            AmountPaid DECIMAL(10, 2) NOT NULL,
            PaymentMethod VARCHAR(50) DEFAULT 'UPI',
            PaymentStatus ENUM('Pending', 'Completed', 'Failed') DEFAULT 'Pending',
            PaymentTime DATETIME NOT NULL
        )
        """)
        print("G11_payments table created or already exists in CIMS database")
        
        # Check if there are any outlets
        cursor.execute("SELECT COUNT(*) FROM outlet")
        outlet_count = cursor.fetchone()[0]
        
        if outlet_count == 0:
            # Insert sample outlets
            cursor.execute("""
            INSERT INTO outlet (name, location, description, opening_time, closing_time) VALUES
            ('Dawat', 'H-Hostel, Ground Floor', 'Indian cuisine restaurant', '08:00:00', '22:00:00'),
            ('Just Chill', 'B-Hostel, Ground Floor', 'Ice cream and beverages', '10:00:00', '23:00:00'),
            ('Tea Post', 'E-Hostel, Ground Floor', 'Tea and snacks', '07:00:00', '23:00:00'),
            ('Madurai Chaat & More', 'Near Sports Complex', 'South Indian snacks and chaat', '09:00:00', '21:00:00'),
            ('AS FastFood', 'I-Hostel, Ground Floor', 'Fast food and burgers', '11:00:00', '23:00:00'),
            ('VS Fastfood', 'H-Hostel, Ground Floor', 'Chinese and Indo-Chinese cuisine', '11:00:00', '22:30:00')
            """)
            conn.commit()
            print("Sample outlets inserted")
        
        # Check if there are any menu items
        cursor.execute("SELECT COUNT(*) FROM menu")
        menu_count = cursor.fetchone()[0]
        
        if menu_count == 0:
            # Insert sample menu items for each outlet
            # Menu items for Dawat (outlet_id = 1)
            cursor.execute("""
            INSERT INTO menu (item_name, price, description, category, available, outlet_id) VALUES
            ('Veg Biryani', 120.00, 'Fragrant basmati rice cooked with mixed vegetables and aromatic spices', 'Veg', TRUE, 1),
            ('Chicken Biryani', 180.00, 'Fragrant basmati rice cooked with tender chicken pieces and aromatic spices', 'Non-Veg', TRUE, 1),
            ('Paneer Butter Masala', 150.00, 'Cottage cheese cubes in a rich and creamy tomato gravy', 'Veg', TRUE, 1),
            ('Butter Naan', 30.00, 'Soft and fluffy Indian bread brushed with butter', 'Veg', TRUE, 1),
            ('Jeera Rice', 80.00, 'Basmati rice flavored with cumin seeds', 'Veg', TRUE, 1)
            """)
            
            # Menu items for Just Chill (outlet_id = 2)
            cursor.execute("""
            INSERT INTO menu (item_name, price, description, category, available, outlet_id) VALUES
            ('Cold Coffee', 60.00, 'Chilled coffee with ice cream', 'Beverage', TRUE, 2),
            ('Chocolate Shake', 80.00, 'Thick chocolate milkshake with ice cream', 'Beverage', TRUE, 2),
            ('Vanilla Ice Cream', 50.00, 'Classic vanilla ice cream scoop', 'Dessert', TRUE, 2),
            ('Mango Shake', 70.00, 'Fresh mango milkshake', 'Beverage', TRUE, 2),
            ('Oreo Shake', 90.00, 'Milkshake with crushed Oreo cookies', 'Beverage', TRUE, 2)
            """)
            
            # Menu items for Tea Post (outlet_id = 3)
            cursor.execute("""
            INSERT INTO menu (item_name, price, description, category, available, outlet_id) VALUES
            ('Masala Chai', 20.00, 'Traditional Indian tea with milk and aromatic spices', 'Beverage', TRUE, 3),
            ('Lemon Tea', 25.00, 'Refreshing tea with lemon', 'Beverage', TRUE, 3),
            ('Green Tea', 30.00, 'Healthy green tea', 'Beverage', TRUE, 3),
            ('Biscuits', 10.00, 'Assorted biscuits', 'Snack', TRUE, 3),
            ('Samosa', 15.00, 'Crispy pastry filled with spiced potatoes', 'Snack', TRUE, 3)
            """)
            
            # Menu items for Madurai Chaat & More (outlet_id = 4)
            cursor.execute("""
            INSERT INTO menu (item_name, price, description, category, available, outlet_id) VALUES
            ('Pani Puri', 40.00, 'Hollow crisp fried puri filled with spicy water', 'Snack', TRUE, 4),
            ('Bhel Puri', 50.00, 'Puffed rice, vegetables and tangy tamarind sauce', 'Snack', TRUE, 4),
            ('Dahi Puri', 60.00, 'Crispy puris filled with potatoes, yogurt and chutneys', 'Snack', TRUE, 4),
            ('Sev Puri', 45.00, 'Crispy puris topped with potatoes, onions and chutneys', 'Snack', TRUE, 4),
            ('Masala Dosa', 80.00, 'Crispy rice crepe filled with spiced potato filling', 'Veg', TRUE, 4)
            """)
            
            # Menu items for AS FastFood (outlet_id = 5)
            cursor.execute("""
            INSERT INTO menu (item_name, price, description, category, available, outlet_id) VALUES
            ('Veg Burger', 70.00, 'Vegetable patty with lettuce, tomato and sauce', 'Veg', TRUE, 5),
            ('Chicken Burger', 90.00, 'Chicken patty with lettuce, tomato and sauce', 'Non-Veg', TRUE, 5),
            ('French Fries', 50.00, 'Crispy fried potato strips', 'Veg', TRUE, 5),
            ('Veg Sandwich', 60.00, 'Sandwich with vegetables and cheese', 'Veg', TRUE, 5),
            ('Chicken Sandwich', 80.00, 'Sandwich with chicken and vegetables', 'Non-Veg', TRUE, 5)
            """)
            
            # Menu items for VS Fastfood (outlet_id = 6)
            cursor.execute("""
            INSERT INTO menu (item_name, price, description, category, available, outlet_id) VALUES
            ('Veg Manchurian', 100.00, 'Vegetable balls in a spicy sauce', 'Veg', TRUE, 6),
            ('Hakka Noodles', 90.00, 'Stir-fried noodles with vegetables', 'Veg', TRUE, 6),
            ('Fried Rice', 80.00, 'Stir-fried rice with vegetables', 'Veg', TRUE, 6),
            ('Chilli Paneer', 120.00, 'Cottage cheese in spicy sauce', 'Veg', TRUE, 6),
            ('Spring Rolls', 60.00, 'Crispy rolls filled with vegetables', 'Veg', TRUE, 6)
            """)
            
            conn.commit()
            print("Sample menu items inserted")
        
        print("\nAll tables created and sample data inserted successfully!")
        
    except mysql.connector.Error as e:
        logging.error(f"Database error: {str(e)}")
    finally:
        if conn:
            conn.close()
        if cims_conn:
            cims_conn.close()

if __name__ == "__main__":
    create_food_ordering_tables()
