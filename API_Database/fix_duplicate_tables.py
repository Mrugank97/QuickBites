"""
Script to fix duplicate tables in the cs432g11 database
This ensures we don't duplicate any tables that already exist in the CIMS database
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

def fix_duplicate_tables():
    """Remove duplicate tables and update views to use CIMS tables"""
    conn = None
    cursor = None
    
    try:
        # Connect to the database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        
        # Drop the duplicate tables
        logging.info("Dropping duplicate tables...")
        
        # First drop views that depend on these tables
        cursor.execute("DROP VIEW IF EXISTS member_roles")
        cursor.execute("DROP VIEW IF EXISTS member_profiles")
        cursor.execute("DROP VIEW IF EXISTS order_details")
        
        # Drop the duplicate tables
        cursor.execute("DROP TABLE IF EXISTS login")
        cursor.execute("DROP TABLE IF EXISTS members")
        cursor.execute("DROP TABLE IF EXISTS payments")
        
        # Recreate the views to use CIMS tables
        logging.info("Recreating views to use CIMS tables...")
        
        # Create a view to show member information with their roles
        cursor.execute("""
            CREATE OR REPLACE VIEW member_roles AS
            SELECT 
                m.ID as member_id,
                m.UserName as name,
                m.emailID as email,
                CASE
                    WHEN s.member_id IS NOT NULL THEN 'Student'
                    WHEN om.member_id IS NOT NULL THEN 'OutletManager'
                    WHEN a.member_id IS NOT NULL THEN 'Admin'
                    ELSE 'Unknown'
                END as role
            FROM 
                cs432cims.members m
            LEFT JOIN 
                student s ON m.ID = s.member_id
            LEFT JOIN 
                outlet_manager om ON m.ID = om.member_id
            LEFT JOIN 
                admin a ON m.ID = a.member_id
        """)
        logging.info("member_roles view recreated successfully")
        
        # Create a view to show member profiles
        cursor.execute("""
            CREATE OR REPLACE VIEW member_profiles AS
            SELECT 
                m.ID as member_id,
                m.UserName as username,
                m.emailID as email,
                m.DoB as date_of_birth,
                l.Role as role,
                mp.bio,
                mp.skills,
                mp.achievements,
                mp.last_updated
            FROM 
                cs432cims.members m
            LEFT JOIN 
                cs432cims.Login l ON m.ID = l.MemberID
            LEFT JOIN 
                member_portfolio mp ON m.ID = mp.member_id
        """)
        logging.info("member_profiles view recreated successfully")
        
        # Create a view to show orders with customer and outlet information
        cursor.execute("""
            CREATE OR REPLACE VIEW order_details AS
            SELECT 
                o.order_id,
                o.member_id,
                m.UserName as customer_name,
                o.outlet_id,
                ot.name as outlet_name,
                o.total_amount,
                o.order_status,
                o.order_time,
                p.PaymentID as payment_id,
                p.PaymentStatus as payment_status
            FROM 
                orders o
            JOIN 
                cs432cims.members m ON o.member_id = m.ID
            JOIN 
                outlet ot ON o.outlet_id = ot.outlet_id
            LEFT JOIN
                cs432cims.G11_payments p ON o.order_id = p.OrderID
        """)
        logging.info("order_details view recreated successfully")
        
        # Update the orders table to reference G11_payments
        cursor.execute("""
            ALTER TABLE orders
            ADD COLUMN payment_id INT,
            ADD CONSTRAINT fk_payment
            FOREIGN KEY (payment_id) REFERENCES cs432cims.G11_payments(PaymentID)
        """)
        logging.info("orders table updated to reference G11_payments")
        
        # Commit the changes
        conn.commit()
        logging.info("All duplicate tables removed and views updated successfully")
        
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
    fix_duplicate_tables()
