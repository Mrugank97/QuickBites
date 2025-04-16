"""
Script to check current outlet-manager assignments
"""
import mysql.connector
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Database configuration
db_config = {
    "host": "10.0.116.125",
    "user": "cs432g11",
    "password": "pXqJ5NYz",
    "database": "cs432g11"
}

def check_outlet_assignments():
    """Check current outlet-manager assignments"""
    conn = None
    cursor = None
    
    try:
        # Connect to the database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        
        # Get all outlets
        cursor.execute("SELECT * FROM outlet ORDER BY outlet_id")
        outlets = cursor.fetchall()
        
        logging.info(f"Found {len(outlets)} outlets:")
        for outlet in outlets:
            logging.info(f"  Outlet ID: {outlet['outlet_id']}, Name: {outlet['name']}")
            
            # Check if this outlet has a manager
            cursor.execute("""
                SELECT om.*, m.UserName 
                FROM outlet_manager om
                JOIN cs432cims.members m ON om.member_id = m.ID
                WHERE om.outlet_id = %s
            """, (outlet['outlet_id'],))
            managers = cursor.fetchall()
            
            if managers:
                logging.info(f"    Assigned managers ({len(managers)}):")
                for manager in managers:
                    logging.info(f"      Manager ID: {manager['member_id']}, Username: {manager['UserName']}")
            else:
                logging.warning(f"    No manager assigned to this outlet")
        
        # Check if any managers are assigned to multiple outlets
        cursor.execute("""
            SELECT om.member_id, m.UserName, COUNT(om.outlet_id) as outlet_count
            FROM outlet_manager om
            JOIN cs432cims.members m ON om.member_id = m.ID
            GROUP BY om.member_id
            HAVING COUNT(om.outlet_id) > 1
        """)
        multi_assigned = cursor.fetchall()
        
        if multi_assigned:
            logging.warning(f"Found {len(multi_assigned)} managers assigned to multiple outlets:")
            for manager in multi_assigned:
                logging.warning(f"  Manager ID: {manager['member_id']}, Username: {manager['UserName']}, Outlet Count: {manager['outlet_count']}")
                
                # Get the outlets this manager is assigned to
                cursor.execute("""
                    SELECT o.outlet_id, o.name
                    FROM outlet_manager om
                    JOIN outlet o ON om.outlet_id = o.outlet_id
                    WHERE om.member_id = %s
                """, (manager['member_id'],))
                assigned_outlets = cursor.fetchall()
                
                for outlet in assigned_outlets:
                    logging.warning(f"    Outlet ID: {outlet['outlet_id']}, Name: {outlet['name']}")
        
        # Check if any outlets have multiple managers
        cursor.execute("""
            SELECT om.outlet_id, o.name, COUNT(om.member_id) as manager_count
            FROM outlet_manager om
            JOIN outlet o ON om.outlet_id = o.outlet_id
            GROUP BY om.outlet_id
            HAVING COUNT(om.member_id) > 1
        """)
        multi_managed = cursor.fetchall()
        
        if multi_managed:
            logging.warning(f"Found {len(multi_managed)} outlets with multiple managers:")
            for outlet in multi_managed:
                logging.warning(f"  Outlet ID: {outlet['outlet_id']}, Name: {outlet['name']}, Manager Count: {outlet['manager_count']}")
                
                # Get the managers assigned to this outlet
                cursor.execute("""
                    SELECT om.member_id, m.UserName
                    FROM outlet_manager om
                    JOIN cs432cims.members m ON om.member_id = m.ID
                    WHERE om.outlet_id = %s
                """, (outlet['outlet_id'],))
                assigned_managers = cursor.fetchall()
                
                for manager in assigned_managers:
                    logging.warning(f"    Manager ID: {manager['member_id']}, Username: {manager['UserName']}")
        
    except mysql.connector.Error as e:
        logging.error(f"Database error: {str(e)}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    check_outlet_assignments()
