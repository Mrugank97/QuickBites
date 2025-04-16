"""
QuickBites - Food Ordering System
Run script to start the application
"""

from main import app

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
