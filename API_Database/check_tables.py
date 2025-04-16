"""
Script to check the structure of menu, orders, and feedback tables
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

def check_tables():
    """Check the structure of menu, orders, and feedback tables"""
    conn = None
    cursor = None
    
    try:
        # Connect to the database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        
        # Check if menu table exists
        cursor.execute("""
            SELECT COUNT(*) as count FROM information_schema.tables
            WHERE table_schema = 'cs432g11' AND table_name = 'menu'
        """)
        result = cursor.fetchone()
        
        if result and result['count'] > 0:
            logging.info("menu table exists")
            
            # Check the structure of the menu table
            cursor.execute("DESCRIBE menu")
            columns = cursor.fetchall()
            logging.info(f"menu table has {len(columns)} columns:")
            for column in columns:
                logging.info(f"  {column['Field']}: {column['Type']}")
            
            # Check if there are any records in the menu table
            cursor.execute("SELECT COUNT(*) as count FROM menu")
            result = cursor.fetchone()
            logging.info(f"menu table has {result['count']} records")
            
            # Get a sample of menu items
            cursor.execute("SELECT * FROM menu LIMIT 5")
            menu_items = cursor.fetchall()
            logging.info("Sample menu items:")
            for item in menu_items:
                logging.info(f"  {item}")
        else:
            logging.warning("menu table does not exist")
        
        # Check if orders table exists
        cursor.execute("""
            SELECT COUNT(*) as count FROM information_schema.tables
            WHERE table_schema = 'cs432g11' AND table_name = 'orders'
        """)
        result = cursor.fetchone()
        
        if result and result['count'] > 0:
            logging.info("orders table exists")
            
            # Check the structure of the orders table
            cursor.execute("DESCRIBE orders")
            columns = cursor.fetchall()
            logging.info(f"orders table has {len(columns)} columns:")
            for column in columns:
                logging.info(f"  {column['Field']}: {column['Type']}")
            
            # Check if there are any records in the orders table
            cursor.execute("SELECT COUNT(*) as count FROM orders")
            result = cursor.fetchone()
            logging.info(f"orders table has {result['count']} records")
            
            # Get a sample of orders
            cursor.execute("SELECT * FROM orders LIMIT 5")
            orders = cursor.fetchall()
            logging.info("Sample orders:")
            for order in orders:
                logging.info(f"  {order}")
        else:
            logging.warning("orders table does not exist")
        
        # Check if feedback table exists
        cursor.execute("""
            SELECT COUNT(*) as count FROM information_schema.tables
            WHERE table_schema = 'cs432g11' AND table_name = 'feedback'
        """)
        result = cursor.fetchone()
        
        if result and result['count'] > 0:
            logging.info("feedback table exists")
            
            # Check the structure of the feedback table
            cursor.execute("DESCRIBE feedback")
            columns = cursor.fetchall()
            logging.info(f"feedback table has {len(columns)} columns:")
            for column in columns:
                logging.info(f"  {column['Field']}: {column['Type']}")
            
            # Check if there are any records in the feedback table
            cursor.execute("SELECT COUNT(*) as count FROM feedback")
            result = cursor.fetchone()
            logging.info(f"feedback table has {result['count']} records")
            
            # Get a sample of feedback
            cursor.execute("SELECT * FROM feedback LIMIT 5")
            feedback = cursor.fetchall()
            logging.info("Sample feedback:")
            for fb in feedback:
                logging.info(f"  {fb}")
        else:
            logging.warning("feedback table does not exist")
        
    except mysql.connector.Error as e:
        logging.error(f"Database error: {str(e)}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    check_tables()
