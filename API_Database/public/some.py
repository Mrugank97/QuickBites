class DatabaseAccessLogger:
    def __init__(self, db_config):
        self.db_config = db_config
        self.setup_logging()
    
    def setup_logging(self):
        # Configure logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('database_access.log'),
                logging.StreamHandler()
            ]
        )
    
    def log_access(self, user_id, action, table, query, is_authorized):
        """Log database access with authorization status"""
        try:
            conn = mysql.connector.connect(**self.db_config)
            cursor = conn.cursor()
            
            # Insert log entry
            query = """
            INSERT INTO access_logs 
            (user_id, action, table_name, query, timestamp, is_authorized) 
            VALUES (%s, %s, %s, %s, NOW(), %s)
            """
            cursor.execute(query, (user_id, action, table, query, is_authorized))
            conn.commit()
            
            # If unauthorized, also log to file with warning level
            if not is_authorized:
                logging.warning(
                    f"UNAUTHORIZED ACCESS: User {user_id} performed {action} on {table} with query: {query}"
                )
            
            cursor.close()
            conn.close()
        except Exception as e:
            logging.error(f"Error logging database access: {str(e)}")

# Usage example
db_logger = DatabaseAccessLogger(db_config)

# Log authorized access
db_logger.log_access(
    user_id=1001, 
    action="SELECT", 
    table="orders", 
    query="SELECT * FROM orders WHERE member_id = 1001", 
    is_authorized=True
)

# Log unauthorized access
db_logger.log_access(
    user_id=1001, 
    action="UPDATE", 
    table="orders", 
    query="UPDATE orders SET status = 'Completed' WHERE order_id = 5002", 
    is_authorized=False
)