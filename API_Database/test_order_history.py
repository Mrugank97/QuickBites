import mysql.connector
import logging
import json
import requests

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_db_connection(cims=True):
    """Get a database connection"""
    db_config_proj = {
        "host": "10.0.116.125",
        "user": "cs432g11",
        "password": "pXqJ5NYz",
        "database": "cs432g11"  # Use cs432g11 for project-specific tables
    }

    db_config_cism = {
        "host": "10.0.116.125",
        "user": "cs432g11",
        "password": "pXqJ5NYz",
        "database": "cs432cims"
    }

    try:
        if cims:
            return mysql.connector.connect(**db_config_cism)
        else:
            return mysql.connector.connect(**db_config_proj)
    except mysql.connector.Error as e:
        logging.error(f"Database connection failed: {str(e)}")
        raise

def test_order_history():
    """Test the order history API and database queries"""
    try:
        # Connect to project database
        conn = get_db_connection(False)
        cursor = conn.cursor(dictionary=True)
        
        # Get a list of member IDs with orders
        cursor.execute("SELECT DISTINCT member_id FROM orders")
        members = cursor.fetchall()
        
        if not members:
            logging.warning("No members with orders found in the database")
            return
        
        member_id = members[0]['member_id']
        logging.info(f"Testing order history for member ID: {member_id}")
        
        # Get orders directly from database
        query = """
        SELECT o.*, ot.name as outlet_name, ot.location as outlet_location
        FROM orders o
        JOIN outlet ot ON o.outlet_id = ot.outlet_id
        WHERE o.member_id = %s
        ORDER BY o.order_time DESC
        """
        cursor.execute(query, (member_id,))
        orders = cursor.fetchall()
        
        if not orders:
            logging.warning(f"No orders found for member ID {member_id}")
            return
        
        logging.info(f"Found {len(orders)} orders in database for member ID {member_id}")
        
        # Get order items for each order
        for order in orders:
            item_query = """
            SELECT oi.*, m.item_name
            FROM order_items oi
            JOIN menu m ON oi.menu_id = m.menu_id
            WHERE oi.order_id = %s
            """
            cursor.execute(item_query, (order['order_id'],))
            order['items'] = cursor.fetchall()
            
            # Get payment status from CIMS
            try:
                cims_conn = get_db_connection()  # Use CIMS database
                cims_cursor = cims_conn.cursor(dictionary=True)
                
                payment_query = """
                SELECT PaymentStatus
                FROM G11_payments
                WHERE OrderID = %s
                """
                cims_cursor.execute(payment_query, (order['order_id'],))
                payment = cims_cursor.fetchone()
                
                if payment:
                    order['payment_status'] = payment['PaymentStatus']
                else:
                    order['payment_status'] = 'Unknown'
                
                cims_cursor.close()
                cims_conn.close()
            except Exception as e:
                logging.warning(f"Error getting payment status: {str(e)}")
                order['payment_status'] = 'Unknown'
        
        # Log sample order data
        sample_order = orders[0]
        logging.info(f"Sample order from database:")
        logging.info(f"  Order ID: {sample_order['order_id']}")
        logging.info(f"  Member ID: {sample_order['member_id']}")
        logging.info(f"  Outlet ID: {sample_order['outlet_id']}")
        logging.info(f"  Outlet Name: {sample_order['outlet_name']}")
        logging.info(f"  Total Amount: {sample_order['total_amount']}")
        logging.info(f"  Order Status: {sample_order['order_status']}")
        logging.info(f"  Order Time: {sample_order['order_time']}")
        logging.info(f"  Payment Status: {sample_order.get('payment_status', 'Unknown')}")
        logging.info(f"  Items: {len(sample_order.get('items', []))}")
        
        # Now test the API
        try:
            api_url = f"http://localhost:5001/api/orders/member/{member_id}"
            
            response = requests.get(
                api_url,
                headers={"Content-Type": "application/json"}
            )
            
            logging.info(f"API response status: {response.status_code}")
            
            if response.status_code == 200:
                api_orders = response.json()
                logging.info(f"API returned {len(api_orders)} orders")
                
                # Compare database and API results
                if len(api_orders) == len(orders):
                    logging.info("API returned the same number of orders as the database query")
                else:
                    logging.warning(f"API returned {len(api_orders)} orders, but database query returned {len(orders)} orders")
                
                # Check if the first order matches
                if api_orders and orders:
                    api_order = api_orders[0]
                    db_order = orders[0]
                    
                    if api_order['order_id'] == db_order['order_id']:
                        logging.info("First order ID matches between API and database")
                    else:
                        logging.warning(f"First order ID mismatch: API={api_order['order_id']}, DB={db_order['order_id']}")
                    
                    if api_order.get('outlet_name') == db_order.get('outlet_name'):
                        logging.info("Outlet name matches between API and database")
                    else:
                        logging.warning(f"Outlet name mismatch: API={api_order.get('outlet_name')}, DB={db_order.get('outlet_name')}")
                    
                    # Log sample API order data
                    logging.info(f"Sample order from API:")
                    logging.info(f"  Order ID: {api_order.get('order_id')}")
                    logging.info(f"  Member ID: {api_order.get('member_id')}")
                    logging.info(f"  Outlet ID: {api_order.get('outlet_id')}")
                    logging.info(f"  Outlet Name: {api_order.get('outlet_name')}")
                    logging.info(f"  Total Amount: {api_order.get('total_amount')}")
                    logging.info(f"  Order Status: {api_order.get('order_status')}")
                    logging.info(f"  Order Time: {api_order.get('order_time')}")
                    logging.info(f"  Payment Status: {api_order.get('payment_status', 'Unknown')}")
                    logging.info(f"  Items: {len(api_order.get('items', []))}")
            else:
                logging.error(f"API request failed: {response.text}")
        except Exception as e:
            logging.error(f"Error testing API: {str(e)}")
        
        # Close connection
        cursor.close()
        conn.close()
        
    except Exception as e:
        logging.error(f"Error in test_order_history: {str(e)}")

if __name__ == "__main__":
    test_order_history()
