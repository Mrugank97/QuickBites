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

def add_payment_method_column():
    """Add payment_method column to orders table"""
    try:
        # Connect to project database
        conn = get_db_connection(False)
        cursor = conn.cursor()
        
        # Check if payment_method column exists
        try:
            cursor.execute("SELECT payment_method FROM orders LIMIT 1")
            logging.info("payment_method column already exists in orders table")
        except mysql.connector.Error as e:
            if "Unknown column" in str(e):
                logging.info("payment_method column does not exist. Adding it...")
                
                # Add payment_method column
                cursor.execute("""
                    ALTER TABLE orders
                    ADD COLUMN payment_method VARCHAR(50) DEFAULT 'UPI'
                """)
                conn.commit()
                logging.info("payment_method column added successfully")
            else:
                raise e
        
        # Verify the orders table structure
        cursor.execute("DESCRIBE orders")
        columns = cursor.fetchall()
        logging.info("Updated orders table structure:")
        for column in columns:
            logging.info(f"  {column[0]} ({column[1].decode('utf-8')}), Null: {column[2]}, Key: {column[3]}, Default: {column[4]}")
        
        # Close connection
        cursor.close()
        conn.close()
        
        logging.info("Orders table fixed successfully")
        
    except Exception as e:
        logging.error(f"Error fixing orders table: {str(e)}")

if __name__ == "__main__":
    add_payment_method_column()
