"""
Script to check the structure of order_items table (fixed query)
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
        
        # Get a sample of orders with their items
        logging.info("Sample orders with items:")
        cursor.execute("""
            SELECT o.order_id, o.member_id, o.outlet_id, o.total_amount, o.order_status, o.order_time,
                   oi.order_item_id, oi.menu_id, oi.quantity, oi.subtotal,
                   m.item_name, m.price
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
            
            logging.info(f"  Item: {detail['item_name']} - Quantity: {detail['quantity']} - Subtotal: {detail['subtotal']}")
        
    except mysql.connector.Error as e:
        logging.error(f"Database error: {str(e)}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    check_order_items()
