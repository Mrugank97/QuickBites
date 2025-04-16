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

def remove_foreign_keys(cursor, table_name):
    """Remove all foreign key constraints from a table"""
    try:
        # Get all foreign key constraints for the table
        cursor.execute(f"""
            SELECT CONSTRAINT_NAME
            FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
            WHERE TABLE_NAME = '{table_name}'
            AND REFERENCED_TABLE_NAME IS NOT NULL
            AND CONSTRAINT_SCHEMA = 'cs432g11'
        """)
        constraints = cursor.fetchall()
        
        # Drop each constraint
        for constraint in constraints:
            constraint_name = constraint[0]
            logging.info(f"Dropping foreign key constraint {constraint_name} from {table_name}")
            cursor.execute(f"ALTER TABLE `{table_name}` DROP FOREIGN KEY `{constraint_name}`")
        
        return len(constraints)
    except Exception as e:
        logging.error(f"Error removing foreign keys from {table_name}: {str(e)}")
        raise

def remove_referencing_constraints(cursor, table_name):
    """Remove all foreign key constraints referencing a table"""
    try:
        # Get all constraints referencing the table
        cursor.execute(f"""
            SELECT CONSTRAINT_NAME, TABLE_NAME
            FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
            WHERE REFERENCED_TABLE_NAME = '{table_name}'
            AND CONSTRAINT_SCHEMA = 'cs432g11'
        """)
        references = cursor.fetchall()
        
        # Drop each constraint
        for ref in references:
            constraint_name = ref[0]
            referencing_table = ref[1]
            logging.info(f"Dropping foreign key constraint {constraint_name} from {referencing_table} that references {table_name}")
            cursor.execute(f"ALTER TABLE `{referencing_table}` DROP FOREIGN KEY `{constraint_name}`")
        
        return len(references)
    except Exception as e:
        logging.error(f"Error removing referencing constraints from {table_name}: {str(e)}")
        raise

def remove_outlet_table():
    """Safely remove the Outlet table"""
    conn = None
    cursor = None
    
    try:
        # Connect to project database
        conn = get_db_connection(False)
        cursor = conn.cursor()
        
        # Check if Outlet table exists
        cursor.execute("SHOW TABLES LIKE 'Outlet'")
        outlet_exists = cursor.fetchone()
        
        if not outlet_exists:
            logging.warning("Outlet table does not exist.")
            return
        
        # Remove foreign key constraints from the table
        fk_count = remove_foreign_keys(cursor, "Outlet")
        logging.info(f"Removed {fk_count} foreign key constraints from Outlet table.")
        
        # Remove constraints referencing the table
        ref_count = remove_referencing_constraints(cursor, "Outlet")
        logging.info(f"Removed {ref_count} foreign key constraints referencing Outlet table.")
        
        # Drop the table
        logging.info("Dropping Outlet table...")
        cursor.execute("DROP TABLE `Outlet`")
        conn.commit()
        
        logging.info("Outlet table successfully removed.")
        
    except Exception as e:
        logging.error(f"Error removing Outlet table: {str(e)}")
        if conn:
            conn.rollback()
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def verify_outlet_removed():
    """Verify that the Outlet table has been removed"""
    try:
        # Connect to project database
        conn = get_db_connection(False)
        cursor = conn.cursor()
        
        # Check if Outlet table exists
        cursor.execute("SHOW TABLES LIKE 'Outlet'")
        outlet_exists = cursor.fetchone()
        
        if outlet_exists:
            logging.error("Outlet table still exists!")
        else:
            logging.info("Outlet table has been successfully removed.")
        
        # Get all tables
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        
        # Extract table names
        table_names = [table[0] for table in tables]
        
        logging.info("Remaining tables in the database:")
        for table in table_names:
            logging.info(f"  - {table}")
        
        # Close connection
        cursor.close()
        conn.close()
        
    except Exception as e:
        logging.error(f"Error verifying Outlet table removed: {str(e)}")

if __name__ == "__main__":
    remove_outlet_table()
    verify_outlet_removed()
