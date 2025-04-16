"""
Script to create the required tables for QuickBites in the cs432g11 database
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

        # Create roles table if it doesn't exist
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS roles (
                id INT AUTO_INCREMENT PRIMARY KEY,
                role_name VARCHAR(50) NOT NULL,
                UNIQUE KEY (role_name)
            )
        """)
        logging.info("roles table created successfully")

        # Insert default roles
        cursor.execute("""
            INSERT IGNORE INTO roles (id, role_name) VALUES
            (1, 'admin'),
            (2, 'user')
        """)
        logging.info("Default roles inserted successfully")

        # Create change_logs table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS change_logs (
                log_id INT AUTO_INCREMENT PRIMARY KEY,
                user_id VARCHAR(50) NOT NULL,
                operation VARCHAR(50) NOT NULL,
                table_name VARCHAR(100) NOT NULL,
                details TEXT,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        logging.info("change_logs table created successfully")

        # Create member_portfolio table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS member_portfolio (
                portfolio_id INT AUTO_INCREMENT PRIMARY KEY,
                member_id INT NOT NULL,
                bio TEXT,
                skills TEXT,
                achievements TEXT,
                last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                UNIQUE KEY (member_id)
            )
        """)
        logging.info("member_portfolio table created successfully")

        # Create user_roles_mapping table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_roles_mapping (
                mapping_id INT AUTO_INCREMENT PRIMARY KEY,
                member_id INT NOT NULL,
                role_id INT NOT NULL,
                UNIQUE KEY (member_id, role_id),
                FOREIGN KEY (role_id) REFERENCES roles(id)
            )
        """)
        logging.info("user_roles_mapping table created successfully")

        # Create orders table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS orders (
                order_id INT AUTO_INCREMENT PRIMARY KEY,
                member_id INT NOT NULL,
                order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                total_amount DECIMAL(10,2) NOT NULL,
                status ENUM('Pending', 'Completed', 'Cancelled') DEFAULT 'Pending'
            )
        """)
        logging.info("orders table created successfully")

        # Create order_items table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS order_items (
                item_id INT AUTO_INCREMENT PRIMARY KEY,
                order_id INT NOT NULL,
                product_name VARCHAR(255) NOT NULL,
                quantity INT NOT NULL,
                price DECIMAL(10,2) NOT NULL,
                FOREIGN KEY (order_id) REFERENCES orders(order_id)
            )
        """)
        logging.info("order_items table created successfully")

        # Create menu table for food items
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS menu (
                menu_id INT AUTO_INCREMENT PRIMARY KEY,
                item_name VARCHAR(100) NOT NULL,
                description TEXT,
                price DECIMAL(10,2) NOT NULL,
                category VARCHAR(50),
                image_url VARCHAR(255),
                is_available BOOLEAN DEFAULT TRUE
            )
        """)
        logging.info("menu table created successfully")

        # Create feedback table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS feedback (
                feedback_id INT AUTO_INCREMENT PRIMARY KEY,
                member_id INT NOT NULL,
                outlet_id INT NOT NULL,
                order_id INT,
                rating INT NOT NULL CHECK (rating BETWEEN 1 AND 5),
                comments TEXT,
                feedback_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        logging.info("feedback table created successfully")

        # Create a view to show member information with their portfolios
        cursor.execute("""
            CREATE OR REPLACE VIEW member_profiles AS
            SELECT
                m.ID as member_id,
                m.UserName as username,
                m.emailID as email,
                m.DoB as date_of_birth,
                l.Role as role,
                mp.bio,
                mp.skills,
                mp.achievements,
                mp.last_updated
            FROM
                cs432cims.members m
            LEFT JOIN
                cs432cims.Login l ON m.ID = l.MemberID
            LEFT JOIN
                member_portfolio mp ON m.ID = mp.member_id
        """)
        logging.info("member_profiles view created successfully")

        # Create a view to show members in Group 11
        cursor.execute("""
            CREATE OR REPLACE VIEW group11_members AS
            SELECT
                m.ID as member_id,
                m.UserName as username,
                m.emailID as email,
                l.Role as role
            FROM
                cs432cims.members m
            JOIN
                cs432cims.MemberGroupMapping mgm ON m.ID = mgm.MemberID
            JOIN
                cs432cims.Login l ON m.ID = l.MemberID
            WHERE
                mgm.GroupID = 11
        """)
        logging.info("group11_members view created successfully")

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
