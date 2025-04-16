"""
Script to check if there's any data in the outlet table
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

def check_outlet_data():
    """Check if there's any data in the outlet table"""
    conn = None
    cursor = None
    
    try:
        # Connect to the database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        
        # Check outlet table
        cursor.execute("SELECT * FROM outlet")
        outlets = cursor.fetchall()
        
        print(f"\nFound {len(outlets)} outlets in the outlet table:")
        if outlets:
            for outlet in outlets:
                print(f"ID: {outlet['outlet_id']}, Name: {outlet['name']}, Location: {outlet['location']}")
        else:
            print("No outlets found. Let's insert some sample data.")
            
            # Insert sample outlets
            cursor.execute("""
                INSERT INTO outlet (name, location) VALUES
                ('Dawat', 'H-Hostel, Ground Floor'),
                ('Just Chill', 'B-Hostel, Ground Floor'),
                ('Tea Post', 'E-Hostel, Ground Floor'),
                ('Madurai Chaat & More', 'Near Sports Complex'),
                ('AS FastFood', 'I-Hostel, Ground Floor'),
                ('VS Fastfood', 'H-Hostel, Ground Floor')
            """)
            
            conn.commit()
            print("Sample outlets inserted successfully!")
            
            # Verify the inserted data
            cursor.execute("SELECT * FROM outlet")
            outlets = cursor.fetchall()
            print(f"\nNow there are {len(outlets)} outlets in the outlet table:")
            for outlet in outlets:
                print(f"ID: {outlet['outlet_id']}, Name: {outlet['name']}, Location: {outlet['location']}")
        
    except mysql.connector.Error as e:
        logging.error(f"Database error: {str(e)}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    check_outlet_data()
