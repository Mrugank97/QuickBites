"""
Script to list all tables in the cs432g11 database
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

def list_tables():
    """List all tables in the cs432g11 database"""
    conn = None
    cursor = None
    
    try:
        # Connect to the database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        
        # Get all tables
        cursor.execute("""
            SELECT table_name, table_type 
            FROM information_schema.tables 
            WHERE table_schema = 'cs432g11'
            ORDER BY table_type, table_name
        """)
        
        tables = cursor.fetchall()
        
        print("\n=== Tables in cs432g11 database ===")
        print("Table Name".ljust(30) + "Table Type")
        print("-" * 50)
        
        for table_name, table_type in tables:
            print(f"{table_name.ljust(30)} {table_type}")
        
        print("\n=== Table Details ===")
        
        # Get details for each table
        for table_name, _ in tables:
            if table_name not in ('group11_members', 'member_profiles'):  # Skip views
                cursor.execute(f"DESCRIBE {table_name}")
                columns = cursor.fetchall()
                
                print(f"\nTable: {table_name}")
                print("Column Name".ljust(20) + "Type".ljust(20) + "Null".ljust(10) + "Key".ljust(10) + "Default".ljust(15) + "Extra")
                print("-" * 85)
                
                for column in columns:
                    col_name = column[0] if column[0] else ""
                    col_type = column[1] if column[1] else ""
                    col_null = column[2] if column[2] else ""
                    col_key = column[3] if column[3] else ""
                    col_default = str(column[4]) if column[4] is not None else "NULL"
                    col_extra = column[5] if column[5] else ""
                    
                    print(f"{col_name.ljust(20)}{col_type.ljust(20)}{col_null.ljust(10)}{col_key.ljust(10)}{col_default.ljust(15)}{col_extra}")
        
    except mysql.connector.Error as e:
        logging.error(f"Database error: {str(e)}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    list_tables()
