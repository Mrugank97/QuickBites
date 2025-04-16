import mysql.connector
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_db_connection(cims=True):
    """Get a database connection"""
    db_config_proj = {
        "host": "10.0.116.125",
        "user": "cs432g11",
        "password": "pXqJ5NYz",
        "database": "cs432g11"  # Use cs432g11 for project-specific tables
    }

    db_config_cism = {
        "host": "10.0.116.125",
        "user": "cs432g11",
        "password": "pXqJ5NYz",
        "database": "cs432cims"
    }

    try:
        if cims:
            return mysql.connector.connect(**db_config_cism)
        else:
            return mysql.connector.connect(**db_config_proj)
    except mysql.connector.Error as e:
        logging.error(f"Database connection failed: {str(e)}")
        raise

def fix_outlet_data():
    """Check and fix outlet data"""
    try:
        # Connect to project database
        conn = get_db_connection(False)
        cursor = conn.cursor(dictionary=True)
        
        # Check if outlet table exists
        cursor.execute("SHOW TABLES LIKE 'outlet'")
        outlet_exists = cursor.fetchone()
        
        if not outlet_exists:
            logging.warning("outlet table does not exist. Creating it...")
            
            # Create outlet table
            cursor.execute("""
                CREATE TABLE outlet (
                    outlet_id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    location VARCHAR(255) NOT NULL,
                    description TEXT,
                    opening_time TIME,
                    closing_time TIME,
                    is_active BOOLEAN DEFAULT TRUE
                )
            """)
            conn.commit()
            logging.info("outlet table created successfully.")
        
        # Check if there are any outlets in the table
        cursor.execute("SELECT COUNT(*) as count FROM outlet")
        outlet_count = cursor.fetchone()['count']
        
        if outlet_count == 0:
            logging.warning("No outlets found in the table. Adding default outlets...")
            
            # Add default outlets
            outlets = [
                (1, "Dawat", "H-Hostel, Ground Floor", "Indian cuisine restaurant", "08:00:00", "22:00:00", True),
                (2, "Just Chill", "H-Hostel, Ground Floor", "Fast food and beverages", "08:00:00", "22:00:00", True),
                (3, "Tea Post", "Academic Area", "Tea and snacks", "08:00:00", "20:00:00", True),
                (4, "AS FastFood", "Academic Area", "Fast food outlet", "08:00:00", "22:00:00", True),
                (5, "VS Fastfood", "V-Hostel, Ground Floor", "Fast food and meals", "08:00:00", "22:00:00", True),
                (6, "Madurai Chaat & More", "Academic Area", "South Indian snacks and chaat", "08:00:00", "20:00:00", True)
            ]
            
            for outlet in outlets:
                cursor.execute("""
                    INSERT INTO outlet (outlet_id, name, location, description, opening_time, closing_time, is_active)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """, outlet)
            
            conn.commit()
            logging.info("Default outlets added successfully.")
        
        # Check if there are any orders with invalid outlet_id
        cursor.execute("""
            SELECT o.order_id, o.outlet_id
            FROM orders o
            LEFT JOIN outlet ot ON o.outlet_id = ot.outlet_id
            WHERE ot.outlet_id IS NULL
        """)
        invalid_orders = cursor.fetchall()
        
        if invalid_orders:
            logging.warning(f"Found {len(invalid_orders)} orders with invalid outlet_id. Fixing them...")
            
            # Fix orders with invalid outlet_id
            for order in invalid_orders:
                # Assign a default outlet (Dawat - ID 1)
                cursor.execute("""
                    UPDATE orders
                    SET outlet_id = 1
                    WHERE order_id = %s
                """, (order['order_id'],))
            
            conn.commit()
            logging.info("Fixed orders with invalid outlet_id.")
        
        # Verify the outlet data
        cursor.execute("SELECT * FROM outlet")
        outlets = cursor.fetchall()
        logging.info(f"Verified {len(outlets)} outlets in the database:")
        for outlet in outlets:
            logging.info(f"  ID: {outlet['outlet_id']}, Name: {outlet['name']}, Location: {outlet['location']}")
        
        # Close connection
        cursor.close()
        conn.close()
        
        logging.info("Outlet data check and fix completed.")
        
    except Exception as e:
        logging.error(f"Error fixing outlet data: {str(e)}")

if __name__ == "__main__":
    fix_outlet_data()
