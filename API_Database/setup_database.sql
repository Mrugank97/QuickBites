-- CS432 Module 3 - Group 11 Database Setup Script

-- Create the change_logs table to track database changes
CREATE TABLE IF NOT EXISTS change_logs (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id VARCHAR(50) NOT NULL,
    operation VARCHAR(50) NOT NULL,
    table_name VARCHAR(100) NOT NULL,
    details TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create the member_portfolio table for member profiles
CREATE TABLE IF NOT EXISTS member_portfolio (
    portfolio_id INT AUTO_INCREMENT PRIMARY KEY,
    member_id INT NOT NULL,
    bio TEXT,
    skills TEXT,
    achievements TEXT,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE KEY (member_id)
);

-- Create user_roles_mapping table for role-based access control
CREATE TABLE IF NOT EXISTS user_roles_mapping (
    mapping_id INT AUTO_INCREMENT PRIMARY KEY,
    member_id INT NOT NULL,
    role_id INT NOT NULL,
    UNIQUE KEY (member_id, role_id),
    FOREIGN KEY (role_id) REFERENCES roles(id)
);

-- Create orders table for tracking orders
CREATE TABLE IF NOT EXISTS orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    member_id INT NOT NULL,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    total_amount DECIMAL(10,2) NOT NULL,
    status ENUM('Pending', 'Completed', 'Cancelled') DEFAULT 'Pending'
);

-- Create order_items table for order details
CREATE TABLE IF NOT EXISTS order_items (
    item_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    product_name VARCHAR(255) NOT NULL,
    quantity INT NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(order_id)
);

-- Insert default roles if they don't exist
INSERT IGNORE INTO roles (id, role_name) VALUES 
(1, 'admin'),
(2, 'user');

-- Create a view to show member information with their portfolios
CREATE OR REPLACE VIEW member_profiles AS
SELECT 
    m.ID as member_id,
    m.UserName as username,
    m.emailID as email,
    m.DoB as date_of_birth,
    l.Role as role,
    mp.bio,
    mp.skills,
    mp.achievements,
    mp.last_updated
FROM 
    cs432cims.members m
LEFT JOIN 
    cs432cims.Login l ON m.ID = l.MemberID
LEFT JOIN 
    member_portfolio mp ON m.ID = mp.member_id;

-- Create a view to show members in Group 11
CREATE OR REPLACE VIEW group11_members AS
SELECT 
    m.ID as member_id,
    m.UserName as username,
    m.emailID as email,
    l.Role as role
FROM 
    cs432cims.members m
JOIN 
    cs432cims.MemberGroupMapping mgm ON m.ID = mgm.MemberID
JOIN 
    cs432cims.Login l ON m.ID = l.MemberID
WHERE 
    mgm.GroupID = 11;
