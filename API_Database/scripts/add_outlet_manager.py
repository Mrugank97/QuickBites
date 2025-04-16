"""
Script to add an outlet manager to the database
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

def add_outlet_manager():
    """Add an outlet manager to the database"""
    conn = None
    cursor = None

    try:
        # Connect to the database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # First, check if there are any members in the CIMS database
        cursor.execute("SELECT ID, UserName FROM cs432cims.members LIMIT 5")
        members = cursor.fetchall()
        
        if not members:
            logging.warning("No members found in CIMS database")
            return
            
        # Use the first member as the outlet manager
        member_id = members[0][0]
        member_name = members[0][1]
        logging.info(f"Using member {member_name} (ID: {member_id}) as outlet manager")
        
        # Check if there are any outlets
        cursor.execute("SELECT outlet_id, name FROM outlet LIMIT 1")
        outlets = cursor.fetchall()
        
        if not outlets:
            logging.warning("No outlets found in database")
            return
            
        # Use the first outlet
        outlet_id = outlets[0][0]
        outlet_name = outlets[0][1]
        logging.info(f"Using outlet {outlet_name} (ID: {outlet_id})")
        
        # Check if this member is already an outlet manager
        cursor.execute("SELECT * FROM outlet_manager WHERE member_id = %s", (member_id,))
        existing_manager = cursor.fetchone()
        
        if existing_manager:
            logging.info(f"Member {member_name} is already an outlet manager")
            
            # Update the assigned outlet
            cursor.execute("""
                UPDATE outlet_manager SET assigned_outlet_id = %s WHERE member_id = %s
            """, (outlet_id, member_id))
            logging.info(f"Updated assigned outlet to {outlet_name} (ID: {outlet_id})")
        else:
            # Insert the outlet manager
            cursor.execute("""
                INSERT INTO outlet_manager (member_id, assigned_outlet_id)
                VALUES (%s, %s)
            """, (member_id, outlet_id))
            logging.info(f"Added {member_name} as manager for outlet {outlet_name}")
        
        # Update the role in the CIMS database
        try:
            cursor.execute("""
                UPDATE cs432cims.Login SET Role = 'OutletManager' WHERE MemberID = %s
            """, (member_id,))
            logging.info(f"Updated role to OutletManager in CIMS database")
        except Exception as e:
            logging.warning(f"Could not update role in CIMS database: {str(e)}")
        
        # Commit the transaction
        conn.commit()
        logging.info(f"Successfully added/updated outlet manager")

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
    add_outlet_manager()
