import hashlib
import mysql.connector
from flask import jsonify, make_response
import jwt
import datetime

class Login:
    def __init__(self, request, conn, logging, secret_key):
        self.success = False
        self.message = "Initialization failed"
        self.response = None
        self.data = request.json

        self.username = self.data.get('username')
        self.password = self.data.get('password')
        self.group = self.data.get('group')


        self.password = hashlib.md5(self.password.encode()).hexdigest()
        self.conn = conn
        self.logging = logging
        self.secret_key = secret_key
        self.member_id = None
        self.success = True
        self.message = ""
        self.get_member_id()


    def get_member_id(self):
        cursor = self.conn.cursor()
        try:
            cursor.execute("SELECT ID FROM members WHERE UserName = (%s);", (self.username,))
            name = cursor.fetchall()
            if name:
                self.member_id = name[0][0]  # Assuming the first column is the ID
                return
            else:
                self.success = False
                self.message = f"Member {self.username} does not exist"
                self.logging.info(f"Member {self.username} does not exist")
                return
        except mysql.connector.Error as e:
            self.success = False
            self.logging.error(f"MySQL Error: {e}")

    def get_session(self):
        if not self.success:
            return jsonify({"error": self.message}), 401

        cursor = None
        try:
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute("SELECT Password, Role FROM Login WHERE MemberID = %s", (self.member_id,))
            user = cursor.fetchone()

            if not user or self.password != user['Password']:
                self.logging.warning(f"Invalid login attempt for user: {self.username}")
                return jsonify({"error": "Invalid credentials"}), 401

            # Use timezone-aware datetime
            expiry = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=1)

            # Create token with additional security information
            token = jwt.encode({
                "user": self.username,
                "role": user['Role'],
                "exp": int(expiry.timestamp()),  # Convert to integer timestamp
                "group": self.group,
                "session_id": self.member_id,
                "iat": int(datetime.datetime.now(datetime.timezone.utc).timestamp()),  # Issued at time
                "jti": hashlib.md5(f"{self.username}-{datetime.datetime.now(datetime.timezone.utc).timestamp()}".encode()).hexdigest()  # Unique token ID
            }, self.secret_key, algorithm="HS256")

            # Update session in database
            cursor.execute(
                'UPDATE Login SET Session = %s, Expiry = %s WHERE MemberID = %s',
                (token, int(expiry.timestamp()), self.member_id)
            )
            self.conn.commit()

            # Log successful login
            self.logging.info(f"User {self.username} (ID: {self.member_id}, Role: {user['Role']}) logged in successfully")

            # Create response with cookie
            response = make_response(jsonify({
                "message": "Login successful",
                "username": self.username,
                "group": self.group,
                "role": user['Role'],
                "token": token,  # Include token in response
                "expiry": int(expiry.timestamp())
            }))

            # Set cookie with enhanced security
            response.set_cookie(
                'session_token',
                token,
                httponly=False,  # Allow JavaScript access for debugging
                secure=False,  # Set to True in production for HTTPS only
                max_age=3600,  # 1 hour
                samesite='None',  # Allow cross-site requests
                path='/'
            )

            return response

        except mysql.connector.Error as e:
            self.logging.error(f"Database error: {str(e)}")
            return jsonify({"error": "Database error"}), 500
        except Exception as e:
            self.logging.error(f"Login error: {str(e)}")
            return jsonify({"error": "Login failed"}), 500
        finally:
            if cursor:
                cursor.close()