"""
Script to create the necessary tables for Group 11 in the cs432cims database
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
    "database": "cs432cims"
}

def create_tables():
    """Create the necessary tables for Group 11"""
    conn = None
    cursor = None
    
    try:
        # Connect to the database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        
        # Create G11_member_portfolio table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS G11_member_portfolio (
                portfolio_id INT AUTO_INCREMENT PRIMARY KEY,
                member_id INT NOT NULL,
                bio TEXT,
                skills TEXT,
                achievements TEXT,
                last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                UNIQUE KEY (member_id)
            )
        """)
        logging.info("G11_member_portfolio table created successfully")
        
        # Create G11_change_logs table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS G11_change_logs (
                log_id INT AUTO_INCREMENT PRIMARY KEY,
                user_id VARCHAR(50) NOT NULL,
                operation VARCHAR(50) NOT NULL,
                table_name VARCHAR(100) NOT NULL,
                details TEXT,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        logging.info("G11_change_logs table created successfully")
        
        # Create G11_roles table if it doesn't exist
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS G11_roles (
                id INT AUTO_INCREMENT PRIMARY KEY,
                role_name VARCHAR(50) NOT NULL,
                UNIQUE KEY (role_name)
            )
        """)
        logging.info("G11_roles table created successfully")
        
        # Insert default roles
        cursor.execute("""
            INSERT IGNORE INTO G11_roles (id, role_name) VALUES 
            (1, 'admin'),
            (2, 'user')
        """)
        logging.info("Default roles inserted successfully")
        
        # Create G11_user_roles_mapping table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS G11_user_roles_mapping (
                mapping_id INT AUTO_INCREMENT PRIMARY KEY,
                member_id INT NOT NULL,
                role_id INT NOT NULL,
                UNIQUE KEY (member_id, role_id)
            )
        """)
        logging.info("G11_user_roles_mapping table created successfully")
        
        # Create G11_orders table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS G11_orders (
                order_id INT AUTO_INCREMENT PRIMARY KEY,
                member_id INT NOT NULL,
                order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                total_amount DECIMAL(10,2) NOT NULL,
                status VARCHAR(20) DEFAULT 'Pending'
            )
        """)
        logging.info("G11_orders table created successfully")
        
        # Create G11_order_items table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS G11_order_items (
                item_id INT AUTO_INCREMENT PRIMARY KEY,
                order_id INT NOT NULL,
                product_name VARCHAR(255) NOT NULL,
                quantity INT NOT NULL,
                price DECIMAL(10,2) NOT NULL
            )
        """)
        logging.info("G11_order_items table created successfully")
        
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
