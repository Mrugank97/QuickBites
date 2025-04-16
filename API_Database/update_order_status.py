"""
Script to update the status of an order in the database
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

def update_order_status(order_id, new_status):
    """Update the status of an order in the database"""
    conn = None
    cursor = None

    try:
        # Connect to the database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Check if the order exists
        cursor.execute("SELECT order_id, order_status FROM orders WHERE order_id = %s", (order_id,))
        order = cursor.fetchone()
        
        if not order:
            logging.warning(f"Order #{order_id} not found")
            return
            
        current_status = order[1]
        logging.info(f"Current status of order #{order_id}: {current_status}")
        
        # Validate the new status
        if new_status not in ['Pending', 'Completed', 'Cancelled']:
            logging.error(f"Invalid status: {new_status}. Must be one of: Pending, Completed, Cancelled")
            return
            
        # Update the order status
        cursor.execute("UPDATE orders SET order_status = %s WHERE order_id = %s", (new_status, order_id))
        conn.commit()
        
        logging.info(f"Updated status of order #{order_id} from {current_status} to {new_status}")

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
    # Check command-line arguments
    if len(sys.argv) < 3:
        logging.error("Usage: python update_order_status.py <order_id> <new_status>")
        sys.exit(1)
        
    try:
        order_id = int(sys.argv[1])
        new_status = sys.argv[2]
        update_order_status(order_id, new_status)
    except ValueError:
        logging.error("Invalid order ID. Please provide a valid integer.")
