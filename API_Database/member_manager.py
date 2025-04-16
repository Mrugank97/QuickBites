import hashlib
from flask import jsonify
import mysql.connector
from database_manager import DatabaseManager

class MemberManager:
    def __init__(self, logging):
        self.logging = logging
        self.db_manager = DatabaseManager(logging)

    def create_member(self, username, email, dob, password, role, group_id=None):
        """
        Create a new member in the centralized database with proper login credentials
        """
        try:
            self.logging.info(f"Creating member: {username}, email: {email}, role: {role}, group_id: {group_id}")

            # Check if username already exists
            existing_user = self.db_manager.execute_cims_query(
                "SELECT ID FROM members WHERE UserName = %s",
                (username,)
            )

            self.logging.info(f"Existing user check result: {existing_user}")

            if existing_user:
                self.logging.warning(f"Username {username} already exists")
                return {"error": "Username already exists"}, 409

            # Insert into members table
            self.db_manager.execute_cims_query(
                "INSERT INTO members (UserName, emailID, DoB) VALUES (%s, %s, %s)",
                (username, email, dob),
                commit=True,
                user_id="SYSTEM",
                operation="INSERT",
                table="members",
                details=f"Created new member: {username}"
            )

            # Get the newly created member ID
            member_result = self.db_manager.execute_cims_query(
                "SELECT ID FROM members WHERE UserName = %s",
                (username,)
            )

            if not member_result:
                return {"error": "Failed to create member"}, 500

            member_id = member_result[0]['ID']

            # Create login entry with default credentials
            hashed_password = hashlib.md5(password.encode()).hexdigest()

            # Ensure role is not longer than 10 characters (database constraint)
            db_role = role
            if role.lower() == 'manager' or role.lower() == 'outletmanager':
                db_role = 'Manager'  # Use 'Manager' instead of 'OutletManager'
                self.logging.info(f"Using shortened role name for database: Manager")

            self.db_manager.execute_cims_query(
                "INSERT INTO Login (MemberID, Password, Role) VALUES (%s, %s, %s)",
                (member_id, hashed_password, db_role),
                commit=True,
                user_id="SYSTEM",
                operation="INSERT",
                table="Login",
                details=f"Created login for member: {username} with role: {db_role}"
            )

            # Add to group mapping if group_id is provided
            if group_id:
                self.db_manager.execute_cims_query(
                    "INSERT INTO MemberGroupMapping (MemberID, GroupID) VALUES (%s, %s)",
                    (member_id, group_id),
                    commit=True,
                    user_id="SYSTEM",
                    operation="INSERT",
                    table="MemberGroupMapping",
                    details=f"Added member {username} to group {group_id}"
                )

            # If role is outlet manager, add to outlet_manager table
            if role.lower() == 'manager' or role.lower() == 'outletmanager':
                try:
                    # Check if outlet_manager table exists in project database
                    outlet_manager_exists = self.db_manager.execute_project_query(
                        """SELECT COUNT(*) as count FROM information_schema.tables
                           WHERE table_schema = 'cs432g11' AND table_name = 'outlet_manager'""",
                        ()
                    )

                    if outlet_manager_exists and outlet_manager_exists[0]['count'] > 0:
                        # Find an outlet without a manager (enforcing one-to-one relationship)
                        unassigned_outlet = self.db_manager.execute_project_query(
                            """
                            SELECT o.outlet_id, o.name
                            FROM outlet o
                            LEFT JOIN outlet_manager om ON o.outlet_id = om.outlet_id
                            WHERE om.member_id IS NULL
                            ORDER BY o.outlet_id
                            LIMIT 1
                            """,
                            ()
                        )

                        if unassigned_outlet and len(unassigned_outlet) > 0:
                            # Found an unassigned outlet
                            outlet_id = unassigned_outlet[0]['outlet_id']
                            outlet_name = unassigned_outlet[0]['name']
                            self.logging.info(f"Found unassigned outlet: {outlet_name} (ID: {outlet_id})")
                        else:
                            # No unassigned outlets, check if we can create a new one
                            self.logging.warning("No unassigned outlets found. All outlets already have managers.")

                            # Get the highest outlet ID
                            max_outlet_id = self.db_manager.execute_project_query(
                                "SELECT MAX(outlet_id) as max_id FROM outlet",
                                ()
                            )

                            next_id = 1
                            if max_outlet_id and max_outlet_id[0]['max_id']:
                                next_id = max_outlet_id[0]['max_id'] + 1

                            # Create a new outlet
                            outlet_name = f"New Outlet {next_id}"
                            self.db_manager.execute_project_query(
                                "INSERT INTO outlet (outlet_id, name, location) VALUES (%s, %s, %s)",
                                (next_id, outlet_name, "Campus"),
                                commit=True,
                                user_id="SYSTEM",
                                operation="INSERT",
                                table="outlet",
                                details=f"Created new outlet: {outlet_name}"
                            )

                            outlet_id = next_id
                            self.logging.info(f"Created new outlet: {outlet_name} (ID: {outlet_id})")

                        # Add to outlet_manager table
                        self.logging.info(f"Assigning manager {username} to outlet {outlet_id}")

                        # Check the structure of the outlet_manager table
                        table_structure = self.db_manager.execute_project_query(
                            "DESCRIBE outlet_manager",
                            ()
                        )

                        # Find the outlet ID column name
                        outlet_id_column = 'outlet_id'
                        for column in table_structure:
                            if 'outlet' in column['Field'].lower():
                                outlet_id_column = column['Field']
                                break

                        self.logging.info(f"Using outlet ID column: {outlet_id_column}")

                        # Add to outlet_manager table with the correct column name and set auto_assigned to true
                        self.db_manager.execute_project_query(
                            f"INSERT INTO outlet_manager (member_id, {outlet_id_column}, auto_assigned) VALUES (%s, %s, %s)",
                            (member_id, outlet_id, True),
                            commit=True,
                            user_id="SYSTEM",
                            operation="INSERT",
                            table="outlet_manager",
                            details=f"Assigned outlet {outlet_id} to manager {username} (automatic assignment)"
                        )
                        self.logging.info(f"Assigned outlet {outlet_id} to manager {username}")
                except Exception as e:
                    self.logging.warning(f"Could not assign outlet to manager: {str(e)}")
                    # Continue without error since this is optional

            return {
                "message": "Member created successfully",
                "member_id": member_id,
                "username": username,
                "role": role
            }, 201

        except mysql.connector.Error as e:
            self.logging.error(f"Database error in create_member: {str(e)}")
            return {"error": str(e)}, 500
        except Exception as e:
            self.logging.error(f"Error in create_member: {str(e)}")
            return {"error": str(e)}, 500

    def delete_member(self, member_id, username, role, group_id=None, user_id=None):
        """
        Delete a member or remove from a specific group based on associations
        """
        try:
            # Verify member exists
            member_exists = self.db_manager.check_member_exists(member_id)
            if not member_exists:
                return {"error": "Member not found"}, 404

            # Get all groups the member is associated with
            member_groups = self.db_manager.get_member_groups(member_id)

            # If group_id is provided, only remove from that group
            if group_id:
                # Check if member is in the specified group
                is_in_group = self.db_manager.check_member_in_group(member_id, group_id)
                if not is_in_group:
                    return {"error": f"Member is not associated with group {group_id}"}, 400

                # Check if member is in other groups
                other_groups = [g for g in member_groups if g['GroupID'] != group_id]

                if other_groups:
                    # Member is in other groups, only remove from specified group
                    self.db_manager.execute_cims_query(
                        "DELETE FROM MemberGroupMapping WHERE MemberID = %s AND GroupID = %s",
                        (member_id, group_id),
                        commit=True,
                        user_id=user_id or "SYSTEM",
                        operation="DELETE",
                        table="MemberGroupMapping",
                        details=f"Removed member {username} from group {group_id}"
                    )

                    return {
                        "message": f"Member {username} removed from group {group_id}",
                        "remaining_groups": [g['GroupID'] for g in other_groups]
                    }, 200
                else:
                    # This is the only group, proceed with complete deletion
                    pass

            # Check if user is an outlet manager and delete from outlet_manager table if needed
            try:
                # Check if the role contains 'manager'
                if 'manager' in role.lower():
                    self.logging.info(f"Checking if member {member_id} is an outlet manager")

                    # Delete from outlet_manager table
                    self.db_manager.execute_project_query(
                        "DELETE FROM outlet_manager WHERE member_id = %s",
                        (member_id,),
                        commit=True,
                        user_id=user_id or "SYSTEM",
                        operation="DELETE",
                        table="outlet_manager",
                        details=f"Deleted outlet manager assignment for: {username}"
                    )
                    self.logging.info(f"Deleted outlet manager assignment for member {member_id}")
            except Exception as e:
                self.logging.warning(f"Error deleting outlet manager assignment: {str(e)}")
                # Continue with deletion even if this fails

            # Delete from Login table
            self.db_manager.execute_cims_query(
                "DELETE FROM Login WHERE MemberID = %s",
                (member_id,),
                commit=True,
                user_id=user_id or "SYSTEM",
                operation="DELETE",
                table="Login",
                details=f"Deleted login for member: {username}"
            )

            # Delete from MemberGroupMapping
            self.db_manager.execute_cims_query(
                "DELETE FROM MemberGroupMapping WHERE MemberID = %s",
                (member_id,),
                commit=True,
                user_id=user_id or "SYSTEM",
                operation="DELETE",
                table="MemberGroupMapping",
                details=f"Deleted all group mappings for member: {username}"
            )

            # Delete from members table
            self.db_manager.execute_cims_query(
                "DELETE FROM members WHERE ID = %s",
                (member_id,),
                commit=True,
                user_id=user_id or "SYSTEM",
                operation="DELETE",
                table="members",
                details=f"Deleted member: {username}"
            )

            return {
                "message": f"Member {username} completely deleted"
            }, 200

        except mysql.connector.Error as e:
            self.logging.error(f"Database error in delete_member: {str(e)}")
            return {"error": str(e)}, 500
        except Exception as e:
            self.logging.error(f"Error in delete_member: {str(e)}")
            return {"error": str(e)}, 500

    def get_member_portfolio(self, member_id, requesting_user_id, requesting_user_role):
        """
        Get a member's portfolio with access control
        """
        try:
            # Check if member exists
            member_exists = self.db_manager.check_member_exists(member_id)
            if not member_exists:
                return {"error": "Member not found"}, 404

            # Get member details
            member_details = self.db_manager.execute_cims_query(
                "SELECT ID, UserName, emailID, DoB FROM members WHERE ID = %s",
                (member_id,)
            )

            if not member_details:
                return {"error": "Member details not found"}, 404

            # Get user role from Login table
            role_info = self.db_manager.execute_cims_query(
                "SELECT Role FROM Login WHERE MemberID = %s",
                (member_id,)
            )

            role = role_info[0]['Role'] if role_info else 'Member'

            # Get member's groups
            member_groups = self.db_manager.get_member_groups(member_id)
            group_ids = [g['GroupID'] for g in member_groups]

            # Get requesting user's groups
            if requesting_user_id != member_id and requesting_user_role != "admin":
                requester_groups = self.db_manager.get_member_groups(requesting_user_id)
                requester_group_ids = [g['GroupID'] for g in requester_groups]

                # Check if they share any groups
                if not any(g in requester_group_ids for g in group_ids):
                    return {"error": "You don't have permission to view this profile"}, 403

            # Get portfolio data from member_portfolio table
            try:
                portfolio = self.db_manager.execute_project_query(
                    "SELECT * FROM member_portfolio WHERE member_id = %s",
                    (member_id,)
                )
            except Exception as e:
                self.logging.warning(f"Error querying member_portfolio: {str(e)}")
                # If there's an error, just create a default portfolio
                portfolio = []

            # If no data found, create a default portfolio
            if not portfolio:
                import datetime
                portfolio = [{
                    'portfolio_id': 0,
                    'member_id': member_id,
                    'bio': f'Default bio for member {member_id}',
                    'skills': f'Default skills for member {member_id}',
                    'achievements': f'Default achievements for member {member_id}',
                    'last_updated': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                }]

            # Get student information if available
            try:
                student_info = self.db_manager.execute_project_query(
                    "SELECT * FROM student WHERE member_id = %s",
                    (member_id,)
                )
            except Exception as e:
                self.logging.warning(f"Error querying student info: {str(e)}")
                student_info = []

            # Get image path if available
            try:
                image_info = self.db_manager.execute_cims_query(
                    "SELECT ImagePath FROM images WHERE MemberID = %s",
                    (member_id,)
                )
                image_path = image_info[0]['ImagePath'] if image_info else None
            except Exception as e:
                self.logging.warning(f"Error querying image info: {str(e)}")
                image_path = None

            # Combine data
            result = {
                "member_id": member_details[0]['ID'],
                "username": member_details[0]['UserName'],
                "email": member_details[0]['emailID'],
                "date_of_birth": member_details[0]['DoB'].strftime('%Y-%m-%d') if member_details[0]['DoB'] else None,
                "role": role,  # Include the role from Login table
                "groups": group_ids,
                "portfolio": portfolio[0] if portfolio else {},
                "student_info": student_info[0] if student_info else None,
                "image": image_path
            }

            return result, 200

        except Exception as e:
            self.logging.error(f"Error in get_member_portfolio: {str(e)}")
            return {"error": str(e)}, 500

    def update_member_portfolio(self, member_id, bio, skills, achievements, user_id):
        """
        Update a member's portfolio
        """
        try:
            # Check if portfolio exists
            try:
                existing_portfolio = self.db_manager.execute_project_query(
                    "SELECT * FROM member_portfolio WHERE member_id = %s",
                    (member_id,)
                )

                if existing_portfolio:
                    # Update existing portfolio
                    self.db_manager.execute_project_query(
                        """
                        UPDATE member_portfolio
                        SET bio = %s, skills = %s, achievements = %s
                        WHERE member_id = %s
                        """,
                        (bio, skills, achievements, member_id),
                        commit=True,
                        user_id=user_id,
                        operation="UPDATE",
                        table="member_portfolio",
                        details=f"Updated portfolio for member ID: {member_id}"
                    )
                    self.logging.info(f"Updated portfolio for member {member_id}")
                else:
                    # Create new portfolio
                    self.db_manager.execute_project_query(
                        """
                        INSERT INTO member_portfolio (member_id, bio, skills, achievements)
                        VALUES (%s, %s, %s, %s)
                        """,
                        (member_id, bio, skills, achievements),
                        commit=True,
                        user_id=user_id,
                        operation="INSERT",
                        table="member_portfolio",
                        details=f"Created portfolio for member ID: {member_id}"
                    )
                    self.logging.info(f"Created portfolio for member {member_id}")
            except Exception as e:
                self.logging.error(f"Error updating portfolio: {str(e)}")
                return {"error": f"Failed to update portfolio: {str(e)}"}, 500

            return {
                "message": "Portfolio updated successfully",
                "member_id": member_id
            }, 200

        except Exception as e:
            self.logging.error(f"Error in update_member_portfolio: {str(e)}")
            return {"error": str(e)}, 500
