"""
Script to update the database schema:
1. Remove the member_portfolio table
2. Modify user_roles_mapping to prevent multiple mappings
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

def update_schema():
    """Update the database schema"""
    conn = None
    cursor = None
    
    try:
        # Connect to the database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        
        # Drop views that depend on member_portfolio
        logging.info("Dropping dependent views...")
        cursor.execute("DROP VIEW IF EXISTS member_profiles")
        
        # Drop the member_portfolio table
        logging.info("Removing member_portfolio table...")
        cursor.execute("DROP TABLE IF EXISTS member_portfolio")
        
        # Recreate the member_profiles view without member_portfolio
        logging.info("Recreating member_profiles view...")
        cursor.execute("""
            CREATE OR REPLACE VIEW member_profiles AS
            SELECT 
                m.ID as member_id,
                m.UserName as username,
                m.emailID as email,
                m.DoB as date_of_birth,
                l.Role as role
            FROM 
                cs432cims.members m
            LEFT JOIN 
                cs432cims.Login l ON m.ID = l.MemberID
        """)
        logging.info("member_profiles view recreated successfully")
        
        # Modify user_roles_mapping to prevent multiple mappings
        logging.info("Modifying user_roles_mapping table...")
        
        # First, drop the existing table
        cursor.execute("DROP TABLE IF EXISTS user_roles_mapping")
        
        # Recreate with a unique constraint on member_id
        cursor.execute("""
            CREATE TABLE user_roles_mapping (
                mapping_id INT AUTO_INCREMENT PRIMARY KEY,
                member_id INT NOT NULL,
                role_id INT NOT NULL,
                UNIQUE KEY (member_id),
                FOREIGN KEY (role_id) REFERENCES roles(id)
            )
        """)
        logging.info("user_roles_mapping table modified successfully")
        
        # Commit the changes
        conn.commit()
        logging.info("Schema updated successfully")
        
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
    update_schema()
