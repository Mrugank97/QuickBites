"""
Script to add a new order to the database with current timestamp
"""
import mysql.connector
import logging
from datetime import datetime

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

def add_new_order():
    """Add a new order to the database with current timestamp"""
    conn = None
    cursor = None

    try:
        # Connect to the database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # First, check if there are any members in the CIMS database
        cursor.execute("SELECT ID, UserName FROM cs432cims.members LIMIT 5")
        members = cursor.fetchall()
        
        if not members:
            logging.warning("No members found in CIMS database")
            return
            
        # Use the first member as the customer
        member_id = members[0][0]
        member_name = members[0][1]
        logging.info(f"Using member {member_name} (ID: {member_id}) as customer")
        
        # Check if there are any outlets
        cursor.execute("SELECT outlet_id, name FROM outlet LIMIT 1")
        outlets = cursor.fetchall()
        
        if not outlets:
            logging.warning("No outlets found in database")
            return
            
        # Use the first outlet
        outlet_id = outlets[0][0]
        outlet_name = outlets[0][1]
        logging.info(f"Using outlet {outlet_name} (ID: {outlet_id})")
        
        # Check if there are any menu items for this outlet
        cursor.execute("SELECT menu_id, item_name, price FROM menu WHERE outlet_id = %s LIMIT 5", (outlet_id,))
        menu_items = cursor.fetchall()
        
        if not menu_items:
            logging.warning(f"No menu items found for outlet {outlet_name}")
            return
            
        # Calculate total amount
        total_amount = 0
        order_items = []
        
        # Add different quantities for variety
        quantities = [2, 1, 3]
        
        for i, (menu_id, item_name, price) in enumerate(menu_items[:3]):
            quantity = quantities[i % len(quantities)]
            subtotal = float(price) * quantity
            total_amount += subtotal
            order_items.append((menu_id, item_name, quantity, subtotal))
            logging.info(f"Adding item: {item_name} (₹{price} x {quantity} = ₹{subtotal})")
            
        # Get current timestamp
        current_time = datetime.now()
        
        # Insert the order with current timestamp
        cursor.execute("""
            INSERT INTO orders (member_id, outlet_id, total_amount, order_status, order_time)
            VALUES (%s, %s, %s, %s, %s)
        """, (member_id, outlet_id, total_amount, 'Pending', current_time))
        
        # Get the order ID
        order_id = cursor.lastrowid
        logging.info(f"Created order with ID: {order_id}")
        
        # Insert the order items
        for menu_id, item_name, quantity, subtotal in order_items:
            cursor.execute("""
                INSERT INTO order_items (order_id, menu_id, quantity, subtotal)
                VALUES (%s, %s, %s, %s)
            """, (order_id, menu_id, quantity, subtotal))
            logging.info(f"Added order item: {item_name} (x{quantity})")
            
        # Commit the transaction
        conn.commit()
        logging.info(f"New order created successfully with total amount: ₹{total_amount}")
        logging.info(f"Order timestamp: {current_time}")

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
    add_new_order()
