"""
Script to test getting orders from the API
"""
import requests
import json
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def test_get_orders():
    """Test getting orders from the API"""
    try:
        # Base URL
        base_url = "http://localhost:5001"
        
        # Member ID to test
        member_id = 2160  # Use the member ID we know exists
        
        # Get orders for this member
        orders_url = f"{base_url}/api/orders/member/{member_id}"
        logging.info(f"Getting orders from: {orders_url}")
        
        # Add cache-busting parameter
        timestamp = int(requests.get("http://worldtimeapi.org/api/ip").json()["unixtime"])
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
        
        if not orders:
            logging.warning(f"No orders found for member {member_id}")
            return
            
        # Print details of each order
        for order in orders:
            logging.info(f"Order #{order.get('order_id')}: {order.get('outlet_name')} - ₹{order.get('total_amount')} - {order.get('order_status')}")
            
            # Check if order has items
            if 'items' in order and order['items']:
                for item in order['items']:
                    logging.info(f"  - {item.get('item_name')} x {item.get('quantity')} = ₹{item.get('subtotal')}")
            else:
                logging.warning(f"  No items found for order #{order.get('order_id')}")
    
    except Exception as e:
        logging.error(f"Error testing get orders: {str(e)}")

if __name__ == "__main__":
    test_get_orders()
