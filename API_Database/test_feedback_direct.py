"""
Script to directly test the feedback API without authentication
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

def test_feedback_direct():
    """Test the feedback API directly by inserting into the database"""
    conn = None
    cursor = None
    
    try:
        # Connect to the database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        
        # Insert a test feedback record
        member_id = 1118  # Use a valid member ID from the database (dd)
        outlet_id = 1     # Dawat
        rating = 5
        comments = "Test feedback inserted directly"
        
        query = """
        INSERT INTO feedback (member_id, outlet_id, rating, comments, feedback_time)
        VALUES (%s, %s, %s, %s, NOW())
        """
        cursor.execute(query, (member_id, outlet_id, rating, comments))
        
        # Get the feedback ID
        feedback_id = cursor.lastrowid
        logging.info(f"Created feedback with ID: {feedback_id}")
        
        # Commit the transaction
        conn.commit()
        logging.info(f"Committed feedback transaction")
        
        # Check if the feedback was inserted
        cursor.execute("SELECT * FROM feedback WHERE feedback_id = %s", (feedback_id,))
        feedback = cursor.fetchone()
        
        if feedback:
            logging.info(f"Feedback inserted successfully: {feedback}")
        else:
            logging.error("Feedback not found after insertion")
        
        # Check all feedback records
        cursor.execute("SELECT * FROM feedback")
        all_feedback = cursor.fetchall()
        
        logging.info(f"Total feedback records: {len(all_feedback)}")
        for fb in all_feedback:
            logging.info(f"  {fb}")
        
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
    test_feedback_direct()
