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

def fix_outlet_manager_assignments():
    """Check and fix outlet manager assignments"""
    try:
        # Connect to project database
        conn = get_db_connection(False)
        cursor = conn.cursor(dictionary=True)
        
        # Check if outlet_manager table exists
        cursor.execute("SHOW TABLES LIKE 'outlet_manager'")
        table_exists = cursor.fetchone()
        
        if not table_exists:
            logging.warning("outlet_manager table does not exist. Creating it...")
            
            # Create outlet_manager table
            cursor.execute("""
                CREATE TABLE outlet_manager (
                    outlet_id INT NOT NULL,
                    member_id INT NOT NULL,
                    auto_assigned BOOLEAN DEFAULT FALSE,
                    PRIMARY KEY (outlet_id, member_id),
                    FOREIGN KEY (outlet_id) REFERENCES outlet(outlet_id) ON DELETE CASCADE
                )
            """)
            conn.commit()
            logging.info("outlet_manager table created successfully.")
        
        # Check current assignments
        cursor.execute("""
            SELECT om.outlet_id, o.name as outlet_name, om.member_id, m.UserName as manager_name
            FROM outlet_manager om
            JOIN outlet o ON om.outlet_id = o.outlet_id
            JOIN cs432cims.members m ON om.member_id = m.ID
        """)
        assignments = cursor.fetchall()
        
        logging.info(f"Found {len(assignments)} outlet manager assignments:")
        for assignment in assignments:
            logging.info(f"  Outlet: {assignment['outlet_name']} (ID: {assignment['outlet_id']}), Manager: {assignment['manager_name']} (ID: {assignment['member_id']})")
        
        # Check for outlets without managers
        cursor.execute("""
            SELECT o.outlet_id, o.name
            FROM outlet o
            LEFT JOIN outlet_manager om ON o.outlet_id = om.outlet_id
            WHERE om.outlet_id IS NULL
        """)
        unassigned_outlets = cursor.fetchall()
        
        if unassigned_outlets:
            logging.warning(f"Found {len(unassigned_outlets)} outlets without managers:")
            for outlet in unassigned_outlets:
                logging.warning(f"  Outlet: {outlet['name']} (ID: {outlet['outlet_id']})")
        
        # Check for managers assigned to multiple outlets
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
                logging.warning(f"  Manager: {manager['UserName']} (ID: {manager['member_id']}), Outlet Count: {manager['outlet_count']}")
                
                # Get the outlets assigned to this manager
                cursor.execute("""
                    SELECT o.outlet_id, o.name
                    FROM outlet_manager om
                    JOIN outlet o ON om.outlet_id = o.outlet_id
                    WHERE om.member_id = %s
                """, (manager['member_id'],))
                assigned_outlets = cursor.fetchall()
                
                for outlet in assigned_outlets:
                    logging.warning(f"    Outlet: {outlet['name']} (ID: {outlet['outlet_id']})")
                
                # Keep only the first assignment and remove others
                if len(assigned_outlets) > 1:
                    logging.warning(f"  Removing extra assignments for manager {manager['UserName']} (ID: {manager['member_id']})")
                    
                    # Keep the first outlet and remove others
                    first_outlet = assigned_outlets[0]
                    for outlet in assigned_outlets[1:]:
                        cursor.execute("""
                            DELETE FROM outlet_manager
                            WHERE member_id = %s AND outlet_id = %s
                        """, (manager['member_id'], outlet['outlet_id']))
                    
                    conn.commit()
                    logging.info(f"  Kept assignment for outlet {first_outlet['name']} (ID: {first_outlet['outlet_id']})")
        
        # Check for outlets with multiple managers
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
                logging.warning(f"  Outlet: {outlet['name']} (ID: {outlet['outlet_id']}), Manager Count: {outlet['manager_count']}")
                
                # Get the managers assigned to this outlet
                cursor.execute("""
                    SELECT om.member_id, m.UserName
                    FROM outlet_manager om
                    JOIN cs432cims.members m ON om.member_id = m.ID
                    WHERE om.outlet_id = %s
                """, (outlet['outlet_id'],))
                assigned_managers = cursor.fetchall()
                
                for manager in assigned_managers:
                    logging.warning(f"    Manager: {manager['UserName']} (ID: {manager['member_id']})")
                
                # Keep only the first manager and remove others
                if len(assigned_managers) > 1:
                    logging.warning(f"  Removing extra managers for outlet {outlet['name']} (ID: {outlet['outlet_id']})")
                    
                    # Keep the first manager and remove others
                    first_manager = assigned_managers[0]
                    for manager in assigned_managers[1:]:
                        cursor.execute("""
                            DELETE FROM outlet_manager
                            WHERE outlet_id = %s AND member_id = %s
                        """, (outlet['outlet_id'], manager['member_id']))
                    
                    conn.commit()
                    logging.info(f"  Kept assignment for manager {first_manager['UserName']} (ID: {first_manager['member_id']})")
        
        # Check if any managers have undefined IDs
        cursor.execute("""
            SELECT om.outlet_id, o.name as outlet_name, om.member_id, m.UserName as manager_name
            FROM outlet_manager om
            LEFT JOIN cs432cims.members m ON om.member_id = m.ID
            JOIN outlet o ON om.outlet_id = o.outlet_id
            WHERE m.ID IS NULL
        """)
        invalid_managers = cursor.fetchall()
        
        if invalid_managers:
            logging.warning(f"Found {len(invalid_managers)} assignments with invalid manager IDs:")
            for assignment in invalid_managers:
                logging.warning(f"  Outlet: {assignment['outlet_name']} (ID: {assignment['outlet_id']}), Manager ID: {assignment['member_id']} (not found in members table)")
                
                # Remove invalid assignments
                cursor.execute("""
                    DELETE FROM outlet_manager
                    WHERE outlet_id = %s AND member_id = %s
                """, (assignment['outlet_id'], assignment['member_id']))
            
            conn.commit()
            logging.info("Removed assignments with invalid manager IDs")
        
        # Verify the outlet_manager table structure
        cursor.execute("DESCRIBE outlet_manager")
        columns = cursor.fetchall()
        logging.info("outlet_manager table structure:")
        for column in columns:
            logging.info(f"  {column['Field']} ({column['Type']}), Null: {column['Null']}, Key: {column['Key']}, Default: {column['Default']}")
        
        # Close connection
        cursor.close()
        conn.close()
        
        logging.info("Outlet manager assignments fixed successfully")
        
    except Exception as e:
        logging.error(f"Error fixing outlet manager assignments: {str(e)}")

if __name__ == "__main__":
    fix_outlet_manager_assignments()
