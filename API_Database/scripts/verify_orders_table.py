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

def check_orders_table():
    """Check the orders table structure and data"""
    try:
        # Connect to project database
        conn = get_db_connection(False)
        cursor = conn.cursor(dictionary=True)
        
        # Check orders table structure
        cursor.execute("DESCRIBE orders")
        columns = cursor.fetchall()
        
        logging.info("orders table structure:")
        for column in columns:
            logging.info(f"  {column['Field']} ({column['Type']}), Null: {column['Null']}, Key: {column['Key']}, Default: {column['Default']}")
        
        # Check if payment_method column exists
        payment_method_exists = any(column['Field'] == 'payment_method' for column in columns)
        if payment_method_exists:
            logging.info("payment_method column exists in orders table")
        else:
            logging.warning("payment_method column does not exist in orders table")
        
        # Check orders data
        cursor.execute("SELECT * FROM orders LIMIT 5")
        orders = cursor.fetchall()
        
        logging.info(f"Sample orders data (first 5 rows):")
        for order in orders:
            order_info = f"  Order ID: {order['order_id']}, Member ID: {order['member_id']}, Outlet ID: {order['outlet_id']}, Total: {order['total_amount']}, Status: {order['order_status']}"
            if payment_method_exists and 'payment_method' in order:
                order_info += f", Payment Method: {order['payment_method']}"
            logging.info(order_info)
        
        # Close connection
        cursor.close()
        conn.close()
        
    except Exception as e:
        logging.error(f"Error checking orders table: {str(e)}")

if __name__ == "__main__":
    check_orders_table()
