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

def check_orders_structure():
    """Check the orders table structure and constraints"""
    try:
        # Connect to project database
        conn = get_db_connection(False)
        cursor = conn.cursor(dictionary=True)
        
        # Check if orders table exists
        cursor.execute("SHOW TABLES LIKE 'orders'")
        orders_exists = cursor.fetchone()
        
        if not orders_exists:
            logging.warning("orders table does not exist.")
            return
        
        logging.info("orders table exists.")
        
        # Check table structure
        cursor.execute("DESCRIBE orders")
        columns = cursor.fetchall()
        logging.info("orders table structure:")
        for column in columns:
            logging.info(f"  {column['Field']} ({column['Type']}), Null: {column['Null']}, Key: {column['Key']}, Default: {column['Default']}")
        
        # Check for foreign key constraints
        cursor.execute("""
            SELECT CONSTRAINT_NAME, COLUMN_NAME, REFERENCED_TABLE_NAME, REFERENCED_COLUMN_NAME
            FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
            WHERE TABLE_NAME = 'orders'
            AND REFERENCED_TABLE_NAME IS NOT NULL
            AND CONSTRAINT_SCHEMA = 'cs432g11'
        """)
        constraints = cursor.fetchall()
        
        if constraints:
            logging.info("Foreign key constraints on orders table:")
            for constraint in constraints:
                logging.info(f"  {constraint['CONSTRAINT_NAME']}: {constraint['COLUMN_NAME']} -> {constraint['REFERENCED_TABLE_NAME']}({constraint['REFERENCED_COLUMN_NAME']})")
        else:
            logging.warning("No foreign key constraints found on orders table.")
        
        # Check for any orders with invalid member_id or outlet_id
        cursor.execute("""
            SELECT o.order_id, o.member_id, o.outlet_id
            FROM orders o
            LEFT JOIN cs432cims.members m ON o.member_id = m.ID
            WHERE m.ID IS NULL
        """)
        invalid_member_orders = cursor.fetchall()
        
        if invalid_member_orders:
            logging.warning(f"Found {len(invalid_member_orders)} orders with invalid member_id:")
            for order in invalid_member_orders:
                logging.warning(f"  Order ID: {order['order_id']}, Member ID: {order['member_id']}")
        else:
            logging.info("All orders have valid member_id references.")
        
        cursor.execute("""
            SELECT o.order_id, o.member_id, o.outlet_id
            FROM orders o
            LEFT JOIN outlet ot ON o.outlet_id = ot.outlet_id
            WHERE ot.outlet_id IS NULL
        """)
        invalid_outlet_orders = cursor.fetchall()
        
        if invalid_outlet_orders:
            logging.warning(f"Found {len(invalid_outlet_orders)} orders with invalid outlet_id:")
            for order in invalid_outlet_orders:
                logging.warning(f"  Order ID: {order['order_id']}, Outlet ID: {order['outlet_id']}")
        else:
            logging.info("All orders have valid outlet_id references.")
        
        # Check order_items table
        cursor.execute("SHOW TABLES LIKE 'order_items'")
        order_items_exists = cursor.fetchone()
        
        if order_items_exists:
            logging.info("order_items table exists.")
            
            # Check order_items structure
            cursor.execute("DESCRIBE order_items")
            columns = cursor.fetchall()
            logging.info("order_items table structure:")
            for column in columns:
                logging.info(f"  {column['Field']} ({column['Type']}), Null: {column['Null']}, Key: {column['Key']}, Default: {column['Default']}")
            
            # Check for foreign key constraints
            cursor.execute("""
                SELECT CONSTRAINT_NAME, COLUMN_NAME, REFERENCED_TABLE_NAME, REFERENCED_COLUMN_NAME
                FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
                WHERE TABLE_NAME = 'order_items'
                AND REFERENCED_TABLE_NAME IS NOT NULL
                AND CONSTRAINT_SCHEMA = 'cs432g11'
            """)
            constraints = cursor.fetchall()
            
            if constraints:
                logging.info("Foreign key constraints on order_items table:")
                for constraint in constraints:
                    logging.info(f"  {constraint['CONSTRAINT_NAME']}: {constraint['COLUMN_NAME']} -> {constraint['REFERENCED_TABLE_NAME']}({constraint['REFERENCED_COLUMN_NAME']})")
            else:
                logging.warning("No foreign key constraints found on order_items table.")
        else:
            logging.warning("order_items table does not exist.")
        
        # Check menu table
        cursor.execute("SHOW TABLES LIKE 'menu'")
        menu_exists = cursor.fetchone()
        
        if menu_exists:
            logging.info("menu table exists.")
            
            # Check menu structure
            cursor.execute("DESCRIBE menu")
            columns = cursor.fetchall()
            logging.info("menu table structure:")
            for column in columns:
                logging.info(f"  {column['Field']} ({column['Type']}), Null: {column['Null']}, Key: {column['Key']}, Default: {column['Default']}")
            
            # Check menu data
            cursor.execute("SELECT COUNT(*) as count FROM menu")
            menu_count = cursor.fetchone()['count']
            logging.info(f"Found {menu_count} menu items.")
            
            # Check a sample of menu items
            cursor.execute("SELECT * FROM menu LIMIT 5")
            sample_menu = cursor.fetchall()
            logging.info("Sample menu items:")
            for item in sample_menu:
                logging.info(f"  ID: {item['menu_id']}, Name: {item['item_name']}, Price: {item['price']}, Outlet ID: {item['outlet_id']}")
        else:
            logging.warning("menu table does not exist.")
        
        # Close connection
        cursor.close()
        conn.close()
        
    except Exception as e:
        logging.error(f"Error checking orders structure: {str(e)}")

if __name__ == "__main__":
    check_orders_structure()
