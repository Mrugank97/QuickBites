"""
Script to fix the outlet_manager table structure
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

def fix_outlet_manager_table():
    """Fix the outlet_manager table structure"""
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
            
            # Check if the table has the correct structure
            has_member_id = False
            outlet_id_column = None
            
            for column in columns:
                if column['Field'] == 'member_id':
                    has_member_id = True
                if 'outlet' in column['Field'].lower():
                    outlet_id_column = column['Field']
            
            if has_member_id and outlet_id_column:
                logging.info(f"outlet_manager table has correct structure with outlet ID column: {outlet_id_column}")
                
                # Rename the column to outlet_id if it's not already named that
                if outlet_id_column != 'outlet_id':
                    logging.info(f"Renaming column {outlet_id_column} to outlet_id")
                    
                    # Check if there's any data in the table
                    cursor.execute(f"SELECT * FROM outlet_manager")
                    data = cursor.fetchall()
                    
                    if data:
                        logging.info(f"Found {len(data)} records in outlet_manager table")
                        
                        # Create a backup of the data
                        backup_data = []
                        for row in data:
                            backup_data.append({
                                'member_id': row['member_id'],
                                'outlet_id': row[outlet_id_column]
                            })
                        
                        # Drop the table
                        cursor.execute("DROP TABLE outlet_manager")
                        logging.info("Dropped outlet_manager table")
                        
                        # Create the table with the correct structure
                        cursor.execute("""
                            CREATE TABLE outlet_manager (
                                member_id INT NOT NULL,
                                outlet_id INT NOT NULL,
                                PRIMARY KEY (member_id),
                                FOREIGN KEY (outlet_id) REFERENCES outlet(outlet_id)
                            )
                        """)
                        logging.info("Created outlet_manager table with correct structure")
                        
                        # Restore the data
                        for row in backup_data:
                            cursor.execute("""
                                INSERT INTO outlet_manager (member_id, outlet_id)
                                VALUES (%s, %s)
                            """, (row['member_id'], row['outlet_id']))
                        
                        conn.commit()
                        logging.info(f"Restored {len(backup_data)} records to outlet_manager table")
                    else:
                        # No data, just recreate the table
                        cursor.execute("DROP TABLE outlet_manager")
                        logging.info("Dropped outlet_manager table")
                        
                        cursor.execute("""
                            CREATE TABLE outlet_manager (
                                member_id INT NOT NULL,
                                outlet_id INT NOT NULL,
                                PRIMARY KEY (member_id),
                                FOREIGN KEY (outlet_id) REFERENCES outlet(outlet_id)
                            )
                        """)
                        logging.info("Created outlet_manager table with correct structure")
                        conn.commit()
            else:
                logging.warning("outlet_manager table has incorrect structure")
                
                # Drop and recreate the table
                cursor.execute("DROP TABLE outlet_manager")
                logging.info("Dropped outlet_manager table")
                
                cursor.execute("""
                    CREATE TABLE outlet_manager (
                        member_id INT NOT NULL,
                        outlet_id INT NOT NULL,
                        PRIMARY KEY (member_id),
                        FOREIGN KEY (outlet_id) REFERENCES outlet(outlet_id)
                    )
                """)
                logging.info("Created outlet_manager table with correct structure")
                conn.commit()
        else:
            logging.warning("outlet_manager table does not exist")
            
            # Create the table
            cursor.execute("""
                CREATE TABLE outlet_manager (
                    member_id INT NOT NULL,
                    outlet_id INT NOT NULL,
                    PRIMARY KEY (member_id),
                    FOREIGN KEY (outlet_id) REFERENCES outlet(outlet_id)
                )
            """)
            logging.info("Created outlet_manager table")
            conn.commit()
        
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
        if conn:
            conn.rollback()
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    fix_outlet_manager_table()
