"""
Script to list tables in the CIMS database that are specific to Group 11
"""
import mysql.connector
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Database configuration for CIMS
cims_config = {
    "host": "10.0.116.125",
    "user": "cs432g11",
    "password": "pXqJ5NYz",
    "database": "cs432cims"
}

def list_cims_tables():
    """List tables in the CIMS database, focusing on Group 11 specific tables"""
    conn = None
    cursor = None
    
    try:
        # Connect to the CIMS database
        conn = mysql.connector.connect(**cims_config)
        cursor = conn.cursor()
        
        # Get all tables in CIMS
        cursor.execute("""
            SELECT table_name, table_type 
            FROM information_schema.tables 
            WHERE table_schema = 'cs432cims'
            ORDER BY table_name
        """)
        
        tables = cursor.fetchall()
        
        print("\n=== All Tables in CIMS database ===")
        print("Table Name".ljust(30) + "Table Type")
        print("-" * 50)
        
        for table_name, table_type in tables:
            print(f"{table_name.ljust(30)} {table_type}")
        
        # Get tables specific to Group 11 (prefixed with G11_)
        cursor.execute("""
            SELECT table_name, table_type 
            FROM information_schema.tables 
            WHERE table_schema = 'cs432cims' AND table_name LIKE 'G11_%'
            ORDER BY table_name
        """)
        
        g11_tables = cursor.fetchall()
        
        print("\n=== Group 11 Specific Tables in CIMS database ===")
        print("Table Name".ljust(30) + "Table Type")
        print("-" * 50)
        
        if g11_tables:
            for table_name, table_type in g11_tables:
                print(f"{table_name.ljust(30)} {table_type}")
                
                # Get details for each Group 11 table
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
        else:
            print("No Group 11 specific tables found in CIMS database")
        
    except mysql.connector.Error as e:
        logging.error(f"Database error: {str(e)}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    list_cims_tables()
