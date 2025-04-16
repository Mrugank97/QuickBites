"""
Script to test the orders API endpoint with authentication
"""
import requests
import json
import logging
import sys

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def login_and_test_orders():
    """Login and test the orders API endpoint"""
    try:
        # Login first to get a token
        login_url = "http://localhost:5001/login"
        login_data = {
            "username": "test",  # Replace with a valid username
            "password": "test",  # Replace with a valid password
            "group": "11"
        }
        
        # Try to login with provided credentials
        logging.info(f"Attempting to login with username: {login_data['username']}")
        login_response = requests.post(login_url, json=login_data)
        
        if login_response.status_code != 200:
            logging.error(f"Login failed: {login_response.text}")
            logging.info("Proceeding without authentication...")
            token = None
            member_id = 2160  # Use the member ID we know has orders
        else:
            login_data = login_response.json()
            token = login_data.get('token')
            member_id = login_data.get('ID') or login_data.get('member_id')
            logging.info(f"Login successful. Member ID: {member_id}, Token: {token[:10]}...")
        
        # Now test the orders API
        orders_url = f"http://localhost:5001/api/orders/member/{member_id}"
        logging.info(f"Testing orders API for member {member_id}: {orders_url}")
        
        headers = {'Content-Type': 'application/json'}
        if token:
            headers['Authorization'] = f"Bearer {token}"
        
        orders_response = requests.get(orders_url, headers=headers)
        
        logging.info(f"Response status code: {orders_response.status_code}")
        
        if orders_response.status_code == 200:
            orders = orders_response.json()
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
            logging.error(f"API request failed: {orders_response.text}")
    
    except Exception as e:
        logging.error(f"Error testing orders API: {str(e)}")

if __name__ == "__main__":
    login_and_test_orders()
