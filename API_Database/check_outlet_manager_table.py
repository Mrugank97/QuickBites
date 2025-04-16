"""
Script to check the outlet_manager table structure and data
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

def check_outlet_manager_table():
    """Check the outlet_manager table structure and data"""
    conn = None
    cursor = None
    
    try:
        # Connect to the database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        
        # Check if outlet_manager table exists
        cursor.execute("""
            SELECT COUNT(*) as count FROM information_schema.tables
            WHERE table_schema = 'cs432g11' AND table_name = 'outlet_manager'
        """)
        result = cursor.fetchone()
        
        if result and result['count'] > 0:
            logging.info("outlet_manager table exists")
            
            # Check the structure of the outlet_manager table
            cursor.execute("DESCRIBE outlet_manager")
            columns = cursor.fetchall()
            logging.info(f"outlet_manager table has {len(columns)} columns:")
            for column in columns:
                logging.info(f"  {column['Field']}: {column['Type']}")
            
            # Check if there are any records in the outlet_manager table
            cursor.execute("SELECT * FROM outlet_manager")
            managers = cursor.fetchall()
            
            logging.info(f"outlet_manager table has {len(managers)} records:")
            for manager in managers:
                logging.info(f"  {manager}")
                
            # Check if outlet table exists
            cursor.execute("""
                SELECT COUNT(*) as count FROM information_schema.tables
                WHERE table_schema = 'cs432g11' AND table_name = 'outlet'
            """)
            result = cursor.fetchone()
            
            if result and result['count'] > 0:
                logging.info("outlet table exists")
                
                # Check the structure of the outlet table
                cursor.execute("DESCRIBE outlet")
                columns = cursor.fetchall()
                logging.info(f"outlet table has {len(columns)} columns:")
                for column in columns:
                    logging.info(f"  {column['Field']}: {column['Type']}")
                
                # Check if there are any records in the outlet table
                cursor.execute("SELECT * FROM outlet")
                outlets = cursor.fetchall()
                
                logging.info(f"outlet table has {len(outlets)} records:")
                for outlet in outlets:
                    logging.info(f"  {outlet}")
            else:
                logging.warning("outlet table does not exist")
        else:
            logging.warning("outlet_manager table does not exist")
            
        # Check users with Manager role in CIMS database
        cursor.execute("""
            SELECT m.ID, m.UserName, l.Role
            FROM cs432cims.members m
            JOIN cs432cims.Login l ON m.ID = l.MemberID
            WHERE l.Role = 'Manager'
        """)
        managers = cursor.fetchall()
        
        logging.info(f"Found {len(managers)} users with Manager role in CIMS database:")
        for manager in managers:
            logging.info(f"  ID: {manager['ID']}, Username: {manager['UserName']}, Role: {manager['Role']}")
            
            # Check if this manager is assigned to an outlet
            cursor.execute("""
                SELECT * FROM outlet_manager
                WHERE member_id = %s
            """, (manager['ID'],))
            assignment = cursor.fetchone()
            
            if assignment:
                logging.info(f"  Manager {manager['UserName']} is assigned to outlet ID: {assignment['outlet_id']}")
            else:
                logging.warning(f"  Manager {manager['UserName']} is not assigned to any outlet")
                
                # Get the first available outlet
                cursor.execute("SELECT outlet_id FROM outlet ORDER BY outlet_id LIMIT 1")
                outlet = cursor.fetchone()
                
                if outlet:
                    # Assign this manager to the outlet
                    cursor.execute("""
                        INSERT INTO outlet_manager (member_id, outlet_id)
                        VALUES (%s, %s)
                    """, (manager['ID'], outlet['outlet_id']))
                    conn.commit()
                    logging.info(f"  Assigned manager {manager['UserName']} to outlet ID: {outlet['outlet_id']}")
        
    except mysql.connector.Error as e:
        logging.error(f"Database error: {str(e)}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    check_outlet_manager_table()
