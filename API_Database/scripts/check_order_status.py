"""
Script to check the status of orders in the database
"""
import mysql.connector
import logging
import sys

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

def check_order_status(order_id=None):
    """Check the status of an order in the database"""
    conn = None
    cursor = None

    try:
        # Connect to the database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)

        if order_id:
            # Check a specific order
            cursor.execute("""
                SELECT o.*, ot.name as outlet_name
                FROM orders o
                JOIN outlet ot ON o.outlet_id = ot.outlet_id
                WHERE o.order_id = %s
            """, (order_id,))
            order = cursor.fetchone()
            
            if order:
                logging.info(f"Order #{order['order_id']}: {order['outlet_name']} - ₹{order['total_amount']} - {order['order_status']}")
                
                # Get order items
                cursor.execute("""
                    SELECT oi.*, m.item_name
                    FROM order_items oi
                    JOIN menu m ON oi.menu_id = m.menu_id
                    WHERE oi.order_id = %s
                """, (order['order_id'],))
                items = cursor.fetchall()
                
                for item in items:
                    logging.info(f"  - {item['item_name']} x {item['quantity']} = ₹{item['subtotal']}")
            else:
                logging.warning(f"Order #{order_id} not found")
        else:
            # Check all orders
            cursor.execute("""
                SELECT o.*, ot.name as outlet_name
                FROM orders o
                JOIN outlet ot ON o.outlet_id = ot.outlet_id
                ORDER BY o.order_time DESC
            """)
            orders = cursor.fetchall()
            
            logging.info(f"Found {len(orders)} orders in the database")
            
            for order in orders:
                logging.info(f"Order #{order['order_id']}: {order['outlet_name']} - ₹{order['total_amount']} - {order['order_status']}")

    except mysql.connector.Error as e:
        logging.error(f"Database error: {str(e)}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    # If an order ID is provided as a command-line argument, check that specific order
    if len(sys.argv) > 1:
        try:
            order_id = int(sys.argv[1])
            check_order_status(order_id)
        except ValueError:
            logging.error("Invalid order ID. Please provide a valid integer.")
    else:
        # Otherwise, check all orders
        check_order_status()
