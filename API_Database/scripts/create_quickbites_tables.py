"""
Script to create the QuickBites tables in the cs432g11 database
This implements Task 4: Database Table Creation
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

def create_tables():
    """Create the required tables for QuickBites in the cs432g11 database"""
    conn = None
    cursor = None

    try:
        # Connect to the database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Drop existing tables if they exist (for clean setup)
        cursor.execute("DROP TABLE IF EXISTS payments")
        cursor.execute("DROP TABLE IF EXISTS feedback")
        cursor.execute("DROP TABLE IF EXISTS order_items")
        cursor.execute("DROP TABLE IF EXISTS orders")
        cursor.execute("DROP TABLE IF EXISTS menu")
        cursor.execute("DROP TABLE IF EXISTS outlet_manager")
        cursor.execute("DROP TABLE IF EXISTS admin")
        cursor.execute("DROP TABLE IF EXISTS student")
        cursor.execute("DROP TABLE IF EXISTS outlet")

        # Create Outlet Table
        cursor.execute("""
            CREATE TABLE outlet (
                outlet_id INT PRIMARY KEY AUTO_INCREMENT,
                name VARCHAR(100) NOT NULL,
                location VARCHAR(255) NOT NULL
            )
        """)
        logging.info("outlet table created successfully")

        # Create Student Table (references CIMS members table)
        cursor.execute("""
            CREATE TABLE student (
                member_id INT PRIMARY KEY,
                roll_number VARCHAR(20) UNIQUE NOT NULL,
                hostel_name VARCHAR(100) NOT NULL,
                department VARCHAR(100) NOT NULL
            )
        """)
        logging.info("student table created successfully")

        # Create Admin Table (references CIMS members table)
        cursor.execute("""
            CREATE TABLE admin (
                member_id INT PRIMARY KEY,
                access_level ENUM('SuperAdmin', 'Moderator') NOT NULL,
                date_of_joining DATE NOT NULL
            )
        """)
        logging.info("admin table created successfully")

        # Create Outlet Manager Table (references CIMS members table)
        cursor.execute("""
            CREATE TABLE outlet_manager (
                member_id INT PRIMARY KEY,
                assigned_outlet_id INT UNIQUE,
                FOREIGN KEY (assigned_outlet_id) REFERENCES outlet(outlet_id) ON DELETE SET NULL
            )
        """)
        logging.info("outlet_manager table created successfully")

        # Create Menu Table
        cursor.execute("""
            CREATE TABLE menu (
                menu_id INT PRIMARY KEY AUTO_INCREMENT,
                item_name VARCHAR(100) NOT NULL,
                price DECIMAL(10,2) NOT NULL,
                available BOOLEAN DEFAULT TRUE,
                outlet_id INT NOT NULL,
                FOREIGN KEY (outlet_id) REFERENCES outlet(outlet_id) ON DELETE CASCADE
            )
        """)
        logging.info("menu table created successfully")

        # Create Orders Table
        cursor.execute("""
            CREATE TABLE orders (
                order_id INT PRIMARY KEY AUTO_INCREMENT,
                member_id INT NOT NULL,
                outlet_id INT NOT NULL,
                total_amount DECIMAL(10,2) NOT NULL,
                order_status ENUM('Pending', 'Completed', 'Cancelled') DEFAULT 'Pending',
                order_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (member_id) REFERENCES student(member_id) ON DELETE CASCADE,
                FOREIGN KEY (outlet_id) REFERENCES outlet(outlet_id) ON DELETE CASCADE
            )
        """)
        logging.info("orders table created successfully")

        # Create Order Items Table
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
        logging.info("order_items table created successfully")

        # Create Feedback Table
        cursor.execute("""
            CREATE TABLE feedback (
                feedback_id INT PRIMARY KEY AUTO_INCREMENT,
                member_id INT NOT NULL,
                menu_id INT NOT NULL,
                rating INT NOT NULL CHECK (rating BETWEEN 1 AND 5),
                comments TEXT,
                feedback_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (member_id) REFERENCES student(member_id) ON DELETE CASCADE,
                FOREIGN KEY (menu_id) REFERENCES menu(menu_id) ON DELETE CASCADE
            )
        """)
        logging.info("feedback table created successfully")

        # Create Payments Table
        cursor.execute("""
            CREATE TABLE payments (
                payment_id INT PRIMARY KEY AUTO_INCREMENT,
                order_id INT NOT NULL,
                amount_paid DECIMAL(10,2) NOT NULL,
                payment_method ENUM('UPI', 'Card', 'Cash') NOT NULL,
                payment_status ENUM('Pending', 'Completed', 'Failed') DEFAULT 'Pending',
                payment_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE
            )
        """)
        logging.info("payments table created successfully")

        # Create a view to show member information with their roles
        cursor.execute("""
            CREATE OR REPLACE VIEW member_roles AS
            SELECT
                m.ID as member_id,
                m.UserName as name,
                m.emailID as email,
                CASE
                    WHEN s.member_id IS NOT NULL THEN 'Student'
                    WHEN om.member_id IS NOT NULL THEN 'OutletManager'
                    WHEN a.member_id IS NOT NULL THEN 'Admin'
                    ELSE 'Unknown'
                END as role
            FROM
                cs432cims.members m
            LEFT JOIN
                student s ON m.ID = s.member_id
            LEFT JOIN
                outlet_manager om ON m.ID = om.member_id
            LEFT JOIN
                admin a ON m.ID = a.member_id
        """)
        logging.info("member_roles view created successfully")

        # Create a view to show menu items with outlet information
        cursor.execute("""
            CREATE OR REPLACE VIEW menu_with_outlet AS
            SELECT
                m.menu_id,
                m.item_name,
                m.price,
                m.available,
                o.outlet_id,
                o.name as outlet_name,
                o.location as outlet_location
            FROM
                menu m
            JOIN
                outlet o ON m.outlet_id = o.outlet_id
        """)
        logging.info("menu_with_outlet view created successfully")

        # Create a view to show orders with customer and outlet information
        cursor.execute("""
            CREATE OR REPLACE VIEW order_details AS
            SELECT
                o.order_id,
                o.member_id,
                m.UserName as customer_name,
                o.outlet_id,
                ot.name as outlet_name,
                o.total_amount,
                o.order_status,
                o.order_time
            FROM
                orders o
            JOIN
                cs432cims.members m ON o.member_id = m.ID
            JOIN
                outlet ot ON o.outlet_id = ot.outlet_id
        """)
        logging.info("order_details view created successfully")

        # Insert sample outlets
        cursor.execute("""
            INSERT INTO outlet (name, location) VALUES
            ('Dawat', 'H-Hostel, Ground Floor'),
            ('Just Chill', 'B-Hostel, Ground Floor'),
            ('Tea Post', 'E-Hostel, Ground Floor'),
            ('AS FastFood', 'I-Hostel, Ground Floor'),
            ('VS Fastfood', 'H-Hostel, Ground Floor'),
            ('Madurai Chaat & More', 'Near Sports Complex')
        """)
        logging.info("Sample outlets inserted successfully")

        # Commit the changes
        conn.commit()
        logging.info("All tables created successfully")

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
    create_tables()
