import mysql.connector
import logging

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

def delete_outlets():
    """Delete specified outlets"""
    try:
        # Connect to project database
        conn = get_db_connection(False)
        cursor = conn.cursor(dictionary=True)
        
        # Outlets to delete
        outlets_to_delete = ["New Outlet 7", "New Outlet 8"]
        
        # First, check if these outlets exist
        outlet_ids = []
        for outlet_name in outlets_to_delete:
            cursor.execute("SELECT outlet_id FROM outlet WHERE name = %s", (outlet_name,))
            result = cursor.fetchone()
            if result:
                outlet_ids.append(result['outlet_id'])
                logging.info(f"Found outlet '{outlet_name}' with ID {result['outlet_id']}")
            else:
                logging.warning(f"Outlet '{outlet_name}' not found")
        
        if not outlet_ids:
            logging.warning("No outlets found to delete")
            cursor.close()
            conn.close()
            return
        
        # Check if there are any orders associated with these outlets
        for outlet_id in outlet_ids:
            cursor.execute("SELECT COUNT(*) as count FROM orders WHERE outlet_id = %s", (outlet_id,))
            order_count = cursor.fetchone()['count']
            
            if order_count > 0:
                logging.warning(f"Outlet ID {outlet_id} has {order_count} associated orders. Cannot delete.")
                outlet_ids.remove(outlet_id)
            else:
                logging.info(f"Outlet ID {outlet_id} has no associated orders. Safe to delete.")
        
        if not outlet_ids:
            logging.warning("No outlets can be safely deleted")
            cursor.close()
            conn.close()
            return
        
        # Check if there are any menu items associated with these outlets
        for outlet_id in outlet_ids.copy():  # Use copy to avoid modifying during iteration
            cursor.execute("SELECT COUNT(*) as count FROM menu WHERE outlet_id = %s", (outlet_id,))
            menu_count = cursor.fetchone()['count']
            
            if menu_count > 0:
                logging.info(f"Outlet ID {outlet_id} has {menu_count} associated menu items. Deleting them first.")
                
                # Delete associated menu items
                cursor.execute("DELETE FROM menu WHERE outlet_id = %s", (outlet_id,))
                conn.commit()
                logging.info(f"Deleted {menu_count} menu items for outlet ID {outlet_id}")
        
        # Check if there are any outlet managers associated with these outlets
        for outlet_id in outlet_ids.copy():  # Use copy to avoid modifying during iteration
            cursor.execute("SELECT COUNT(*) as count FROM outlet_manager WHERE outlet_id = %s", (outlet_id,))
            manager_count = cursor.fetchone()['count']
            
            if manager_count > 0:
                logging.info(f"Outlet ID {outlet_id} has {manager_count} associated outlet managers. Deleting them first.")
                
                # Delete associated outlet managers
                cursor.execute("DELETE FROM outlet_manager WHERE outlet_id = %s", (outlet_id,))
                conn.commit()
                logging.info(f"Deleted {manager_count} outlet managers for outlet ID {outlet_id}")
        
        # Now delete the outlets
        for outlet_id in outlet_ids:
            cursor.execute("DELETE FROM outlet WHERE outlet_id = %s", (outlet_id,))
            conn.commit()
            logging.info(f"Deleted outlet with ID {outlet_id}")
        
        # Verify the deletion
        cursor.execute("SELECT * FROM outlet")
        remaining_outlets = cursor.fetchall()
        logging.info(f"Remaining outlets ({len(remaining_outlets)}):")
        for outlet in remaining_outlets:
            logging.info(f"  ID: {outlet['outlet_id']}, Name: {outlet['name']}, Location: {outlet['location']}")
        
        # Close connection
        cursor.close()
        conn.close()
        
        logging.info("Outlet deletion completed")
        
    except Exception as e:
        logging.error(f"Error deleting outlets: {str(e)}")

if __name__ == "__main__":
    delete_outlets()
