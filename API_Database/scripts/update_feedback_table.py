"""
Script to update the feedback table schema
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

def update_feedback_table():
    """Update the feedback table schema"""
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
            logging.info("Feedback table exists, dropping it to recreate with correct schema")
            
            # Drop the existing feedback table
            cursor.execute("DROP TABLE feedback")
            logging.info("Feedback table dropped")
        
        # Create the feedback table with the correct schema
        logging.info("Creating feedback table with correct schema...")
        cursor.execute("""
            CREATE TABLE feedback (
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
        
        # Commit the changes
        conn.commit()
        
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
    update_feedback_table()
