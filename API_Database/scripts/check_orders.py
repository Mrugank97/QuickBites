"""
Script to check orders in the database
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

def check_orders():
    """Check orders in the database"""
    conn = None
    cursor = None

    try:
        # Connect to the database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)

        # Check if orders table exists
        cursor.execute("""
            SELECT COUNT(*) as count FROM information_schema.tables
            WHERE table_schema = 'cs432g11' AND table_name = 'orders'
        """)
        result = cursor.fetchone()
        if result and result['count'] > 0:
            logging.info("orders table exists")
        else:
            logging.warning("orders table does not exist")
            return

        # Check if there are any orders
        cursor.execute("SELECT COUNT(*) as count FROM orders")
        count = cursor.fetchone()['count']
        logging.info(f"Found {count} orders in the database")

        if count > 0:
            # Get all orders
            cursor.execute("""
                SELECT o.*, ot.name as outlet_name
                FROM orders o
                JOIN outlet ot ON o.outlet_id = ot.outlet_id
                ORDER BY o.order_time DESC
            """)
            orders = cursor.fetchall()
            
            for order in orders:
                logging.info(f"Order #{order['order_id']}: Member {order['member_id']} - {order['outlet_name']} - ₹{order['total_amount']} - {order['order_status']}")
                
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

    except mysql.connector.Error as e:
        logging.error(f"Database error: {str(e)}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    check_orders()
