"""
Script to test the orders API endpoint directly
"""
import requests
import json
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def test_orders_api():
    """Test the orders API endpoint directly"""
    try:
        # Test for member ID 2160 (from the check_orders.py output)
        member_id = 2160
        url = f"http://localhost:5001/api/orders/member/{member_id}"
        logging.info(f"Testing orders API for member {member_id}: {url}")
        
        # Make the request without authentication (for testing)
        response = requests.get(url)
        
        logging.info(f"Response status code: {response.status_code}")
        
        if response.status_code == 200:
            orders = response.json()
            logging.info(f"Found {len(orders)} orders for member {member_id}")
            
            if orders:
                for order in orders[:2]:  # Show first 2 orders
                    logging.info(f"Order #{order.get('order_id')}: {order.get('outlet_name')} - ₹{order.get('total_amount')}")
                    
                    if 'items' in order:
                        for item in order['items'][:3]:  # Show first 3 items
                            logging.info(f"  - {item.get('item_name')} x {item.get('quantity')} = ₹{item.get('subtotal')}")
            else:
                logging.warning(f"No orders found for member {member_id}")
        else:
            logging.error(f"API request failed: {response.text}")
    
    except Exception as e:
        logging.error(f"Error testing orders API: {str(e)}")

if __name__ == "__main__":
    test_orders_api()
