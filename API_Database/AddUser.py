import hashlib
from flask import jsonify
import mysql.connector
import psycopg2
import time
import DeleteUser


class AddUser:
    def __init__(self, request, logging, conn):
        self.request = request
        self.logging = logging
        self.conn = conn
        self.data = request.json
        self.success = True
        self.message = ''
        self.member_id = None
        self.status = 200
        self.username = self.data.get('username')
        self.password = self.data.get('password')
        self.role = self.data.get('role')
        self.email = self.data.get('email')
        self.DoB = self.data.get('DoB')
        self.check_keys()
        self.add_user()
        self.add_group_mapping()
        self.create_login()

    def response(self):
        return jsonify(self.message),self.status    

    def check_keys(self):
        keys = ['username','password','role', 'email', 'DoB']
        for key in keys:
            if key not in self.data.keys():
                self.success = False
                self.message = {'error', f'Bad request: {key} not found'}, 400
                return
    
    def add_user(self):
        if not self.success:
            return
        
        cursor = None
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT ID FROM members WHERE UserName = %s", (self.username,))
            existing_user = cursor.fetchone()
            
            if existing_user:
                self.member_id = existing_user[0]
                self.message = {'error': 'User already exists'}
                self.status = 409
                self.success = False
                return
                
            cursor.execute(
                "INSERT INTO members (UserName, emailID, DoB) VALUES (%s, %s, %s)", 
                (self.username, self.email, self.DoB)
            )
            self.conn.commit()
            
            # Get the newly created member ID
            cursor.execute("SELECT ID FROM members WHERE UserName = %s", (self.username,))
            self.member_id = cursor.fetchone()[0]
            
        except mysql.connector.Error as e:
            self.success = False
            self.message = {'error': str(e)}
            self.status = 500
            self.logging.error(f"Database error in add_user: {str(e)}")
        finally:
            if cursor:
                cursor.close()

    def add_group_mapping(self):
        pass

    def get_group_id(self, session_id):
        if not self.success:
            return
        pass

    def create_login(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT ID FROM members WHERE UserName = (%s);", (self.data.get('username'),))
            name = cursor.fetchall()
            # print('login', self.member_id)
            # if user already exists then just update the password and role
            cursor.execute('INSERT INTO Login (MemberID, Password, Role) VALUES (%s, %s, %s)', (self.member_id, hashlib.md5(self.data.get('password', '').encode()).hexdigest(), self.data['role']))
            self.conn.commit()
            self.logging.info(f"User {self.data.get('username')} added to login table")
            self.message = {'message': f"{self.data.get('role', 'user')} added successfully"}
            self.status = 200
        except Exception as e:
            self.message = {'error': f"Error adding user to login table: {str(e)}"}
            self.status = 500
            # print(e)
            self.logging.error(f"Error adding user to login table: {e}")
        finally:
            cursor.close()

    def __del__(self):
        try:
            self.conn.close()
        finally:
            pass