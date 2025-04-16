import mysql.connector

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
        print(f"Database connection failed: {str(e)}")
        raise

def check_order_tables():
    try:
        conn = get_db_connection(False)  # Use project database
        cursor = conn.cursor(dictionary=True)
        
        # Check orders table structure
        print("=== ORDERS TABLE STRUCTURE ===")
        cursor.execute("DESCRIBE orders")
        columns = cursor.fetchall()
        for column in columns:
            print(column)
        
        # Check order_items table structure
        print("\n=== ORDER_ITEMS TABLE STRUCTURE ===")
        cursor.execute("DESCRIBE order_items")
        columns = cursor.fetchall()
        for column in columns:
            print(column)
        
        # Check sample orders
        print("\n=== SAMPLE ORDERS (LIMIT 5) ===")
        cursor.execute("SELECT * FROM orders LIMIT 5")
        orders = cursor.fetchall()
        for order in orders:
            print(order)
        
        # Check sample order items
        print("\n=== SAMPLE ORDER ITEMS (LIMIT 5) ===")
        cursor.execute("SELECT * FROM order_items LIMIT 5")
        items = cursor.fetchall()
        for item in items:
            print(item)
        
        # Check payment table in CIMS
        print("\n=== PAYMENT TABLE STRUCTURE IN CIMS ===")
        cims_conn = get_db_connection(True)
        cims_cursor = cims_conn.cursor(dictionary=True)
        try:
            cims_cursor.execute("DESCRIBE G11_payments")
            columns = cims_cursor.fetchall()
            for column in columns:
                print(column)
                
            # Check sample payments
            print("\n=== SAMPLE PAYMENTS (LIMIT 5) ===")
            cims_cursor.execute("SELECT * FROM G11_payments LIMIT 5")
            payments = cims_cursor.fetchall()
            for payment in payments:
                print(payment)
        except Exception as e:
            print(f"Error checking payment table: {str(e)}")
        finally:
            cims_cursor.close()
            cims_conn.close()
        
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    check_order_tables()
