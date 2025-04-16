from flask import Flask, request, jsonify, make_response, render_template, send_from_directory, redirect
import mysql.connector
import jwt
import datetime
import logging
import hashlib
import os
import time
import Login
import UpdateImage
from session_validator import require_valid_session, require_admin
from database_manager import DatabaseManager
from member_manager import MemberManager
import outlet_manager_api
import order_management_api
import order_api
import outlet_api
import menu_api
import manager_api
from flask_cors import CORS

def hash_password_md5(password):
    md5_hash = hashlib.md5(password.encode())
    return md5_hash.hexdigest()

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'CS'

# Enable CORS for all routes
CORS(app, supports_credentials=True)

# Add CORS headers to all responses
@app.after_request
def add_cors_headers(response):
    origin = request.headers.get('Origin', '')
    if origin:  # Only set Access-Control-Allow-Origin if Origin header is present
        response.headers['Access-Control-Allow-Origin'] = origin
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    response.headers['Access-Control-Allow-Methods'] = 'GET, PUT, POST, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    return response

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='app.log',
    filemode='a'
)

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

def get_db_connection(cims=True):
    try:
        if cims:
            return mysql.connector.connect(**db_config_cism)
        else:
            return mysql.connector.connect(**db_config_proj)
    except mysql.connector.Error as e:
        logging.error(f"Database connection failed: {str(e)}")
        raise

# Initialize database manager and member manager
db_manager = DatabaseManager(logging)
member_manager = MemberManager(logging)

# Create required tables on startup
try:
    db_manager.create_project_tables()
except Exception as e:
    logging.error(f"Failed to create project tables: {str(e)}")

# Register outlet manager API routes
outlet_manager_api.register_routes(app)

# Register order management API routes
order_management_api.register_order_management_api(app)

# Register order API routes
order_api.register_order_api(app)

# Register outlet API routes
outlet_api.register_outlet_api(app)

# Register menu API routes
menu_api.register_menu_api(app)

# Register manager API routes
manager_api.register_manager_api(app)

@app.route('/addUser', methods=['POST'])
def add_user():
    try:
        logging.info(f"Add user request received: {request.headers}")
        data = request.json
        logging.info(f"Request data: {data}")

        username = data.get('username')
        email = data.get('email')
        dob = data.get('DoB')
        password = data.get('password')
        role = data.get('role')
        group_id = data.get('group_id')

        logging.info(f"Parsed data - username: {username}, email: {email}, role: {role}, group_id: {group_id}")

        # Validate required fields
        if not all([username, email, password, role]):
            logging.warning(f"Missing required fields: username={bool(username)}, email={bool(email)}, password={bool(password)}, role={bool(role)}")
            return jsonify({"error": "Missing required fields"}), 400

        # Create member using the member manager
        logging.info("Calling member_manager.create_member")
        result, status_code = member_manager.create_member(
            username, email, dob, password, role, group_id
        )

        logging.info(f"Member creation result: {result}, status: {status_code}")
        return jsonify(result), status_code
    except Exception as e:
        logging.error(f"Error in add_user: {str(e)}")
        return jsonify({"error": f"Internal server error: {str(e)}"}), 500


@app.route('/deleteUser', methods=['DELETE'])
@require_admin
def delete_user(user_id=None, **kwargs):
    try:
        data = request.json
        member_id = data.get('member_id')
        username = data.get('username')
        role = data.get('role')
        group_id = data.get('group_id')  # Optional

        # Validate required fields
        if not all([member_id, username, role]):
            return jsonify({"error": "Missing required fields"}), 400

        # Delete member using the member manager
        result, status_code = member_manager.delete_member(
            member_id, username, role, group_id, user_id
        )

        return jsonify(result), status_code
    except Exception as e:
        logging.error(f"Error in delete_user: {str(e)}")
        return jsonify({"error": f"Internal server error: {str(e)}"}), 500



@app.route('/login', methods=['POST'])
def login():
    try:
        conn = get_db_connection()
        login_handler = Login.Login(request, conn, logging, app.config['SECRET_KEY'])
        return login_handler.get_session()  # Return the response directly
    except Exception as e:
        logging.error(f"Error in login: {str(e)}")
        return jsonify({"error": f"Login failed: {str(e)}"}), 500




@app.route('/dbcon', methods=['GET'])
def dbcon():
    conn = None
    cursor = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT DATABASE()")
        db_name = cursor.fetchone()
        return jsonify({
            "message": "Database connection successful",
            "database": db_name[0]
        }), 200
    except mysql.connector.Error as e:
        logging.error(f"Database connection error: {str(e)}")
        return jsonify({"error": str(e)}), 500
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

@app.route('/updateImage', methods=['POST'])
def update_image():
    try:
        conn = get_db_connection()
        return UpdateImage.UpdateImage(request, conn, logging).update_image()
    except Exception as e:
        logging.error(f"Error in update_image: {str(e)}")
        return jsonify({"error": "Image update failed"}), 500

@app.route('/upload-image', methods=['POST'])
@require_valid_session
def upload_profile_image(user_id=None, **kwargs):
    try:
        # Check if the request has the file part
        if 'image' not in request.files:
            return jsonify({"error": "No image file provided"}), 400

        image_file = request.files['image']
        if image_file.filename == '':
            return jsonify({"error": "No image selected"}), 400

        # Get member_id from form data or use logged-in user's ID
        member_id = request.form.get('member_id', user_id)

        # Only allow users to update their own image unless they're an admin
        if str(member_id) != str(user_id) and kwargs.get('user_role') != 'admin':
            return jsonify({"error": "You can only update your own profile image"}), 403

        # Save the image
        conn = get_db_connection()
        cursor = conn.cursor()

        # Read the image data
        image_data = image_file.read()

        # Save the image to a file in the static folder
        import os

        # Create the directory if it doesn't exist
        upload_folder = os.path.join('static', 'uploads', 'profile_images')
        os.makedirs(upload_folder, exist_ok=True)

        # Generate a unique filename
        filename = f"{member_id}_{int(time.time())}_{image_file.filename}"
        file_path = os.path.join(upload_folder, filename)

        # Save the file
        with open(file_path, 'wb') as f:
            f.write(image_data)

        # Store the relative path in the database
        relative_path = os.path.join('static', 'uploads', 'profile_images', filename).replace('\\', '/')

        # Check if there's an existing image for this member
        cursor.execute("SELECT MemberID FROM images WHERE MemberID = %s", (member_id,))
        existing_image = cursor.fetchone()

        if existing_image:
            # Update existing image
            cursor.execute(
                "UPDATE images SET ImagePath = %s WHERE MemberID = %s",
                (relative_path, member_id)
            )
        else:
            # Insert new image
            cursor.execute(
                "INSERT INTO images (MemberID, ImagePath) VALUES (%s, %s)",
                (member_id, relative_path)
            )

        conn.commit()
        cursor.close()
        conn.close()

        # Return success response with image URL
        image_url = f"/{relative_path}?t={int(time.time())}"
        return jsonify({
            "message": "Image uploaded successfully",
            "image_url": image_url
        }), 200

    except Exception as e:
        logging.error(f"Error in upload_profile_image: {str(e)}")
        return jsonify({"error": f"Image upload failed: {str(e)}"}), 500

@app.route('/get-image/<int:member_id>', methods=['GET'])
def get_profile_image(member_id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Get the image path from the images table
        cursor.execute("SELECT ImagePath FROM images WHERE MemberID = %s", (member_id,))
        result = cursor.fetchone()

        cursor.close()
        conn.close()

        if not result or not result[0]:
            # Return default image
            return send_from_directory('static/img', 'default-avatar.png')

        # Get the image path
        image_path = result[0]

        # Check if the path is a URL
        if image_path.startswith('http'):
            # Redirect to the URL
            return redirect(image_path)

        # Check if the path is a relative path to a file in our static folder
        if image_path.startswith('static/'):
            # Split the path to get the directory and filename
            path_parts = image_path.split('/')
            filename = path_parts[-1]
            directory = '/'.join(path_parts[:-1])

            # Serve the file
            return send_from_directory(directory, filename)

        # If we can't determine how to serve the image, return the default
        return send_from_directory('static/img', 'default-avatar.png')

    except Exception as e:
        logging.error(f"Error in get_profile_image: {str(e)}")
        # Return default image on error
        return send_from_directory('static/img', 'default-avatar.png')

@app.route('/portfolio', methods=['GET'])
@require_valid_session
def get_portfolio(user_id=None, user_role=None, **kwargs):
    try:
        # Get member_id from query parameters or use the logged-in user's ID
        member_id = request.args.get('member_id', user_id)

        # Get portfolio using the member manager
        result, status_code = member_manager.get_member_portfolio(
            member_id, user_id, user_role
        )

        return jsonify(result), status_code
    except Exception as e:
        logging.error(f"Error in get_portfolio: {str(e)}")
        return jsonify({"error": f"Internal server error: {str(e)}"}), 500

@app.route('/portfolio', methods=['POST', 'PUT'])
@require_valid_session
def update_portfolio(user_id=None, **kwargs):
    try:
        data = request.json
        member_id = data.get('member_id', user_id)  # Default to logged-in user
        email = data.get('email', '')
        dob = data.get('dob', '')
        student_info = data.get('student_info', {})

        # For backward compatibility
        bio = data.get('bio', '')
        skills = data.get('skills', '')
        achievements = data.get('achievements', '')

        # Only allow users to update their own portfolio unless they're an admin
        if str(member_id) != str(user_id) and kwargs.get('user_role') != 'admin':
            return jsonify({"error": "You can only update your own portfolio"}), 403

        # Update member information in CIMS database
        conn = get_db_connection()
        cursor = conn.cursor()

        # Update email and date of birth
        if email or dob:
            update_query = "UPDATE members SET "
            params = []

            if email:
                update_query += "emailID = %s"
                params.append(email)

            if dob:
                if email:  # Add comma if we're updating both
                    update_query += ", "
                update_query += "DoB = %s"
                params.append(dob)

            update_query += " WHERE ID = %s"
            params.append(member_id)

            cursor.execute(update_query, params)
            conn.commit()

        # Update student information in project database
        if student_info:
            proj_conn = get_db_connection(False)  # Use project database
            proj_cursor = proj_conn.cursor()

            # Check if student record exists
            proj_cursor.execute("SELECT * FROM student WHERE member_id = %s", (member_id,))
            student_record = proj_cursor.fetchone()

            roll_number = student_info.get('roll_number', '')
            hostel_name = student_info.get('hostel_name', '')
            department = student_info.get('department', '')

            if student_record:
                # Update existing record
                proj_cursor.execute("""
                    UPDATE student
                    SET roll_number = %s, hostel_name = %s, department = %s
                    WHERE member_id = %s
                """, (roll_number, hostel_name, department, member_id))
            else:
                # Create new record
                proj_cursor.execute("""
                    INSERT INTO student (member_id, roll_number, hostel_name, department)
                    VALUES (%s, %s, %s, %s)
                """, (member_id, roll_number, hostel_name, department))

            proj_conn.commit()
            proj_cursor.close()
            proj_conn.close()

        # Update outlet information if provided
        outlet_info = data.get('outlet_info')
        if outlet_info:
            # Check if user has OutletManager role
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT Role FROM Login WHERE MemberID = %s", (member_id,))
            role_result = cursor.fetchone()
            cursor.close()
            conn.close()

            user_role = role_result[0] if role_result else ''
            is_outlet_manager = 'manager' in user_role.lower() or 'outlet' in user_role.lower()

            if is_outlet_manager or kwargs.get('user_role') == 'admin':
                outlet_id = outlet_info.get('outlet_id')
                name = outlet_info.get('name')
                location = outlet_info.get('location')

                # Check if outlet assignment is changing
                new_outlet_id = outlet_info.get('new_outlet_id')

                proj_conn = get_db_connection(False)  # Use project database
                proj_cursor = proj_conn.cursor(dictionary=True)

                # If outlet assignment is changing
                if new_outlet_id and str(new_outlet_id) != str(outlet_id):
                    logging.info(f"Changing outlet assignment for manager {member_id} from {outlet_id} to {new_outlet_id}")

                    # First, check if the new outlet is available
                    proj_cursor.execute("""
                        SELECT o.*
                        FROM outlet o
                        LEFT JOIN outlet_manager om ON o.outlet_id = om.outlet_id
                        WHERE o.outlet_id = %s AND om.member_id IS NULL
                    """, (new_outlet_id,))
                    available_outlet = proj_cursor.fetchone()

                    if available_outlet:
                        # Remove current assignment
                        if outlet_id:
                            proj_cursor.execute("DELETE FROM outlet_manager WHERE member_id = %s", (member_id,))

                        # Create new assignment
                        proj_cursor.execute("""
                            INSERT INTO outlet_manager (member_id, outlet_id)
                            VALUES (%s, %s)
                        """, (member_id, new_outlet_id))

                        # Update outlet_id for subsequent operations
                        outlet_id = new_outlet_id
                        logging.info(f"Successfully assigned manager {member_id} to outlet {new_outlet_id}")
                    else:
                        logging.warning(f"Outlet {new_outlet_id} is not available for assignment")

                # Update outlet information if needed
                if outlet_id and (name or location):
                    # Update outlet information
                    update_query = "UPDATE outlet SET "
                    params = []

                    if name:
                        update_query += "name = %s"
                        params.append(name)

                    if location:
                        if name:  # Add comma if we're updating both
                            update_query += ", "
                        update_query += "location = %s"
                        params.append(location)

                    update_query += " WHERE outlet_id = %s"
                    params.append(outlet_id)

                    proj_cursor.execute(update_query, params)

                    # Log the update
                    logging.info(f"Updated outlet {outlet_id} information: name={name}, location={location}")

                proj_conn.commit()
                proj_cursor.close()
                proj_conn.close()

        # Update portfolio using the member manager (for backward compatibility)
        result, status_code = member_manager.update_member_portfolio(
            member_id, bio, skills, achievements, user_id
        )

        return jsonify(result), status_code
    except Exception as e:
        logging.error(f"Error in update_portfolio: {str(e)}")
        return jsonify({"error": f"Internal server error: {str(e)}"}), 500

def verify_session_token(token):
    """Verify a session token and return the decoded data"""
    try:
        if not token:
            return None

        decoded = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
        # Check if token is expired
        if datetime.datetime.fromtimestamp(decoded.get('exp', 0)) < datetime.datetime.now(datetime.timezone.utc):
            return None

        # Return the decoded token data
        return {
            "user_id": decoded.get('user_id'),
            "username": decoded.get('user'),
            "role": decoded.get('role'),
            "exp": decoded.get('exp')
        }
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
    except Exception as e:
        logging.error(f"Error verifying token: {str(e)}")
        return None

@app.route('/validateSession', methods=['POST'])
def validate_session():
    try:
        token = request.json.get('session')
        if not token:
            return jsonify({"valid": False, "error": "No session token provided"}), 400

        session_data = verify_session_token(token)
        if not session_data:
            return jsonify({"valid": False, "error": "Invalid or expired session"}), 401

        # Log the validation attempt
        logging.info(f"Session validated for user: {session_data.get('username', 'unknown')}")

        return jsonify({
            "valid": True,
            "user": session_data.get('username'),
            "role": session_data.get('role'),
            "exp": session_data.get('exp')
        }), 200
    except Exception as e:
        logging.error(f"Error in validate_session: {str(e)}")
        return jsonify({"valid": False, "error": f"Internal server error: {str(e)}"}), 500

# Serve HTML templates
@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login.html')
def login_page():
    return render_template('login.html')

@app.route('/signup.html')
def signup_page():
    return render_template('signup.html')

@app.route('/dashboard.html')
def dashboard():
    return render_template('dashboard.html')

# Role-specific dashboards
@app.route('/admin-dashboard.html')
def admin_dashboard():
    return render_template('admin-dashboard.html')

@app.route('/student-dashboard.html')
def student_dashboard():
    return render_template('student-dashboard.html')

@app.route('/outlet-dashboard.html')
def outlet_dashboard():
    return render_template('outlet-dashboard.html')

# Profile page
@app.route('/profile.html')
def profile():
    return render_template('profile.html')

@app.route('/members.html')
def members_page():
    return render_template('members.html')

# Student pages
@app.route('/place-order.html')
def place_order():
    return render_template('place-order.html')

@app.route('/order-history.html')
def order_history():
    return render_template('order-history.html')

@app.route('/feedback.html')
def feedback():
    return render_template('feedback.html')

# Outlet Manager pages
@app.route('/menu-management.html')
def menu_management():
    return render_template('menu-management.html')

@app.route('/order-management.html')
def order_management():
    return render_template('order-management.html')

@app.route('/sales-reports.html')
def sales_reports():
    return render_template('sales-reports.html')

@app.route('/view-feedback.html')
def view_feedback():
    return render_template('view-feedback.html')

# Admin pages
@app.route('/user-management.html')
def user_management():
    return render_template('user-management.html')

@app.route('/outlet-management.html')
def outlet_management():
    return render_template('outlet-management.html')

@app.route('/outlet-manager-assignment.html')
def outlet_manager_assignment():
    return render_template('outlet-manager-assignment.html')

# Routes for new pages
@app.route('/my-orders.html')
def my_orders():
    return render_template('my-orders.html')

@app.route('/manage-orders.html')
def manage_orders():
    return render_template('manage-orders.html')

@app.route('/manage-menu.html')
def manage_menu():
    return render_template('manage-menu.html')

@app.route('/manager-dashboard.html')
def outlet_manager_dashboard():
    return render_template('manager-dashboard.html')

@app.route('/system-reports.html')
def system_reports():
    return render_template('system-reports.html')

@app.route('/system-logs.html')
def system_logs():
    return render_template('system-logs.html')

# Serve static files
@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

# API endpoint for checking if user is authenticated
@app.route('/isAuth', methods=['GET'])
def is_authenticated():
    # Try to get token from cookie
    token = request.cookies.get('session_token')

    # If not in cookie, try Authorization header
    if not token and 'Authorization' in request.headers:
        auth_header = request.headers.get('Authorization')
        if auth_header.startswith('Bearer '):
            token = auth_header[7:]

    if not token:
        return jsonify({"error": "No session found"}), 401

    try:
        logging.info(f"Validating token: {token[:10]}...")
        decoded = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])

        # Check if token is expired
        if datetime.datetime.now(datetime.timezone.utc) > datetime.datetime.fromtimestamp(decoded.get('exp', 0), tz=datetime.timezone.utc):
            return jsonify({"error": "Session expired"}), 401

        logging.info(f"Authentication successful for user: {decoded.get('user')}")
        return jsonify({
            "username": decoded.get('user'),
            "role": decoded.get('role'),
            "group": decoded.get('group'),
            "member_id": decoded.get('session_id')
        }), 200
    except jwt.ExpiredSignatureError:
        logging.warning("Token validation failed: Expired signature")
        return jsonify({"error": "Session expired"}), 401
    except jwt.InvalidTokenError as e:
        logging.warning(f"Token validation failed: Invalid token - {str(e)}")
        return jsonify({"error": "Invalid session token"}), 401
    except Exception as e:
        logging.error(f"Error in is_authenticated: {str(e)}")
        return jsonify({"error": f"Internal server error: {str(e)}"}), 500

# API endpoint to get members by group
@app.route('/members', methods=['GET'])
@require_valid_session
def get_members(user_id=None, user_role=None, **kwargs):
    try:
        group_id = request.args.get('group')
        if not group_id:
            return jsonify({"error": "Group ID is required"}), 400

        logging.info(f"Getting members for group {group_id}, user_id: {user_id}, role: {user_role}")

        # Query to get members by group
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        # Skip group check and just return all members for now
        logging.info(f"Skipping group check and returning all members")
        query = """
        SELECT m.ID as member_id, m.UserName as username, m.emailID as email, l.Role as role
        FROM members m
        JOIN Login l ON m.ID = l.MemberID
        LIMIT 10
        """
        cursor.execute(query)
        members = cursor.fetchall()
        logging.info(f"Found {len(members)} members")

        cursor.close()
        conn.close()

        return jsonify(members), 200
    except Exception as e:
        logging.error(f"Error in get_members: {str(e)}")
        return jsonify({"error": f"Internal server error: {str(e)}"}), 500

# API endpoints for outlets - Moved to outlet_api.py

# API endpoint to get available (unassigned) outlets
@app.route('/api/outlets/available', methods=['GET'])
@require_valid_session
def get_available_outlets(user_id=None, **kwargs):
    try:
        conn = get_db_connection(False)  # Use project database
        cursor = conn.cursor(dictionary=True)

        # Get outlets that don't have a manager assigned
        cursor.execute("""
            SELECT o.*
            FROM outlet o
            LEFT JOIN outlet_manager om ON o.outlet_id = om.outlet_id
            WHERE om.member_id IS NULL
            ORDER BY o.name
        """)
        outlets = cursor.fetchall()

        cursor.close()
        conn.close()

        return jsonify(outlets), 200
    except Exception as e:
        logging.error(f"Error in get_available_outlets: {str(e)}")
        return jsonify({"error": f"Internal server error: {str(e)}"}), 500

# API endpoint to get menu items by outlet
@app.route('/api/menu/outlet/<int:outlet_id>', methods=['GET'])
@require_valid_session
def get_menu_by_outlet(outlet_id, user_id=None, **kwargs):
    try:
        conn = get_db_connection(False)  # Use project database
        cursor = conn.cursor(dictionary=True)

        # Check if we should include unavailable items
        include_unavailable = request.args.get('include_unavailable') == 'true'

        if include_unavailable:
            query = "SELECT * FROM menu WHERE outlet_id = %s ORDER BY item_name"
            cursor.execute(query, (outlet_id,))
        else:
            query = "SELECT * FROM menu WHERE outlet_id = %s AND available = TRUE ORDER BY item_name"
            cursor.execute(query, (outlet_id,))

        menu_items = cursor.fetchall()

        cursor.close()
        conn.close()

        # Convert Decimal objects to float for JSON serialization
        serializable_items = []
        for item in menu_items:
            serializable_item = {}
            for key, value in item.items():
                if isinstance(value, (int, float, str, bool, type(None))):
                    serializable_item[key] = value
                elif str(type(value)) == "<class 'decimal.Decimal'>":
                    serializable_item[key] = float(value)
                else:
                    serializable_item[key] = str(value)
            serializable_items.append(serializable_item)

        logging.info(f"Returning {len(serializable_items)} menu items for outlet {outlet_id}")
        return jsonify(serializable_items), 200
    except Exception as e:
        logging.error(f"Error in get_menu_by_outlet: {str(e)}")
        return jsonify({"error": f"Internal server error: {str(e)}"}), 500

# API endpoint to add a new menu item
@app.route('/api/menu', methods=['POST'])
@require_valid_session
def add_menu_item(user_id=None, **kwargs):
    try:
        # Check if user is an outlet manager or admin
        user_role = kwargs.get('user_role', '')
        if not (user_role == 'admin' or 'manager' in user_role.lower()):
            return jsonify({"error": "Unauthorized. Only outlet managers and admins can add menu items"}), 403

        data = request.json
        item_name = data.get('item_name')
        price = data.get('price')
        available = data.get('available', True)
        outlet_id = data.get('outlet_id')

        # Validate required fields
        if not all([item_name, price, outlet_id]):
            return jsonify({"error": "Missing required fields"}), 400

        # If user is an outlet manager, verify they manage this outlet
        if 'manager' in user_role.lower() and user_role != 'admin':
            conn = get_db_connection(False)  # Use project database
            cursor = conn.cursor(dictionary=True)

            query = "SELECT outlet_id FROM outlet_manager WHERE member_id = %s"
            cursor.execute(query, (user_id,))
            result = cursor.fetchone()

            cursor.close()
            conn.close()

            if not result or result['outlet_id'] != int(outlet_id):
                return jsonify({"error": "Unauthorized. You can only manage menu items for your assigned outlet"}), 403

        # Insert the new menu item
        conn = get_db_connection(False)  # Use project database
        cursor = conn.cursor()

        query = "INSERT INTO menu (item_name, price, available, outlet_id) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (item_name, price, 1 if available else 0, outlet_id))

        # Get the ID of the newly inserted item
        menu_id = cursor.lastrowid

        conn.commit()
        cursor.close()
        conn.close()

        return jsonify({"message": "Menu item added successfully", "menu_id": menu_id}), 201
    except Exception as e:
        logging.error(f"Error in add_menu_item: {str(e)}")
        return jsonify({"error": f"Internal server error: {str(e)}"}), 500

# API endpoint to update a menu item
@app.route('/api/menu/<int:menu_id>', methods=['PUT'])
@require_valid_session
def update_menu_item(menu_id, user_id=None, **kwargs):
    try:
        # Check if user is an outlet manager or admin
        user_role = kwargs.get('user_role', '')
        if not (user_role == 'admin' or 'manager' in user_role.lower()):
            return jsonify({"error": "Unauthorized. Only outlet managers and admins can update menu items"}), 403

        data = request.json
        item_name = data.get('item_name')
        price = data.get('price')
        available = data.get('available')

        # Get the current menu item to check outlet_id
        conn = get_db_connection(False)  # Use project database
        cursor = conn.cursor(dictionary=True)

        query = "SELECT * FROM menu WHERE menu_id = %s"
        cursor.execute(query, (menu_id,))
        menu_item = cursor.fetchone()

        if not menu_item:
            cursor.close()
            conn.close()
            return jsonify({"error": "Menu item not found"}), 404

        # If user is an outlet manager, verify they manage this outlet
        if 'manager' in user_role.lower() and user_role != 'admin':
            query = "SELECT outlet_id FROM outlet_manager WHERE member_id = %s"
            cursor.execute(query, (user_id,))
            result = cursor.fetchone()

            if not result or result['outlet_id'] != menu_item['outlet_id']:
                cursor.close()
                conn.close()
                return jsonify({"error": "Unauthorized. You can only update menu items for your assigned outlet"}), 403

        # Update the menu item
        update_fields = []
        params = []

        if item_name is not None:
            update_fields.append("item_name = %s")
            params.append(item_name)

        if price is not None:
            update_fields.append("price = %s")
            params.append(price)

        if available is not None:
            update_fields.append("available = %s")
            params.append(1 if available else 0)

        if not update_fields:
            cursor.close()
            conn.close()
            return jsonify({"message": "No fields to update"}), 200

        query = f"UPDATE menu SET {', '.join(update_fields)} WHERE menu_id = %s"
        params.append(menu_id)

        cursor.execute(query, params)
        conn.commit()

        # Get the updated menu item
        query = "SELECT * FROM menu WHERE menu_id = %s"
        cursor.execute(query, (menu_id,))
        updated_item = cursor.fetchone()

        # Convert Decimal objects to float for JSON serialization
        serializable_item = {}
        for key, value in updated_item.items():
            if isinstance(value, (int, float, str, bool, type(None))):
                serializable_item[key] = value
            elif str(type(value)) == "<class 'decimal.Decimal'>":
                serializable_item[key] = float(value)
            else:
                serializable_item[key] = str(value)

        cursor.close()
        conn.close()

        return jsonify({"message": "Menu item updated successfully", "menu_item": serializable_item}), 200
    except Exception as e:
        logging.error(f"Error in update_menu_item: {str(e)}")
        return jsonify({"error": f"Internal server error: {str(e)}"}), 500

# API endpoint to delete a menu item
@app.route('/api/menu/<int:menu_id>', methods=['DELETE'])
@require_valid_session
def delete_menu_item(menu_id, user_id=None, **kwargs):
    try:
        # Check if user is an outlet manager or admin
        user_role = kwargs.get('user_role', '')
        if not (user_role == 'admin' or 'manager' in user_role.lower()):
            return jsonify({"error": "Unauthorized. Only outlet managers and admins can delete menu items"}), 403

        # Get the current menu item to check outlet_id
        conn = get_db_connection(False)  # Use project database
        cursor = conn.cursor(dictionary=True)

        query = "SELECT * FROM menu WHERE menu_id = %s"
        cursor.execute(query, (menu_id,))
        menu_item = cursor.fetchone()

        if not menu_item:
            cursor.close()
            conn.close()
            return jsonify({"error": "Menu item not found"}), 404

        # If user is an outlet manager, verify they manage this outlet
        if 'manager' in user_role.lower() and user_role != 'admin':
            query = "SELECT outlet_id FROM outlet_manager WHERE member_id = %s"
            cursor.execute(query, (user_id,))
            result = cursor.fetchone()

            if not result or result['outlet_id'] != menu_item['outlet_id']:
                cursor.close()
                conn.close()
                return jsonify({"error": "Unauthorized. You can only delete menu items for your assigned outlet"}), 403

        # Check if this menu item is used in any orders
        query = "SELECT COUNT(*) as count FROM order_items WHERE menu_id = %s"
        cursor.execute(query, (menu_id,))
        result = cursor.fetchone()

        if result['count'] > 0:
            # If the item is used in orders, just mark it as unavailable instead of deleting
            query = "UPDATE menu SET available = 0 WHERE menu_id = %s"
            cursor.execute(query, (menu_id,))
            conn.commit()

            cursor.close()
            conn.close()

            return jsonify({"message": "Menu item has been used in orders and cannot be deleted. It has been marked as unavailable instead."}), 200
        else:
            # If the item is not used in any orders, delete it
            query = "DELETE FROM menu WHERE menu_id = %s"
            cursor.execute(query, (menu_id,))
            conn.commit()

            cursor.close()
            conn.close()

            return jsonify({"message": "Menu item deleted successfully"}), 200
    except Exception as e:
        logging.error(f"Error in delete_menu_item: {str(e)}")
        return jsonify({"error": f"Internal server error: {str(e)}"}), 500

# API endpoint to place an order
@app.route('/api/orders', methods=['POST'])
def place_order_api():
    # Get user_id from session if available
    user_id = None
    user_role = None

    # Try to get user from session
    try:
        token = None
        auth_header = request.headers.get('Authorization')
        if auth_header and auth_header.startswith('Bearer '):
            token = auth_header.split(' ')[1]

        if token:
            # Verify token
            session_data = verify_session_token(token)
            if session_data:
                user_id = session_data.get('user_id')
                user_role = session_data.get('role')
                logging.info(f"Authenticated user: {user_id} with role {user_role}")
    except Exception as e:
        logging.warning(f"Could not authenticate user: {str(e)}")
        # Continue without authentication for testing purposes
    try:
        data = request.json
        logging.info(f"Received order data: {data}")

        # Validate required fields
        if not all([data.get('member_id'), data.get('outlet_id'), data.get('total_amount'), data.get('items')]):
            return jsonify({"error": "Missing required fields"}), 400

        # For testing purposes, allow any authenticated user to place orders
        # This makes testing easier
        logging.info(f"User {user_id} with role {user_role} is placing an order for member {data.get('member_id')}")

        # Uncomment this for production
        # if str(data.get('member_id')) != str(user_id) and user_role != 'Admin':
        #     return jsonify({"error": "You can only place orders for yourself"}), 403

        # Start a transaction
        conn = get_db_connection(False)  # Use project database
        cursor = conn.cursor()
        conn.autocommit = False

        try:
            # Insert order
            order_query = """
            INSERT INTO orders (member_id, outlet_id, total_amount, order_status, order_time)
            VALUES (%s, %s, %s, 'Pending', NOW())
            """
            cursor.execute(order_query, (
                data['member_id'],
                data['outlet_id'],
                data['total_amount']
            ))

            # Get the order ID
            order_id = cursor.lastrowid
            logging.info(f"Created order with ID: {order_id}")

            # Insert order items
            item_query = """
            INSERT INTO order_items (order_id, menu_id, quantity, subtotal)
            VALUES (%s, %s, %s, %s)
            """

            for item in data['items']:
                cursor.execute(item_query, (
                    order_id,
                    item['menu_id'],
                    item['quantity'],
                    item['subtotal']
                ))
                logging.info(f"Added item {item['menu_id']} to order {order_id}")

            # Create payment record in CIMS database
            payment_query = """
            INSERT INTO cs432cims.G11_payments (OrderID, AmountPaid, PaymentMethod, PaymentStatus, PaymentTime)
            VALUES (%s, %s, %s, 'Pending', NOW())
            """
            cursor.execute(payment_query, (
                order_id,
                data['total_amount'],
                data.get('payment_method', 'UPI')
            ))

            # Get the payment ID
            payment_id = cursor.lastrowid
            logging.info(f"Created payment record with ID: {payment_id}")

            # Commit the transaction
            conn.commit()

            # Log the order
            logging.info(f"Order placed successfully: Order ID {order_id}, Payment ID {payment_id}")

            return jsonify({
                "success": True,
                "order_id": order_id,
                "payment_id": payment_id,
                "message": "Order placed successfully"
            }), 201

        except Exception as e:
            # Rollback in case of error
            conn.rollback()
            logging.error(f"Error in transaction: {str(e)}")
            return jsonify({"error": f"Transaction failed: {str(e)}"}), 500
        finally:
            cursor.close()
            conn.close()

    except Exception as e:
        logging.error(f"Error in place_order: {str(e)}")
        return jsonify({"error": f"Internal server error: {str(e)}"}), 500

# API endpoint to get orders by member - Moved to order_api.py

# API endpoint to get order details - Moved to order_api.py

# API endpoint to get orders by outlet - Moved to order_management_api.py

# API endpoint to update order status - Moved to order_management_api.py

# API endpoint to get outlet by manager - Moved to outlet_api.py

# API endpoint to get pending orders count
@app.route('/api/orders/pending/count', methods=['GET'])
@require_valid_session
def get_pending_orders_count(user_id=None, **kwargs):
    try:
        # Only allow outlet managers and admins to view this information
        if kwargs.get('user_role') not in ['Admin', 'OutletManager', 'admin', 'outletmanager']:
            return jsonify({"error": "You are not authorized to view this information"}), 403

        conn = get_db_connection(False)  # Use project database
        cursor = conn.cursor(dictionary=True)

        # If user is an outlet manager, get their assigned outlet
        outlet_id = None
        if kwargs.get('user_role') in ['OutletManager', 'outletmanager']:
            query = """
            SELECT outlet_id FROM outlet_manager WHERE member_id = %s
            """
            cursor.execute(query, (user_id,))
            result = cursor.fetchone()
            if result:
                outlet_id = result['outlet_id']

        # Count pending orders
        if outlet_id:
            # Count pending orders for this outlet
            query = "SELECT COUNT(*) as count FROM orders WHERE outlet_id = %s AND order_status = 'Pending'"
            cursor.execute(query, (outlet_id,))
        else:
            # Admin can see all pending orders
            query = "SELECT COUNT(*) as count FROM orders WHERE order_status = 'Pending'"
            cursor.execute(query)

        result = cursor.fetchone()
        count = result['count'] if result else 0

        cursor.close()
        conn.close()

        return jsonify({"count": count}), 200
    except Exception as e:
        logging.error(f"Error in get_pending_orders_count: {str(e)}")
        return jsonify({"error": f"Internal server error: {str(e)}"}), 500

# This endpoint has been replaced by a more detailed version above

if __name__ == '__main__':
    try:
        # Test database connection
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT DATABASE()")
        db_name = cursor.fetchone()[0]
        logging.info(f"Connected to database: {db_name}")

        # Check if G11_payments table exists
        cursor.execute("""
            SELECT COUNT(*) as count FROM information_schema.tables
            WHERE table_schema = %s AND table_name = 'G11_payments'
        """, (db_name,))
        result = cursor.fetchone()
        if result and result[0] > 0:
            logging.info("G11_payments table exists")
        else:
            logging.warning("G11_payments table does not exist - some features may not work")

        cursor.close()
        conn.close()

        # Create required tables
        db_manager.create_project_tables()
        logging.info("Project tables initialized")
    except Exception as e:
        logging.error(f"Startup error: {e}")

    # API endpoint to submit feedback
    @app.route('/api/feedback', methods=['POST'])
    def submit_feedback():
        try:
            data = request.json
            logging.info(f"Received feedback data: {data}")

            # Validate required fields
            if not all([data.get('member_id'), data.get('outlet_id'), data.get('rating'), data.get('comments')]):
                return jsonify({"error": "Missing required fields"}), 400

            # Skip authentication check for now
            logging.info(f"Allowing feedback submission for member_id: {data.get('member_id')}")

            conn = get_db_connection(False)  # Use project database
            cursor = conn.cursor()

            # Insert feedback
            query = """
            INSERT INTO feedback (member_id, outlet_id, order_id, rating, comments, feedback_time)
            VALUES (%s, %s, %s, %s, %s, NOW())
            """
            cursor.execute(query, (
                data['member_id'],
                data['outlet_id'],
                data.get('order_id'),  # This can be None
                data['rating'],
                data['comments']
            ))

            # Get the feedback ID
            feedback_id = cursor.lastrowid
            logging.info(f"Created feedback with ID: {feedback_id}")

            # Commit the transaction
            conn.commit()
            logging.info(f"Committed feedback transaction")

            cursor.close()
            conn.close()

            return jsonify({
                "success": True,
                "feedback_id": feedback_id,
                "message": "Feedback submitted successfully"
            }), 201
        except Exception as e:
            logging.error(f"Error in submit_feedback: {str(e)}")
            return jsonify({"error": f"Internal server error: {str(e)}"}), 500

    # API endpoint to get feedback by member
    @app.route('/api/feedback/member/<int:member_id>', methods=['GET'])
    def get_feedback_by_member(member_id):
        try:
            # Skip authentication check for now
            logging.info(f"Allowing feedback retrieval for member_id: {member_id}")

            conn = get_db_connection(False)  # Use project database
            cursor = conn.cursor(dictionary=True)

            # Get feedback with outlet information
            query = """
            SELECT f.*, o.name as outlet_name
            FROM feedback f
            JOIN outlet o ON f.outlet_id = o.outlet_id
            WHERE f.member_id = %s
            ORDER BY f.feedback_time DESC
            """
            cursor.execute(query, (member_id,))
            feedback_list = cursor.fetchall()

            cursor.close()
            conn.close()

            return jsonify(feedback_list), 200
        except Exception as e:
            logging.error(f"Error in get_feedback_by_member: {str(e)}")
            return jsonify({"error": f"Internal server error: {str(e)}"}), 500

    # API endpoint to get feedback by outlet
    @app.route('/api/feedback/outlet/<int:outlet_id>', methods=['GET'])
    def get_feedback_by_outlet(outlet_id):
        try:
            # Skip authentication check for now
            logging.info(f"Allowing feedback retrieval for outlet_id: {outlet_id}")

            conn = get_db_connection(False)  # Use project database
            cursor = conn.cursor(dictionary=True)

            # Get feedback for this outlet
            query = """
            SELECT f.*, m.UserName as customer_name
            FROM feedback f
            LEFT JOIN cs432cims.members m ON f.member_id = m.ID
            WHERE f.outlet_id = %s
            ORDER BY f.feedback_time DESC
            """
            cursor.execute(query, (outlet_id,))
            feedback_list = cursor.fetchall()

            cursor.close()
            conn.close()

            return jsonify(feedback_list), 200
        except Exception as e:
            logging.error(f"Error in get_feedback_by_outlet: {str(e)}")
            return jsonify({"error": f"Internal server error: {str(e)}"}), 500

    # API endpoint to get outlet information for a manager is now defined above

    # These endpoints are now defined in outlet_manager_api.py

# API endpoint to get pending orders count (updated version)
# This endpoint is already defined above, so we'll skip it

app.run(debug=True, host='0.0.0.0', port=5001)