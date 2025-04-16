"""
Script to test placing an order directly
"""
import requests
import json
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def test_place_order():
    """Test placing an order directly"""
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
            quantity = 1
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
        
        if order_response.ok:
            result = order_response.json()
            logging.info(f"Order placed successfully: {result}")
            logging.info(f"Order ID: {result.get('order_id')}")
            logging.info(f"Payment ID: {result.get('payment_id')}")
        else:
            logging.error(f"Failed to place order: {order_response.status_code}")
            logging.error(f"Response: {order_response.text}")
            
            # Try to parse the error response
            try:
                error_data = order_response.json()
                logging.error(f"Error details: {error_data}")
            except:
                logging.error("Could not parse error response")
    
    except Exception as e:
        logging.error(f"Error testing place order: {str(e)}")

if __name__ == "__main__":
    test_place_order()
