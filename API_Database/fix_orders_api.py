"""
Script to fix the orders API by updating the main.py file
"""
import re
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def fix_orders_api():
    """Fix the orders API in main.py"""
    try:
        # Read the main.py file
        with open('main.py', 'r') as file:
            content = file.read()

        # Fix the get_orders_by_member function
        # The issue is that we're trying to join with cs432cims.G11_payments but that table might not exist
        # or the join might be failing
        old_query = """
        SELECT o.*, ot.name as outlet_name, ot.location as outlet_location,
               p.PaymentID as payment_id, p.PaymentStatus as payment_status, p.PaymentMethod as payment_method
        FROM orders o
        JOIN outlet ot ON o.outlet_id = ot.outlet_id
        LEFT JOIN cs432cims.G11_payments p ON o.order_id = p.OrderID
        WHERE o.member_id = %s
        ORDER BY o.order_time DESC
        """

        new_query = """
        SELECT o.*, ot.name as outlet_name, ot.location as outlet_location
        FROM orders o
        JOIN outlet ot ON o.outlet_id = ot.outlet_id
        WHERE o.member_id = %s
        ORDER BY o.order_time DESC
        """

        # Replace the query
        content = content.replace(old_query, new_query)

        # Fix the serialization of Decimal objects in the get_orders_by_member function
        # Find the get_orders_by_member function
        get_orders_pattern = r'@app\.route\(\'/api/orders/member/<int:member_id>\', methods=\[\'GET\'\]\)\n@require_valid_session\ndef get_orders_by_member\(member_id, user_id=None, \*\*kwargs\):.*?return jsonify\(orders\), 200'
        get_orders_match = re.search(get_orders_pattern, content, re.DOTALL)
        
        if get_orders_match:
            old_function = get_orders_match.group(0)
            
            # Add code to convert Decimal objects to float
            new_function = old_function.replace(
                'return jsonify(orders), 200',
                '''
        # Convert Decimal objects to float for JSON serialization
        serializable_orders = []
        for order in orders:
            serializable_order = {}
            for key, value in order.items():
                if isinstance(value, (int, float, str, bool, type(None))):
                    serializable_order[key] = value
                elif str(type(value)) == "<class 'decimal.Decimal'>":
                    serializable_order[key] = float(value)
                elif key == 'items' and isinstance(value, list):
                    serializable_items = []
                    for item in value:
                        serializable_item = {}
                        for item_key, item_value in item.items():
                            if isinstance(item_value, (int, float, str, bool, type(None))):
                                serializable_item[item_key] = item_value
                            elif str(type(item_value)) == "<class 'decimal.Decimal'>":
                                serializable_item[item_key] = float(item_value)
                            else:
                                serializable_item[item_key] = str(item_value)
                        serializable_items.append(serializable_item)
                    serializable_order[key] = serializable_items
                else:
                    serializable_order[key] = str(value)
            serializable_orders.append(serializable_order)

        return jsonify(serializable_orders), 200'''
            )
            
            content = content.replace(old_function, new_function)
            
            logging.info("Updated get_orders_by_member function")
        else:
            logging.warning("Could not find get_orders_by_member function")

        # Write the updated content back to main.py
        with open('main.py', 'w') as file:
            file.write(content)
            
        logging.info("Successfully updated main.py")
        
    except Exception as e:
        logging.error(f"Error fixing orders API: {str(e)}")

if __name__ == "__main__":
    fix_orders_api()
