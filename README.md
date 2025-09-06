# QuickBites - Food Ordering System

This project implements a food ordering system called QuickBites, focusing on connecting project-specific databases to a central database (CIMS), implementing secure APIs with session validation, and setting up role-based access control.

## Project Structure

- `main.py`: Main Flask application with API endpoints
- `session_validator.py`: Session validation middleware
- `database_manager.py`: Database connection and query management
- `member_manager.py`: Member-related operations
- `Login.py`: User authentication
- `UpdateImage.py`: Image upload functionality
- `setup_database.sql`: SQL script to set up required tables

## Features Implemented

### 1. Member Creation and Authentication
- New members are created in the centralized members table
- Corresponding entries are created in the login table with default credentials
- Session tokens are generated and validated securely

### 2. Role-Based Access Control
- Admin users can perform administrative actions
- Regular users are restricted to their own data
- Session validation middleware checks user roles

### 3. Member Deletion with Group Association Checks
- When deleting a member, the system checks for group associations
- If a member is associated with other groups, only the specific group mapping is removed
- If no other associations exist, the member is completely deleted

### 4. Project-Specific Database Tables
- Created tables specific to Group 11's project
- Established proper relationships with centralized tables
- Avoided duplicating data from centralized tables

### 5. Secure API Development
- All API endpoints validate sessions before processing
- Role-based access control is enforced
- Unauthorized modifications are logged and flagged

### 6. Logging Changes to CIMS Database
- All database operations are logged
- Logs include user ID, operation type, and details
- Unauthorized modifications are detected

### 7. Member Portfolio Management
- Members can create and update their portfolios
- Access control restricts viewing based on project membership
- Admin users can view all portfolios

## API Endpoints

### Authentication
- `POST /login`: Authenticate a user and get a session token
- `POST /validateSession`: Validate a session token

### Member Management
- `POST /addUser`: Add a new member (admin only)
- `DELETE /deleteUser`: Delete a member (admin only)

### Portfolio Management
- `GET /portfolio`: Get a member's portfolio
- `POST /portfolio`: Create or update a portfolio

### Image Management
- `POST /updateImage`: Upload a profile image

## Security Features

- Session validation for all API endpoints
- Role-based access control
- Secure token generation with JWT
- Logging of all database operations
- Detection of unauthorized modifications

## Setup and Usage

1. Ensure MySQL is installed and running
2. Run the `setup_database.sql` script to create required tables
3. Start the Flask application with `python main.py`
4. Access the API at `http://localhost:5001`

Working Demonstration : [Link](https://drive.google.com/drive/folders/1c43iRpQfTdOiynji5I7AVUyOovuvAZwu?usp=drive_link)
