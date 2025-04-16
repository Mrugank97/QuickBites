import os
import shutil
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Files to move
file_mappings = {
    # API files
    'auth_api.py': 'src/api/auth_api.py',
    'order_management_api.py': 'src/api/order_management_api.py',
    'outlet_manager_api.py': 'src/api/outlet_manager_api.py',
    'profile_api.py': 'src/api/profile_api.py',
    
    # Middleware
    'session_validator.py': 'src/middleware/session_validator.py',
    
    # Models
    'database_manager.py': 'src/models/database_manager.py',
    
    # Controllers
    'member_manager.py': 'src/controllers/member_manager.py',
    'Login.py': 'src/controllers/login_controller.py',
    'UpdateImage.py': 'src/controllers/image_controller.py',
    
    # Config
    'config.py': 'src/config/config.py',
    
    # Static files
    'static': 'public',
    
    # SQL files
    'localhost.sql': 'docs/database_schema.sql',
    'setup_database.sql': 'docs/setup_database.sql',
    
    # Test files
    'test_ui_functionality.py': 'tests/test_ui_functionality.py',
    'check_piyush_assignment.py': 'tests/check_piyush_assignment.py',
    'check_piyush_login.py': 'tests/check_piyush_login.py',
    'fix_outlet_manager_role.py': 'tests/fix_outlet_manager_role.py',
}

def create_directories():
    """Create the directory structure if it doesn't exist"""
    directories = [
        'src/api',
        'src/config',
        'src/controllers',
        'src/models',
        'src/middleware',
        'src/utils',
        'src/services',
        'public/css',
        'public/js',
        'public/img',
        'docs',
        'tests'
    ]
    
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            logging.info(f"Created directory: {directory}")

def move_files():
    """Move files to their new locations"""
    for source, destination in file_mappings.items():
        if not os.path.exists(source):
            logging.warning(f"Source file/directory not found: {source}")
            continue
        
        # Create destination directory if it doesn't exist
        dest_dir = os.path.dirname(destination)
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
            logging.info(f"Created directory: {dest_dir}")
        
        # Handle directories
        if os.path.isdir(source):
            if os.path.exists(destination):
                # If destination exists, copy files individually
                for item in os.listdir(source):
                    s = os.path.join(source, item)
                    d = os.path.join(destination, item)
                    if os.path.isdir(s):
                        if not os.path.exists(d):
                            shutil.copytree(s, d)
                            logging.info(f"Copied directory: {s} -> {d}")
                    else:
                        shutil.copy2(s, d)
                        logging.info(f"Copied file: {s} -> {d}")
            else:
                # If destination doesn't exist, copy the whole directory
                shutil.copytree(source, destination)
                logging.info(f"Copied directory: {source} -> {destination}")
        else:
            # Handle files
            try:
                shutil.copy2(source, destination)
                logging.info(f"Copied file: {source} -> {destination}")
            except Exception as e:
                logging.error(f"Error copying {source} to {destination}: {str(e)}")

def update_main_py():
    """Update main.py to use the new file structure"""
    if not os.path.exists('main.py'):
        logging.warning("main.py not found, skipping update")
        return
    
    with open('main.py', 'r') as f:
        content = f.read()
    
    # Update imports
    replacements = {
        'import auth_api': 'from src.api import auth_api',
        'import order_management_api': 'from src.api import order_management_api',
        'import outlet_manager_api': 'from src.api import outlet_manager_api',
        'import profile_api': 'from src.api import profile_api',
        'import session_validator': 'from src.middleware import session_validator',
        'import database_manager': 'from src.models import database_manager',
        'import member_manager': 'from src.controllers import member_manager',
        'import Login': 'from src.controllers import login_controller as Login',
        'import UpdateImage': 'from src.controllers import image_controller as UpdateImage',
        'import config': 'from src.config import config',
        'static_folder="static"': 'static_folder="public"',
    }
    
    for old, new in replacements.items():
        content = content.replace(old, new)
    
    # Write updated content
    with open('main.py.new', 'w') as f:
        f.write(content)
    
    logging.info("Created updated main.py.new")

if __name__ == "__main__":
    create_directories()
    move_files()
    update_main_py()
    logging.info("Reorganization complete!")
    logging.info("Please review the changes and then rename main.py.new to main.py if everything looks good.")
