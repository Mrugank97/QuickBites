"""
Script to create a student user for testing
"""
import mysql.connector
import hashlib
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Database configuration
db_config_cims = {
    "host": "10.0.116.125",
    "user": "cs432g11",
    "password": "pXqJ5NYz",
    "database": "cs432cims"
}

db_config_proj = {
    "host": "10.0.116.125",
    "user": "cs432g11",
    "password": "pXqJ5NYz",
    "database": "cs432g11"
}

def hash_password_md5(password):
    md5_hash = hashlib.md5(password.encode())
    return md5_hash.hexdigest()

def create_student_user():
    """Create a student user for testing"""
    cims_conn = None
    proj_conn = None
    
    try:
        # Connect to CIMS database
        cims_conn = mysql.connector.connect(**db_config_cims)
        cims_cursor = cims_conn.cursor(dictionary=True)
        
        # Connect to project database
        proj_conn = mysql.connector.connect(**db_config_proj)
        proj_cursor = proj_conn.cursor(dictionary=True)
        
        # Create user in CIMS members table
        username = "student1"
        email = "student1@example.com"
        dob = "2000-01-01"
        
        # Check if user already exists
        cims_cursor.execute("SELECT ID FROM members WHERE UserName = %s", (username,))
        existing_user = cims_cursor.fetchone()
        
        if existing_user:
            member_id = existing_user['ID']
            print(f"User {username} already exists with ID: {member_id}")
        else:
            # Insert into members table
            cims_cursor.execute("""
                INSERT INTO members (UserName, emailID, DoB)
                VALUES (%s, %s, %s)
            """, (username, email, dob))
            cims_conn.commit()
            
            # Get the member ID
            member_id = cims_cursor.lastrowid
            print(f"Created member with ID: {member_id}")
            
            # Insert into MemberGroupMapping table
            cims_cursor.execute("""
                INSERT INTO MemberGroupMapping (MemberID, GroupID)
                VALUES (%s, %s)
            """, (member_id, 11))  # Group 11
            cims_conn.commit()
            print(f"Added member to group 11")
            
            # Insert into Login table
            password = hash_password_md5("password123")
            cims_cursor.execute("""
                INSERT INTO Login (MemberID, Password, Role)
                VALUES (%s, %s, %s)
            """, (member_id, password, "Student"))
            cims_conn.commit()
            print(f"Added login credentials with role: Student")
        
        # Check if student record exists
        proj_cursor.execute("SELECT member_id FROM student WHERE member_id = %s", (member_id,))
        existing_student = proj_cursor.fetchone()
        
        if existing_student:
            print(f"Student record already exists for member ID: {member_id}")
        else:
            # Create student record in project database
            proj_cursor.execute("""
                INSERT INTO student (member_id, roll_number, hostel_name, department)
                VALUES (%s, %s, %s, %s)
            """, (member_id, "S2023001", "H-Hostel", "Computer Science"))
            proj_conn.commit()
            print(f"Created student record for member ID: {member_id}")
            
            # Add user role mapping
            # First, get the role ID for Student
            proj_cursor.execute("SELECT id FROM roles WHERE role_name = 'Student'")
            role = proj_cursor.fetchone()
            
            if role:
                role_id = role['id']
                
                # Check if mapping already exists
                proj_cursor.execute("SELECT mapping_id FROM user_roles_mapping WHERE member_id = %s", (member_id,))
                existing_mapping = proj_cursor.fetchone()
                
                if not existing_mapping:
                    proj_cursor.execute("""
                        INSERT INTO user_roles_mapping (member_id, role_id)
                        VALUES (%s, %s)
                    """, (member_id, role_id))
                    proj_conn.commit()
                    print(f"Added user role mapping for Student role")
                else:
                    print(f"User role mapping already exists")
            else:
                print("Student role not found in roles table")
        
        print("\nStudent user created successfully!")
        print(f"Username: {username}")
        print(f"Password: password123")
        print(f"Role: Student")
        
    except mysql.connector.Error as e:
        logging.error(f"Database error: {str(e)}")
    finally:
        if cims_conn:
            cims_conn.close()
        if proj_conn:
            proj_conn.close()

if __name__ == "__main__":
    create_student_user()
