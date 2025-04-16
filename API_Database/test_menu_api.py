"""
Script to test the menu API endpoint directly
"""
import requests
import json
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def test_menu_api():
    """Test the menu API endpoint directly"""
    try:
        # Test for each outlet
        for outlet_id in range(1, 7):  # Outlets 1-6
            url = f"http://localhost:5001/api/menu/outlet/{outlet_id}"
            logging.info(f"Testing menu API for outlet {outlet_id}: {url}")
            
            # Make the request without authentication (the API allows this for debugging)
            response = requests.get(url)
            
            logging.info(f"Response status code: {response.status_code}")
            
            if response.status_code == 200:
                menu_items = response.json()
                logging.info(f"Found {len(menu_items)} menu items for outlet {outlet_id}")
                
                if menu_items:
                    for item in menu_items[:3]:  # Show first 3 items
                        logging.info(f"  - {item.get('item_name')} (₹{item.get('price')})")
                else:
                    logging.warning(f"No menu items found for outlet {outlet_id}")
            else:
                logging.error(f"API request failed: {response.text}")
    
    except Exception as e:
        logging.error(f"Error testing menu API: {str(e)}")

if __name__ == "__main__":
    test_menu_api()
