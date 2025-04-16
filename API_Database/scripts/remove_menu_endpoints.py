import re

def remove_menu_endpoints():
    # Read the main.py file
    with open('main.py', 'r') as file:
        content = file.read()
    
    # Define patterns to match the menu-related endpoints
    patterns = [
        r'# API endpoint to get menu items by outlet.*?def get_menu_by_outlet.*?}\), 500\n',
        r'# API endpoint to add a menu item.*?def add_menu_item.*?}\), 500\n',
        r'# API endpoint to update a menu item.*?def update_menu_item.*?}\), 500\n',
        r'# API endpoint to delete a menu item.*?def delete_menu_item.*?}\), 500\n'
    ]
    
    # Remove each pattern
    for pattern in patterns:
        content = re.sub(pattern, '', content, flags=re.DOTALL)
    
    # Write the updated content back to main.py
    with open('main.py', 'w') as file:
        file.write(content)
    
    print("Menu endpoints removed from main.py")

if __name__ == "__main__":
    remove_menu_endpoints()
