import mysql.connector
import logging
from session_validator import log_database_change

class DatabaseManager:
    def __init__(self, logging):
        self.logging = logging
        self.cims_config = {
            "host": "10.0.116.125",
            "user": "cs432g11",
            "password": "pXqJ5NYz",
            "database": "cs432cims"
        }
        # Use the cs432g11 database for project-specific tables
        self.project_config = {
            "host": "10.0.116.125",
            "user": "cs432g11",
            "password": "pXqJ5NYz",
            "database": "cs432g11"  # Use cs432g11 for project-specific tables
        }
        self.logging.info("Database configurations initialized")

    def get_cims_connection(self):
        """Get a connection to the centralized CIMS database"""
        try:
            return mysql.connector.connect(**self.cims_config)
        except mysql.connector.Error as e:
            self.logging.error(f"CIMS database connection failed: {str(e)}")
            raise

    def get_project_connection(self):
        """Get a connection to the project-specific database"""
        try:
            return mysql.connector.connect(**self.project_config)
        except mysql.connector.Error as e:
            self.logging.error(f"Project database connection failed: {str(e)}")
            raise

    def execute_cims_query(self, query, params=None, commit=False, user_id=None, operation=None, table=None, details=None):
        """Execute a query on the CIMS database with optional logging"""
        conn = None
        cursor = None
        try:
            self.logging.info(f"Executing CIMS query: {query}")
            if params:
                self.logging.info(f"Query parameters: {params}")

            conn = self.get_cims_connection()
            cursor = conn.cursor(dictionary=True)

            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)

            result = None
            if query.strip().upper().startswith("SELECT"):
                result = cursor.fetchall()
                self.logging.info(f"Query result: {result}")

            if commit:
                conn.commit()
                self.logging.info("Changes committed to database")

                # Log the database change if requested
                if user_id and operation and table:
                    log_database_change(conn, self.logging, operation, table, user_id, details or "")

            return result
        except mysql.connector.Error as e:
            self.logging.error(f"CIMS database query failed: {str(e)}")
            if conn:
                conn.rollback()
            raise
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def execute_project_query(self, query, params=None, commit=False, user_id=None, operation=None, table=None, details=None):
        """Execute a query on the project-specific database with optional logging"""
        conn = None
        cursor = None
        try:
            conn = self.get_project_connection()
            cursor = conn.cursor(dictionary=True)

            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)

            result = None
            if query.strip().upper().startswith("SELECT"):
                result = cursor.fetchall()

            if commit:
                conn.commit()

                # Log the database change if requested
                if user_id and operation and table:
                    log_database_change(conn, self.logging, operation, table, user_id, details or "")

            return result
        except mysql.connector.Error as e:
            self.logging.error(f"Project database query failed: {str(e)}")
            if conn:
                conn.rollback()
            raise
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def check_member_exists(self, member_id):
        """Check if a member exists in the CIMS database"""
        result = self.execute_cims_query(
            "SELECT ID FROM members WHERE ID = %s",
            (member_id,)
        )
        return len(result) > 0

    def check_member_in_group(self, member_id, group_id):
        """Check if a member is associated with a specific group"""
        result = self.execute_cims_query(
            "SELECT * FROM MemberGroupMapping WHERE MemberID = %s AND GroupID = %s",
            (member_id, group_id)
        )
        return len(result) > 0

    def get_member_groups(self, member_id):
        """Get all groups a member is associated with"""
        return self.execute_cims_query(
            "SELECT GroupID FROM MemberGroupMapping WHERE MemberID = %s",
            (member_id,)
        )

    def create_change_logs_table(self):
        """Create the change_logs table if it doesn't exist"""
        self.logging.info("Creating change_logs table")
        try:
            self.execute_project_query("""
                CREATE TABLE IF NOT EXISTS change_logs (
                    log_id INT AUTO_INCREMENT PRIMARY KEY,
                    user_id VARCHAR(50) NOT NULL,
                    operation VARCHAR(50) NOT NULL,
                    table_name VARCHAR(100) NOT NULL,
                    details TEXT,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """, commit=True)
            self.logging.info("change_logs table created successfully")
        except Exception as e:
            self.logging.error(f"Error creating change_logs table: {str(e)}")

    def create_member_portfolio_table(self):
        """Create the member_portfolio table if it doesn't exist"""
        self.logging.info("Creating member_portfolio table")
        try:
            self.execute_project_query("""
                CREATE TABLE IF NOT EXISTS member_portfolio (
                    portfolio_id INT AUTO_INCREMENT PRIMARY KEY,
                    member_id INT NOT NULL,
                    bio TEXT,
                    skills TEXT,
                    achievements TEXT,
                    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                    UNIQUE KEY (member_id)
                )
            """, commit=True)
            self.logging.info("member_portfolio table created successfully")
        except Exception as e:
            self.logging.error(f"Error creating member_portfolio table: {str(e)}")

    def create_project_tables(self):
        """Create all required project-specific tables"""
        self.logging.info("Creating project-specific tables")
        try:
            # Create change logs table
            self.create_change_logs_table()

            # Create member portfolio table
            self.create_member_portfolio_table()

            # Create roles table if not exists
            self.execute_project_query("""
                CREATE TABLE IF NOT EXISTS roles (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    role_name VARCHAR(50) NOT NULL,
                    UNIQUE KEY (role_name)
                )
            """, commit=True)
            self.logging.info("roles table created successfully")

            # Insert default roles
            self.execute_project_query("""
                INSERT IGNORE INTO roles (id, role_name) VALUES
                (1, 'admin'),
                (2, 'user')
            """, commit=True)
            self.logging.info("Default roles inserted successfully")

            # Create user_roles_mapping table
            self.execute_project_query("""
                CREATE TABLE IF NOT EXISTS user_roles_mapping (
                    mapping_id INT AUTO_INCREMENT PRIMARY KEY,
                    member_id INT NOT NULL,
                    role_id INT NOT NULL,
                    UNIQUE KEY (member_id, role_id),
                    FOREIGN KEY (role_id) REFERENCES roles(id)
                )
            """, commit=True)
            self.logging.info("user_roles_mapping table created successfully")

            # Create orders table
            self.execute_project_query("""
                CREATE TABLE IF NOT EXISTS orders (
                    order_id INT AUTO_INCREMENT PRIMARY KEY,
                    member_id INT NOT NULL,
                    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    total_amount DECIMAL(10,2) NOT NULL,
                    status ENUM('Pending', 'Completed', 'Cancelled') DEFAULT 'Pending'
                )
            """, commit=True)
            self.logging.info("orders table created successfully")

            # Create order_items table
            self.execute_project_query("""
                CREATE TABLE IF NOT EXISTS order_items (
                    item_id INT AUTO_INCREMENT PRIMARY KEY,
                    order_id INT NOT NULL,
                    product_name VARCHAR(255) NOT NULL,
                    quantity INT NOT NULL,
                    price DECIMAL(10,2) NOT NULL,
                    FOREIGN KEY (order_id) REFERENCES orders(order_id)
                )
            """, commit=True)
            self.logging.info("order_items table created successfully")

            # Create menu table
            self.execute_project_query("""
                CREATE TABLE IF NOT EXISTS menu (
                    menu_id INT AUTO_INCREMENT PRIMARY KEY,
                    item_name VARCHAR(100) NOT NULL,
                    description TEXT,
                    price DECIMAL(10,2) NOT NULL,
                    category VARCHAR(50),
                    image_url VARCHAR(255),
                    is_available BOOLEAN DEFAULT TRUE
                )
            """, commit=True)
            self.logging.info("menu table created successfully")

            # Create feedback table
            self.execute_project_query("""
                CREATE TABLE IF NOT EXISTS feedback (
                    feedback_id INT AUTO_INCREMENT PRIMARY KEY,
                    member_id INT NOT NULL,
                    order_id INT,
                    rating INT NOT NULL CHECK (rating BETWEEN 1 AND 5),
                    comments TEXT,
                    feedback_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (order_id) REFERENCES orders(order_id)
                )
            """, commit=True)
            self.logging.info("feedback table created successfully")

            # Create views
            self.create_project_views()

            self.logging.info("All project-specific tables created successfully")
        except Exception as e:
            self.logging.error(f"Error creating project tables: {str(e)}")

    def create_project_views(self):
        """Create views for the project"""
        try:
            # Create a view to show member information with their portfolios
            self.execute_project_query("""
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
            """, commit=True)
            self.logging.info("member_profiles view created successfully")

            # Create a view to show members in Group 11
            self.execute_project_query("""
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
            """, commit=True)
            self.logging.info("group11_members view created successfully")
        except Exception as e:
            self.logging.error(f"Error creating project views: {str(e)}")
