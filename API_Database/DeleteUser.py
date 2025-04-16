# from flask import jsonify
# import mysql.connector

# class DeleteUser:
#     def __init__(self, request, logging, conn):
#         self.request = request
#         self.logging = logging
#         self.conn = conn
#         self.data = request.json
#         self.success = True
#         self.message = ''
#         self.status = 200
#         self.member_id = self.data.get('member_id')
#         self.group_id = self.data.get('group_id')
#         self.username = self.data.get('username')
#         self.role = self.data.get('role')
#         self.check_input()

#     def check_input(self):
#         required_fields = {
#             'member_id': self.member_id,
#             'group_id': self.group_id,
#             'username': self.username,
#             'role': self.role
#         }
        
#         missing_fields = [field for field, value in required_fields.items() if not value]
        
#         if missing_fields:
#             self.success = False
#             self.message = {'error': f'Missing required fields: {", ".join(missing_fields)}'}
#             self.status = 400
#             return False
#         return True

#     def delete_member(self):
#         if not self.success:
#             return jsonify(self.message), self.status

#         cursor = None
#         try:
#             cursor = self.conn.cursor(dictionary=True)
            
#             # First verify if member exists
#             cursor.execute("""
#                 SELECT m.ID, m.UserName, l.Role 
#                 FROM members m 
#                 JOIN Login l ON m.ID = l.MemberID 
#                 WHERE m.ID = %s AND m.UserName = %s AND l.Role = %s
#             """, (self.member_id, self.username, self.role))
            
#             user = cursor.fetchone()
#             if not user:
#                 return jsonify({"error": "User details do not match"}), 400

#             # Check if member has any group mappings
#             cursor.execute("""
#                 SELECT COUNT(*) as mapping_count 
#                 FROM MemberGroupMapping 
#                 WHERE MemberID = %s
#             """, (self.member_id,))
            
#             mapping_result = cursor.fetchone()
            
#             if mapping_result['mapping_count'] == 0:
#                 # Member has no group mappings, proceed with complete deletion
#                 cursor.execute("START TRANSACTION")
#                 cursor.execute("DELETE FROM Login WHERE MemberID = %s", (self.member_id,))
#                 cursor.execute("DELETE FROM members WHERE ID = %s", (self.member_id,))
#                 cursor.execute("COMMIT")
                
#                 self.message = {
#                     'message': f'Member {self.username} (ID: {self.member_id}, Role: {self.role}) completely deleted - No group associations found'
#                 }
#                 self.logging.info(f"Member {self.username} (ID: {self.member_id}, Role: {self.role}) deleted - No group associations")
                
#             else:
#                 # Member has group mappings, proceed with normal flow
#                 cursor.execute("START TRANSACTION")
                
#                 if self.group_id:
#                     # Check other group associations
#                     cursor.execute("""
#                         SELECT COUNT(*) as group_count 
#                         FROM MemberGroupMapping 
#                         WHERE MemberID = %s AND GroupID != %s
#                     """, (self.member_id, self.group_id))
                    
#                     result = cursor.fetchone()
                    
#                     if result['group_count'] > 0:
#                         # Remove specific group mapping
#                         cursor.execute("""
#                             DELETE FROM MemberGroupMapping 
#                             WHERE MemberID = %s AND GroupID = %s
#                         """, (self.member_id, self.group_id))
                        
#                         self.message = {
#                             'message': f'Member {self.username} (ID: {self.member_id}, Role: {self.role}) removed from group {self.group_id}'
#                         }
#                     else:
#                         # Last group, delete everything
#                         cursor.execute("DELETE FROM Login WHERE MemberID = %s", (self.member_id,))
#                         cursor.execute("DELETE FROM MemberGroupMapping WHERE MemberID = %s", (self.member_id,))
#                         cursor.execute("DELETE FROM members WHERE ID = %s", (self.member_id,))
                        
#                         self.message = {
#                             'message': f'Member {self.username} (ID: {self.member_id}, Role: {self.role}) completely deleted - Last group removed'
#                         }
#                 else:
#                     return jsonify({"error": "Group ID required for members with existing group mappings"}), 400
                
#                 cursor.execute("COMMIT")
            
#             self.conn.commit()
#             return jsonify(self.message), self.status

#         except mysql.connector.Error as e:
#             if cursor:
#                 cursor.execute("ROLLBACK")
#             self.logging.error(f"Database error in delete_member: {str(e)}")
#             return jsonify({'error': str(e)}), 500
#         finally:
#             if cursor:
#                 cursor.close()



from flask import jsonify
import mysql.connector

class DeleteUser:
    def __init__(self, request, logging, conn):
        self.request = request
        self.logging = logging
        self.conn = conn
        self.data = request.json
        self.success = True
        self.message = ''
        self.status = 200
        self.member_id = self.data.get('member_id')
        self.username = self.data.get('username')
        self.role = self.data.get('role')
        self.group_id = self.data.get('group_id')  # Optional field
        self.check_input()

    def check_input(self):
        # Required fields check
        required_fields = {
            'member_id': self.member_id,
            'username': self.username,
            'role': self.role
        }
        
        missing_fields = [field for field, value in required_fields.items() if not value]
        
        if missing_fields:
            self.success = False
            self.message = {'error': f'Missing required fields: {", ".join(missing_fields)}'}
            self.status = 400
            return False
        return True

    def delete_member(self):
        if not self.success:
            return jsonify(self.message), self.status

        cursor = None
        try:
            cursor = self.conn.cursor(dictionary=True)
            
            # First verify if member exists
            cursor.execute("""
                SELECT m.ID, m.UserName, l.Role 
                FROM members m 
                JOIN Login l ON m.ID = l.MemberID 
                WHERE m.ID = %s AND m.UserName = %s AND l.Role = %s
            """, (self.member_id, self.username, self.role))
            
            user = cursor.fetchone()
            if not user:
                return jsonify({"error": "User details do not match"}), 400

            # Check if member has any group mappings
            cursor.execute("""
                SELECT COUNT(*) as mapping_count 
                FROM MemberGroupMapping 
                WHERE MemberID = %s
            """, (self.member_id,))
            
            mapping_result = cursor.fetchone()
            
            cursor.execute("START TRANSACTION")
            
            if mapping_result['mapping_count'] == 0:
                # Member has no group mappings, proceed with complete deletion
                cursor.execute("DELETE FROM Login WHERE MemberID = %s", (self.member_id,))
                cursor.execute("DELETE FROM members WHERE ID = %s", (self.member_id,))
                
                self.message = {
                    'message': f'Member {self.username} (ID: {self.member_id}, Role: {self.role}) completely deleted - No group associations found'
                }
                self.logging.info(f"Member {self.username} (ID: {self.member_id}, Role: {self.role}) deleted - No group associations")
            
            else:
                # Member has group mappings
                if self.group_id:
                    # Remove specific group mapping if group_id is provided
                    cursor.execute("""
                        DELETE FROM MemberGroupMapping 
                        WHERE MemberID = %s AND GroupID = %s
                    """, (self.member_id, self.group_id))
                    
                    self.message = {
                        'message': f'Member {self.username} (ID: {self.member_id}, Role: {self.role}) removed from group {self.group_id}'
                    }
                else:
                    # Delete member completely if no group_id specified
                    cursor.execute("DELETE FROM Login WHERE MemberID = %s", (self.member_id,))
                    cursor.execute("DELETE FROM MemberGroupMapping WHERE MemberID = %s", (self.member_id,))
                    cursor.execute("DELETE FROM members WHERE ID = %s", (self.member_id,))
                    
                    self.message = {
                        'message': f'Member {self.username} (ID: {self.member_id}, Role: {self.role}) completely deleted with all group associations'
                    }
            
            cursor.execute("COMMIT")
            self.conn.commit()
            return jsonify(self.message), self.status

        except mysql.connector.Error as e:
            if cursor:
                cursor.execute("ROLLBACK")
            self.logging.error(f"Database error in delete_member: {str(e)}")
            return jsonify({'error': str(e)}), 500
        finally:
            if cursor:
                cursor.close()