"""
Script to check the structure of order_items table
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

def check_order_items():
    """Check the structure of order_items table"""
    conn = None
    cursor = None
    
    try:
        # Connect to the database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        
        # Check if order_items table exists
        cursor.execute("""
            SELECT COUNT(*) as count FROM information_schema.tables
            WHERE table_schema = 'cs432g11' AND table_name = 'order_items'
        """)
        result = cursor.fetchone()
        
        if result and result['count'] > 0:
            logging.info("order_items table exists")
            
            # Check the structure of the order_items table
            cursor.execute("DESCRIBE order_items")
            columns = cursor.fetchall()
            logging.info(f"order_items table has {len(columns)} columns:")
            for column in columns:
                logging.info(f"  {column['Field']}: {column['Type']}")
            
            # Check if there are any records in the order_items table
            cursor.execute("SELECT COUNT(*) as count FROM order_items")
            result = cursor.fetchone()
            logging.info(f"order_items table has {result['count']} records")
            
            # Get a sample of order_items
            cursor.execute("SELECT * FROM order_items LIMIT 5")
            order_items = cursor.fetchall()
            logging.info("Sample order_items:")
            for item in order_items:
                logging.info(f"  {item}")
                
            # Get a sample of orders with their items
            logging.info("Sample orders with items:")
            cursor.execute("""
                SELECT o.order_id, o.member_id, o.outlet_id, o.total_amount, o.order_status, o.order_time,
                       oi.item_id, oi.menu_id, oi.quantity, oi.item_price,
                       m.item_name
                FROM orders o
                JOIN order_items oi ON o.order_id = oi.order_id
                JOIN menu m ON oi.menu_id = m.menu_id
                ORDER BY o.order_id
                LIMIT 10
            """)
            order_details = cursor.fetchall()
            
            current_order_id = None
            for detail in order_details:
                if current_order_id != detail['order_id']:
                    current_order_id = detail['order_id']
                    logging.info(f"Order #{detail['order_id']} - Status: {detail['order_status']} - Total: {detail['total_amount']}")
                
                logging.info(f"  Item: {detail['item_name']} - Quantity: {detail['quantity']} - Price: {detail['item_price']}")
        else:
            logging.warning("order_items table does not exist")
        
    except mysql.connector.Error as e:
        logging.error(f"Database error: {str(e)}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    check_order_items()
