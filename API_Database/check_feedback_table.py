"""
Script to check if the feedback table exists in the database
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

def check_feedback_table():
    """Check if the feedback table exists in the database"""
    conn = None
    cursor = None
    
    try:
        # Connect to the database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        
        # Check if feedback table exists
        cursor.execute("""
            SELECT COUNT(*) as count FROM information_schema.tables
            WHERE table_schema = 'cs432g11' AND table_name = 'feedback'
        """)
        result = cursor.fetchone()
        
        if result and result[0] > 0:
            logging.info("Feedback table exists")
            
            # Check the structure of the feedback table
            cursor.execute("DESCRIBE feedback")
            columns = cursor.fetchall()
            logging.info(f"Feedback table has {len(columns)} columns:")
            for column in columns:
                logging.info(f"  {column[0]}: {column[1]}")
            
            # Check if there are any records in the feedback table
            cursor.execute("SELECT COUNT(*) FROM feedback")
            count = cursor.fetchone()[0]
            logging.info(f"Feedback table has {count} records")
            
            if count > 0:
                # Show some sample records
                cursor.execute("SELECT * FROM feedback LIMIT 5")
                records = cursor.fetchall()
                logging.info("Sample records:")
                for record in records:
                    logging.info(f"  {record}")
        else:
            logging.warning("Feedback table does not exist")
            
            # Create the feedback table
            logging.info("Creating feedback table...")
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS feedback (
                    feedback_id INT AUTO_INCREMENT PRIMARY KEY,
                    member_id INT NOT NULL,
                    outlet_id INT NOT NULL,
                    order_id INT,
                    rating INT NOT NULL CHECK (rating BETWEEN 1 AND 5),
                    comments TEXT,
                    feedback_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            logging.info("Feedback table created successfully")
        
    except mysql.connector.Error as e:
        logging.error(f"Database error: {str(e)}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    check_feedback_table()
