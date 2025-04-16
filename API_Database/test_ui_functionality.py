import requests
import json
import logging
import time
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("ui_test_results.log"),
        logging.StreamHandler()
    ]
)

# API base URL
API_BASE_URL = "http://localhost:5001"

# Test credentials
TEST_CREDENTIALS = {
    "student": {
        "username": "student1",
        "password": "password123",
        "role": "student"
    },
    "manager": {
        "username": "piyush",
        "password": "piyush",
        "role": "OutletManager"
    },
    "admin": {
        "username": "admin1",
        "password": "password123",
        "role": "admin"
    }
}

# Store session tokens
session_tokens = {}

def login(role):
    """Login with the specified role and return the session token"""
    logging.info(f"Logging in as {role}...")

    try:
        response = requests.post(
            f"{API_BASE_URL}/login",
            json=TEST_CREDENTIALS[role]
        )

        if response.status_code == 200:
            data = response.json()
            token = data.get("token")
            logging.info(f"Login successful for {role}")
            return token
        else:
            logging.error(f"Login failed for {role}: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        logging.error(f"Error during login: {str(e)}")
        return None

def test_get_outlets():
    """Test getting all outlets"""
    logging.info("Testing get outlets API...")

    try:
        headers = {}
        if "student" in session_tokens:
            headers["Authorization"] = f"Bearer {session_tokens['student']}"

        response = requests.get(
            f"{API_BASE_URL}/api/outlets",
            headers=headers
        )

        if response.status_code == 200:
            outlets = response.json()
            logging.info(f"Successfully retrieved {len(outlets)} outlets")
            return outlets
        else:
            logging.error(f"Failed to get outlets: {response.status_code} - {response.text}")
            return []
    except Exception as e:
        logging.error(f"Error getting outlets: {str(e)}")
        return []

def test_get_menu_for_outlet(outlet_id):
    """Test getting menu items for an outlet"""
    logging.info(f"Testing get menu API for outlet {outlet_id}...")

    try:
        headers = {}
        if "student" in session_tokens:
            headers["Authorization"] = f"Bearer {session_tokens['student']}"

        response = requests.get(
            f"{API_BASE_URL}/api/menu/outlet/{outlet_id}",
            headers=headers
        )

        if response.status_code == 200:
            menu_items = response.json()
            logging.info(f"Successfully retrieved {len(menu_items)} menu items for outlet {outlet_id}")
            return menu_items
        else:
            logging.error(f"Failed to get menu for outlet {outlet_id}: {response.status_code} - {response.text}")
            return []
    except Exception as e:
        logging.error(f"Error getting menu for outlet {outlet_id}: {str(e)}")
        return []

def test_place_order(outlet_id, menu_items):
    """Test placing an order"""
    if not menu_items or len(menu_items) == 0:
        logging.error(f"No menu items available for outlet {outlet_id}, cannot place order")
        return False

    logging.info(f"Testing place order API for outlet {outlet_id}...")

    try:
        # Select 2 random items from the menu
        selected_items = menu_items[:2] if len(menu_items) >= 2 else menu_items

        # Prepare order data
        order_items = []
        total_amount = 0

        for item in selected_items:
            quantity = 1
            subtotal = float(item["price"]) * quantity
            total_amount += subtotal

            order_items.append({
                "menu_id": item["menu_id"],
                "quantity": quantity,
                "subtotal": subtotal
            })

        order_data = {
            "member_id": 2160,  # Default test member ID
            "outlet_id": outlet_id,
            "total_amount": total_amount,
            "payment_method": "UPI",
            "items": order_items
        }

        headers = {}
        if "student" in session_tokens:
            headers["Authorization"] = f"Bearer {session_tokens['student']}"
            headers["Content-Type"] = "application/json"

        response = requests.post(
            f"{API_BASE_URL}/api/orders",
            headers=headers,
            json=order_data
        )

        if response.status_code == 201:
            order_result = response.json()
            logging.info(f"Successfully placed order: {order_result}")
            return order_result.get("order_id")
        else:
            logging.error(f"Failed to place order: {response.status_code} - {response.text}")
            return False
    except Exception as e:
        logging.error(f"Error placing order: {str(e)}")
        return False

def test_get_orders_for_student():
    """Test getting orders for a student"""
    logging.info("Testing get orders API for student...")

    try:
        headers = {}
        if "student" in session_tokens:
            headers["Authorization"] = f"Bearer {session_tokens['student']}"

        response = requests.get(
            f"{API_BASE_URL}/api/orders/member/2160",  # Default test member ID
            headers=headers
        )

        if response.status_code == 200:
            orders = response.json()
            logging.info(f"Successfully retrieved {len(orders)} orders for student")
            return orders
        else:
            logging.error(f"Failed to get orders for student: {response.status_code} - {response.text}")
            return []
    except Exception as e:
        logging.error(f"Error getting orders for student: {str(e)}")
        return []

def test_get_outlet_for_manager():
    """Test getting outlet for a manager"""
    logging.info("Testing get outlet API for manager...")

    try:
        headers = {}
        if "manager" in session_tokens:
            headers["Authorization"] = f"Bearer {session_tokens['manager']}"

        response = requests.get(
            f"{API_BASE_URL}/api/manager/assigned-outlet",
            headers=headers
        )

        if response.status_code == 200:
            outlet = response.json()
            logging.info(f"Successfully retrieved outlet for manager: {outlet}")
            return outlet
        elif response.status_code == 404 and "No outlet assigned" in response.text:
            logging.error(f"CRITICAL ERROR: Outlet manager is not assigned to any outlet")
            logging.error(f"Response: {response.text}")
            return None
        else:
            logging.error(f"Failed to get outlet for manager: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        logging.error(f"Error getting outlet for manager: {str(e)}")
        return None

def test_get_orders_for_outlet(outlet_id):
    """Test getting orders for an outlet"""
    logging.info(f"Testing get orders API for outlet {outlet_id}...")

    try:
        headers = {}
        if "manager" in session_tokens:
            headers["Authorization"] = f"Bearer {session_tokens['manager']}"

        response = requests.get(
            f"{API_BASE_URL}/api/orders/outlet/{outlet_id}",
            headers=headers
        )

        if response.status_code == 200:
            orders = response.json()
            logging.info(f"Successfully retrieved {len(orders)} orders for outlet {outlet_id}")
            return orders
        elif response.status_code == 403 and "You are not assigned to any outlet" in response.text:
            logging.error(f"CRITICAL ERROR: Outlet manager is not assigned to outlet {outlet_id}")
            logging.error(f"Response: {response.text}")
            return []
        else:
            logging.error(f"Failed to get orders for outlet {outlet_id}: {response.status_code} - {response.text}")
            return []
    except Exception as e:
        logging.error(f"Error getting orders for outlet {outlet_id}: {str(e)}")
        return []

def test_update_order_status(order_id, status):
    """Test updating order status"""
    logging.info(f"Testing update order status API for order {order_id} to {status}...")

    try:
        headers = {}
        if "manager" in session_tokens:
            headers["Authorization"] = f"Bearer {session_tokens['manager']}"
            headers["Content-Type"] = "application/json"

        response = requests.put(
            f"{API_BASE_URL}/api/orders/{order_id}/status",
            headers=headers,
            json={"status": status}
        )

        if response.status_code == 200:
            result = response.json()
            logging.info(f"Successfully updated order {order_id} status to {status}")
            return True
        else:
            logging.error(f"Failed to update order status: {response.status_code} - {response.text}")
            return False
    except Exception as e:
        logging.error(f"Error updating order status: {str(e)}")
        return False

def test_create_menu_item(outlet_id):
    """Test creating a menu item"""
    logging.info(f"Testing create menu item API for outlet {outlet_id}...")

    try:
        # Generate a unique item name
        timestamp = int(time.time())
        item_name = f"Test Item {timestamp}"

        menu_data = {
            "outlet_id": outlet_id,
            "item_name": item_name,
            "price": 99.99,
            "available": True
        }

        headers = {}
        if "manager" in session_tokens:
            headers["Authorization"] = f"Bearer {session_tokens['manager']}"
            headers["Content-Type"] = "application/json"

        response = requests.post(
            f"{API_BASE_URL}/api/menu",
            headers=headers,
            json=menu_data
        )

        if response.status_code == 201:
            result = response.json()
            logging.info(f"Successfully created menu item: {result}")
            return result.get("menu_id")
        else:
            logging.error(f"Failed to create menu item: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        logging.error(f"Error creating menu item: {str(e)}")
        return None

def test_update_menu_item(menu_id):
    """Test updating a menu item"""
    logging.info(f"Testing update menu item API for menu item {menu_id}...")

    try:
        # Generate a unique item name
        timestamp = int(time.time())
        item_name = f"Updated Test Item {timestamp}"

        menu_data = {
            "item_name": item_name,
            "price": 149.99,
            "available": True
        }

        headers = {}
        if "manager" in session_tokens:
            headers["Authorization"] = f"Bearer {session_tokens['manager']}"
            headers["Content-Type"] = "application/json"

        response = requests.put(
            f"{API_BASE_URL}/api/menu/{menu_id}",
            headers=headers,
            json=menu_data
        )

        if response.status_code == 200:
            result = response.json()
            logging.info(f"Successfully updated menu item {menu_id}")
            return True
        else:
            logging.error(f"Failed to update menu item: {response.status_code} - {response.text}")
            return False
    except Exception as e:
        logging.error(f"Error updating menu item: {str(e)}")
        return False

def test_delete_menu_item(menu_id):
    """Test deleting a menu item"""
    logging.info(f"Testing delete menu item API for menu item {menu_id}...")

    try:
        headers = {}
        if "manager" in session_tokens:
            headers["Authorization"] = f"Bearer {session_tokens['manager']}"

        response = requests.delete(
            f"{API_BASE_URL}/api/menu/{menu_id}",
            headers=headers
        )

        if response.status_code == 200:
            result = response.json()
            logging.info(f"Successfully deleted menu item {menu_id}")
            return True
        else:
            logging.error(f"Failed to delete menu item: {response.status_code} - {response.text}")
            return False
    except Exception as e:
        logging.error(f"Error deleting menu item: {str(e)}")
        return False

def run_tests():
    """Run all tests"""
    logging.info("Starting UI functionality tests...")

    # Login with different roles
    for role in TEST_CREDENTIALS.keys():
        token = login(role)
        if token:
            session_tokens[role] = token

    # Test student functionality
    outlets = test_get_outlets()

    if outlets:
        for outlet in outlets[:2]:  # Test first 2 outlets
            outlet_id = outlet["outlet_id"]
            menu_items = test_get_menu_for_outlet(outlet_id)

            if menu_items:
                order_id = test_place_order(outlet_id, menu_items)
                if order_id:
                    logging.info(f"Successfully placed order {order_id} for outlet {outlet_id}")

    student_orders = test_get_orders_for_student()

    # Test manager functionality
    manager_outlet = test_get_outlet_for_manager()

    if manager_outlet:
        outlet_id = manager_outlet["outlet_id"]
        outlet_orders = test_get_orders_for_outlet(outlet_id)

        # Test menu management
        menu_id = test_create_menu_item(outlet_id)
        if menu_id:
            test_update_menu_item(menu_id)
            test_delete_menu_item(menu_id)

        # Test order management
        if outlet_orders and len(outlet_orders) > 0:
            order_id = outlet_orders[0]["order_id"]
            test_update_order_status(order_id, "Completed")

    logging.info("UI functionality tests completed!")

if __name__ == "__main__":
    run_tests()
