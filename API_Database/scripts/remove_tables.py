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

def remove_table(table_name):
    """Safely remove a table"""
    conn = None
    cursor = None
    
    try:
        # Connect to project database
        conn = get_db_connection(False)
        cursor = conn.cursor()
        
        # Check if table exists
        cursor.execute(f"SHOW TABLES LIKE '{table_name}'")
        table_exists = cursor.fetchone()
        
        if not table_exists:
            logging.warning(f"Table '{table_name}' does not exist.")
            return
        
        # Remove foreign key constraints from the table
        fk_count = remove_foreign_keys(cursor, table_name)
        logging.info(f"Removed {fk_count} foreign key constraints from '{table_name}'.")
        
        # Remove constraints referencing the table
        ref_count = remove_referencing_constraints(cursor, table_name)
        logging.info(f"Removed {ref_count} foreign key constraints referencing '{table_name}'.")
        
        # Drop the table
        logging.info(f"Dropping table '{table_name}'...")
        cursor.execute(f"DROP TABLE `{table_name}`")
        conn.commit()
        
        logging.info(f"Table '{table_name}' successfully removed.")
        
    except Exception as e:
        logging.error(f"Error removing table '{table_name}': {str(e)}")
        if conn:
            conn.rollback()
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def verify_tables_removed():
    """Verify that the tables have been removed"""
    try:
        # Connect to project database
        conn = get_db_connection(False)
        cursor = conn.cursor()
        
        # Check for OutletManager table
        cursor.execute("SHOW TABLES LIKE 'OutletManager'")
        outlet_manager_exists = cursor.fetchone()
        
        if outlet_manager_exists:
            logging.error("OutletManager table still exists!")
        else:
            logging.info("OutletManager table has been successfully removed.")
        
        # Check for Student table
        cursor.execute("SHOW TABLES LIKE 'Student'")
        student_exists = cursor.fetchone()
        
        if student_exists:
            logging.error("Student table still exists!")
        else:
            logging.info("Student table has been successfully removed.")
        
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
        logging.error(f"Error verifying tables removed: {str(e)}")

if __name__ == "__main__":
    logging.info("Removing OutletManager table...")
    remove_table("OutletManager")
    
    logging.info("\nRemoving Student table...")
    remove_table("Student")
    
    logging.info("\nVerifying tables removed...")
    verify_tables_removed()
