"""
Script to check if the G11_payments table exists in CIMS database
"""
import mysql.connector
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Database configuration
db_config_cims = {
    "host": "10.0.116.125",
    "user": "cs432g11",
    "password": "pXqJ5NYz",
    "database": "cs432cims"
}

def check_payments_table():
    """Check if the G11_payments table exists in CIMS database"""
    conn = None
    
    try:
        # Connect to CIMS database
        conn = mysql.connector.connect(**db_config_cims)
        cursor = conn.cursor()
        
        # Check if G11_payments table exists
        cursor.execute("SHOW TABLES LIKE 'G11_payments'")
        table_exists = cursor.fetchone()
        
        if table_exists:
            print("G11_payments table exists in CIMS database")
            
            # Check table structure
            cursor.execute("DESCRIBE G11_payments")
            columns = cursor.fetchall()
            print("\nTable structure:")
            for column in columns:
                print(column)
            
            # Check if there are any records
            cursor.execute("SELECT COUNT(*) FROM G11_payments")
            count = cursor.fetchone()[0]
            print(f"\nNumber of records: {count}")
            
            if count > 0:
                cursor.execute("SELECT * FROM G11_payments LIMIT 5")
                records = cursor.fetchall()
                print("\nSample records:")
                for record in records:
                    print(record)
        else:
            print("G11_payments table does not exist in CIMS database")
            print("Let's create it manually...")
            
            try:
                # Try to create the table
                cursor.execute("""
                CREATE TABLE G11_payments (
                    PaymentID INT AUTO_INCREMENT PRIMARY KEY,
                    OrderID INT NOT NULL,
                    AmountPaid DECIMAL(10, 2) NOT NULL,
                    PaymentMethod VARCHAR(50) DEFAULT 'UPI',
                    PaymentStatus ENUM('Pending', 'Completed', 'Failed') DEFAULT 'Pending',
                    PaymentTime DATETIME NOT NULL
                )
                """)
                print("G11_payments table created successfully")
            except mysql.connector.Error as e:
                print(f"Error creating table: {str(e)}")
                print("You may need to ask the database administrator to create this table for you")
        
    except mysql.connector.Error as e:
        logging.error(f"Database error: {str(e)}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    check_payments_table()
