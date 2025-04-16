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

def check_menu_items():
    try:
        conn = get_db_connection(False)  # Use project database
        cursor = conn.cursor(dictionary=True)
        
        # Check menu table structure
        print("=== MENU TABLE STRUCTURE ===")
        cursor.execute("DESCRIBE menu")
        columns = cursor.fetchall()
        for column in columns:
            print(column)
        
        # Count menu items by outlet
        print("\n=== MENU ITEMS COUNT BY OUTLET ===")
        cursor.execute("""
            SELECT o.outlet_id, o.name as outlet_name, COUNT(m.menu_id) as item_count
            FROM outlet o
            LEFT JOIN menu m ON o.outlet_id = m.outlet_id
            GROUP BY o.outlet_id, o.name
            ORDER BY o.name
        """)
        counts = cursor.fetchall()
        for count in counts:
            print(f"Outlet: {count['outlet_name']} (ID: {count['outlet_id']}) - {count['item_count']} items")
        
        # Check sample menu items for each outlet
        for outlet_id in range(1, 7):  # Assuming outlet IDs 1-6
            print(f"\n=== SAMPLE MENU ITEMS FOR OUTLET ID {outlet_id} (LIMIT 5) ===")
            cursor.execute(f"SELECT * FROM menu WHERE outlet_id = {outlet_id} LIMIT 5")
            items = cursor.fetchall()
            if items:
                for item in items:
                    print(f"ID: {item['menu_id']} - {item['item_name']} - ₹{item['price']} - Available: {item['available']}")
            else:
                print(f"No menu items found for outlet ID {outlet_id}")
        
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    check_menu_items()
