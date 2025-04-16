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

def test_order_creation():
    """Test creating an order directly in the database"""
    try:
        # Connect to project database
        conn = get_db_connection(False)
        cursor = conn.cursor()
        
        # Start a transaction
        conn.start_transaction()
        
        try:
            # Test data
            member_id = 2160  # Use a known valid member ID
            outlet_id = 1     # Use a known valid outlet ID
            total_amount = 250.00
            payment_method = 'UPI'
            
            # Insert order
            order_query = """
            INSERT INTO orders (member_id, outlet_id, total_amount, order_status, payment_method)
            VALUES (%s, %s, %s, 'Pending', %s)
            """
            cursor.execute(order_query, (member_id, outlet_id, total_amount, payment_method))
            
            # Get the order ID
            order_id = cursor.lastrowid
            logging.info(f"Created order with ID: {order_id}")
            
            # Insert order items
            items = [
                {"menu_id": 160, "quantity": 1, "subtotal": 100.00},
                {"menu_id": 161, "quantity": 1, "subtotal": 120.00},
                {"menu_id": 162, "quantity": 1, "subtotal": 70.00}
            ]
            
            item_query = """
            INSERT INTO order_items (order_id, menu_id, quantity, subtotal)
            VALUES (%s, %s, %s, %s)
            """
            for item in items:
                cursor.execute(item_query, (
                    order_id,
                    item['menu_id'],
                    item['quantity'],
                    item['subtotal']
                ))
            
            # Create payment record in CIMS database
            try:
                cims_conn = get_db_connection()  # Use CIMS database
                cims_cursor = cims_conn.cursor()
                
                payment_query = """
                INSERT INTO G11_payments (OrderID, AmountPaid, PaymentMethod, PaymentStatus, PaymentTime)
                VALUES (%s, %s, %s, 'Pending', NOW())
                """
                cims_cursor.execute(payment_query, (order_id, total_amount, payment_method))
                
                cims_conn.commit()
                cims_cursor.close()
                cims_conn.close()
                logging.info("Created payment record in CIMS database")
            except Exception as e:
                logging.warning(f"Error creating payment record: {str(e)}")
                # Continue even if payment record creation fails
            
            # Commit the transaction
            conn.commit()
            logging.info("Order created successfully via direct database access")
            
        except Exception as e:
            # Rollback in case of error
            conn.rollback()
            logging.error(f"Error creating order via direct database access: {str(e)}")
            raise e
        finally:
            cursor.close()
            conn.close()
        
        # Now test creating an order via the API
        try:
            api_url = "http://localhost:5001/api/orders"
            order_data = {
                "member_id": member_id,
                "outlet_id": outlet_id,
                "total_amount": total_amount,
                "payment_method": payment_method,
                "items": items
            }
            
            logging.info(f"Sending order data to API: {json.dumps(order_data)}")
            
            response = requests.post(
                api_url,
                json=order_data,
                headers={"Content-Type": "application/json"}
            )
            
            logging.info(f"API response status: {response.status_code}")
            logging.info(f"API response body: {response.text}")
            
            if response.status_code == 201:
                logging.info("Order created successfully via API")
            else:
                logging.error(f"Failed to create order via API: {response.text}")
        except Exception as e:
            logging.error(f"Error creating order via API: {str(e)}")
        
    except Exception as e:
        logging.error(f"Error in test_order_creation: {str(e)}")

if __name__ == "__main__":
    test_order_creation()
