"""
Script to test placing an order and checking if it appears in the order history
"""
import requests
import json
import logging
import time

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def test_place_and_check_order():
    """Test placing an order and checking if it appears in the order history"""
    try:
        # Base URL
        base_url = "http://localhost:5001"
        
        # First, get a list of outlets
        outlets_url = f"{base_url}/api/outlets"
        logging.info(f"Getting outlets from: {outlets_url}")
        
        outlets_response = requests.get(outlets_url)
        if not outlets_response.ok:
            logging.error(f"Failed to get outlets: {outlets_response.text}")
            return
            
        outlets = outlets_response.json()
        if not outlets:
            logging.error("No outlets found")
            return
            
        # Use the first outlet
        outlet = outlets[0]
        logging.info(f"Using outlet: {outlet['name']} (ID: {outlet['outlet_id']})")
        
        # Get menu items for this outlet
        menu_url = f"{base_url}/api/menu/outlet/{outlet['outlet_id']}"
        logging.info(f"Getting menu from: {menu_url}")
        
        menu_response = requests.get(menu_url)
        if not menu_response.ok:
            logging.error(f"Failed to get menu: {menu_response.text}")
            return
            
        menu_items = menu_response.json()
        if not menu_items:
            logging.error("No menu items found")
            return
            
        # Use the first 2 menu items
        selected_items = menu_items[:2]
        logging.info(f"Selected {len(selected_items)} menu items")
        
        # Create order items
        order_items = []
        total_amount = 0
        
        for item in selected_items:
            quantity = 2  # Order 2 of each item
            subtotal = float(item['price']) * quantity
            total_amount += subtotal
            
            order_items.append({
                "menu_id": item['menu_id'],
                "quantity": quantity,
                "subtotal": subtotal
            })
            
            logging.info(f"Added item: {item['item_name']} (₹{item['price']} x {quantity} = ₹{subtotal})")
        
        # Create order data
        member_id = 2160  # Use the member ID we know exists
        order_data = {
            "member_id": member_id,
            "outlet_id": outlet['outlet_id'],
            "total_amount": total_amount,
            "payment_method": "UPI",
            "items": order_items
        }
        
        logging.info(f"Order data: {json.dumps(order_data, indent=2)}")
        
        # Place the order
        order_url = f"{base_url}/api/orders"
        logging.info(f"Placing order at: {order_url}")
        
        order_response = requests.post(
            order_url,
            json=order_data,
            headers={"Content-Type": "application/json"}
        )
        
        if not order_response.ok:
            logging.error(f"Failed to place order: {order_response.status_code}")
            logging.error(f"Response: {order_response.text}")
            return
            
        result = order_response.json()
        logging.info(f"Order placed successfully: {result}")
        order_id = result.get('order_id')
        logging.info(f"Order ID: {order_id}")
        
        # Wait a moment for the order to be processed
        logging.info("Waiting 2 seconds for the order to be processed...")
        time.sleep(2)
        
        # Now check if the order appears in the order history
        orders_url = f"{base_url}/api/orders/member/{member_id}"
        logging.info(f"Checking order history at: {orders_url}")
        
        # Add cache-busting parameter
        timestamp = int(time.time())
        orders_url = f"{orders_url}?_={timestamp}"
        
        # Add headers to prevent caching
        headers = {
            "Cache-Control": "no-cache, no-store, must-revalidate",
            "Pragma": "no-cache",
            "Expires": "0"
        }
        
        orders_response = requests.get(orders_url, headers=headers)
        if not orders_response.ok:
            logging.error(f"Failed to get orders: {orders_response.text}")
            return
            
        orders = orders_response.json()
        logging.info(f"Found {len(orders)} orders for member {member_id}")
        
        # Check if our new order is in the list
        new_order = next((order for order in orders if order.get('order_id') == order_id), None)
        
        if new_order:
            logging.info(f"Found our new order in the order history: Order #{new_order.get('order_id')}")
            logging.info(f"Order status: {new_order.get('order_status')}")
            logging.info(f"Order total: ₹{new_order.get('total_amount')}")
            
            # Check if order has items
            if 'items' in new_order and new_order['items']:
                logging.info(f"Order has {len(new_order['items'])} items:")
                for item in new_order['items']:
                    logging.info(f"  - {item.get('item_name')} x {item.get('quantity')} = ₹{item.get('subtotal')}")
            else:
                logging.warning(f"  No items found for order #{new_order.get('order_id')}")
        else:
            logging.error(f"Could not find our new order (ID: {order_id}) in the order history")
    
    except Exception as e:
        logging.error(f"Error testing place and check order: {str(e)}")

if __name__ == "__main__":
    test_place_and_check_order()
