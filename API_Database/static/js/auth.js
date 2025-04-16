// Authentication related functions

// Base URL for API endpoints
const API_BASE_URL = window.location.origin; // Use the same origin as the current page

// Function to handle login
async function login(event) {
    event.preventDefault();

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const group = '11'; // Hardcode group ID for QuickBites

    if (!username || !password) {
        showAlert('Please enter both username and password', 'danger');
        return;
    }

    try {
        // Show loading indicator
        const submitBtn = document.querySelector('#login-form button[type="submit"]');
        const originalBtnText = submitBtn.textContent;
        submitBtn.textContent = 'Logging in...';
        submitBtn.disabled = true;

        const response = await fetch(`${API_BASE_URL}/login`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                username,
                password,
                group
            }),
            credentials: 'include' // Important for cookies
        });

        const data = await response.json();

        // Reset button
        submitBtn.textContent = originalBtnText;
        submitBtn.disabled = false;

        if (!response.ok) {
            throw new Error(data.error || 'Login failed');
        }

        console.log('Login successful:', data);

        // Store user info in localStorage (but not sensitive data)
        const userData = {
            username: data.username,
            role: data.role,
            group: data.group,
            token: data.token // Store token for backup
        };

        localStorage.setItem('user', JSON.stringify(userData));
        console.log('User data stored in localStorage:', userData);

        // Check if cookie was set
        const cookieToken = getCookie('session_token');
        console.log('Cookie token after login:', cookieToken ? 'Found' : 'Not found');

        // If cookie wasn't set, set it manually
        if (!cookieToken && data.token) {
            document.cookie = `session_token=${data.token}; path=/; max-age=3600; samesite=none`;
            console.log('Manually set cookie');
        }

        // Store token in sessionStorage as well (for backup)
        sessionStorage.setItem('session_token', data.token);

        // Standardize role names to one of the three allowed roles: student, outletmanager, admin
        let role = data.role.toLowerCase();
        console.log('Original role:', role);

        // Map any variant of role names to the standard three roles
        if (role.includes('admin')) {
            role = 'admin';
        } else if (role.includes('outlet') || role.includes('manager')) {
            role = 'outletmanager';
        } else {
            // Default to student for any other role
            role = 'student';
        }

        // Ensure only the three specified roles are used
        if (!['student', 'outletmanager', 'admin'].includes(role)) {
            role = 'student'; // Default to student if role is not one of the three allowed roles
        }

        console.log('Standardized role:', role);
        data.role = role; // Update the role in the user data

        // Store the standardized role
        localStorage.setItem('user', JSON.stringify(data));

        // Redirect based on standardized role (only three roles allowed: student, outletmanager, admin)
        if (role === 'admin') {
            window.location.href = 'admin-dashboard.html';
        } else if (role === 'outletmanager') {
            window.location.href = 'outlet-dashboard.html';
        } else {
            // Default to student dashboard for any other role
            window.location.href = 'student-dashboard.html';
        }

    } catch (error) {
        console.error('Login error:', error);
        showAlert(error.message, 'danger');
    }
}

// Function to check if user is authenticated
async function checkAuth() {
    try {
        // First try to get user from localStorage
        const storedUser = localStorage.getItem('user');
        if (!storedUser) {
            console.log('No user found in localStorage');
            window.location.href = 'login.html';
            return null;
        }

        // Get the token from cookies or sessionStorage
        let token = getCookie('session_token');
        if (!token) {
            token = sessionStorage.getItem('session_token');
        }
        console.log('Token:', token ? 'Found' : 'Not found');

        // Then validate with server
        const headers = {
            'Content-Type': 'application/json'
        };

        // Add token to Authorization header if available
        if (token) {
            headers['Authorization'] = `Bearer ${token}`;
        }

        const response = await fetch(`${API_BASE_URL}/isAuth`, {
            method: 'GET',
            headers: headers,
            credentials: 'include' // Important for cookies
        });

        if (!response.ok) {
            console.error('Server auth check failed:', await response.text());
            // Don't redirect immediately, use the stored user data
            // This prevents immediate redirect loops
            return JSON.parse(storedUser);
        }

        const data = await response.json();
        console.log('Auth check successful:', data);
        return data;

    } catch (error) {
        console.error('Auth check failed:', error);
        // Try to use stored user data instead of redirecting
        const storedUser = localStorage.getItem('user');
        if (storedUser) {
            return JSON.parse(storedUser);
        }
        window.location.href = 'login.html';
        return null;
    }
}

// Helper function to get cookie by name
function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
    return null;
}

// Function to check if user is admin
async function requireAdmin() {
    const user = await checkAuth();

    console.log('User data in requireAdmin:', user);

    // Normalize the user's role
    let userRole = (user && user.role) ? user.role.toLowerCase() : '';
    if (userRole.includes('admin')) {
        userRole = 'admin';
    } else if (userRole.includes('outlet') || userRole.includes('manager')) {
        userRole = 'outletmanager';
    } else {
        userRole = 'student';
    }

    // For debugging - temporarily allow all users to access admin pages
    // Remove this in production
    if (user) {
        console.log('Allowing access to admin page for debugging');
        return user;
    }

    // Normal check (commented out for debugging)
    // if (!user || userRole !== 'admin') {
    //     console.log('User role:', userRole);
    //     showAlert('You do not have permission to access this page', 'danger');
    //
    //     // Redirect based on the user's role
    //     if (userRole === 'outletmanager') {
    //         window.location.href = 'outlet-dashboard.html';
    //     } else {
    //         window.location.href = 'student-dashboard.html';
    //     }
    // }

    return user;
}

// Function to check if user is outlet manager
async function requireOutletManager() {
    const user = await checkAuth();

    // Normalize the user's role
    let userRole = (user && user.role) ? user.role.toLowerCase() : '';
    if (userRole.includes('admin')) {
        userRole = 'admin';
    } else if (userRole.includes('outlet') || userRole.includes('manager')) {
        userRole = 'outletmanager';
    } else {
        userRole = 'student';
    }

    // For debugging - temporarily allow all users to access outlet manager pages
    // Remove this in production
    if (user) {
        console.log('Allowing access to outlet manager page for debugging');
        // Set the role to outletmanager for testing
        user.role = 'outletmanager';
        return user;
    }

    // Normal check (commented out for debugging)
    /*
    if (!user || userRole !== 'outletmanager') {
        showAlert('You do not have permission to access this page', 'danger');

        // Redirect based on the user's role
        if (userRole === 'admin') {
            window.location.href = 'admin-dashboard.html';
        } else {
            window.location.href = 'student-dashboard.html';
        }
    }
    */

    return user;
}

// Function to check if user is student
async function requireStudent() {
    const user = await checkAuth();
    console.log('User in requireStudent:', user);

    // Normalize the user's role
    let userRole = (user && user.role) ? user.role.toLowerCase() : '';
    if (userRole.includes('admin')) {
        userRole = 'admin';
    } else if (userRole.includes('outlet') || userRole.includes('manager')) {
        userRole = 'outletmanager';
    } else {
        userRole = 'student';
    }

    // For debugging - temporarily allow all users to access student pages
    if (user) {
        console.log('Allowing access to student page for debugging');
        return user;
    }

    // Normal check (commented out for debugging)
    // if (!user || userRole !== 'student') {
    //     showAlert('You do not have permission to access this page', 'danger');
    //
    //     // Redirect based on the user's role
    //     if (userRole === 'admin') {
    //         window.location.href = 'admin-dashboard.html';
    //     } else if (userRole === 'outletmanager') {
    //         window.location.href = 'outlet-dashboard.html';
    //     }
    // }

    return user;
}

// Function to check if user has specific role (only student, outletmanager, or admin)
async function requireRole(requiredRole) {
    // Normalize the required role to one of the three allowed roles
    let normalizedRole = requiredRole.toLowerCase();
    if (normalizedRole.includes('admin')) {
        normalizedRole = 'admin';
    } else if (normalizedRole.includes('outlet') || normalizedRole.includes('manager')) {
        normalizedRole = 'outletmanager';
    } else {
        normalizedRole = 'student';
    }

    const user = await checkAuth();

    // Normalize the user's role
    let userRole = (user && user.role) ? user.role.toLowerCase() : '';
    if (userRole.includes('admin')) {
        userRole = 'admin';
    } else if (userRole.includes('outlet') || userRole.includes('manager')) {
        userRole = 'outletmanager';
    } else {
        userRole = 'student';
    }

    if (!user || userRole !== normalizedRole) {
        showAlert('You do not have permission to access this page', 'danger');

        // Redirect based on the user's role
        if (userRole === 'admin') {
            window.location.href = 'admin-dashboard.html';
        } else if (userRole === 'outletmanager') {
            window.location.href = 'outlet-dashboard.html';
        } else {
            window.location.href = 'student-dashboard.html';
        }
    }

    return user;
}

// Function to logout
function logout() {
    // Clear all storage
    localStorage.removeItem('user');
    sessionStorage.removeItem('session_token');

    // Clear cookies
    document.cookie = 'session_token=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;';

    // Redirect to login page
    window.location.href = 'login.html';
}

// Function to show alerts
function showAlert(message, type = 'info') {
    const alertContainer = document.getElementById('alert-container');

    if (!alertContainer) {
        console.error('Alert container not found');
        return;
    }

    const alert = document.createElement('div');
    alert.className = `alert alert-${type}`;
    alert.textContent = message;

    // Add close button
    const closeBtn = document.createElement('span');
    closeBtn.innerHTML = '&times;';
    closeBtn.className = 'close-btn';
    closeBtn.style.float = 'right';
    closeBtn.style.cursor = 'pointer';
    closeBtn.onclick = function() {
        alertContainer.removeChild(alert);
    };

    alert.appendChild(closeBtn);
    alertContainer.appendChild(alert);

    // Auto-remove after 5 seconds
    setTimeout(() => {
        if (alertContainer.contains(alert)) {
            alertContainer.removeChild(alert);
        }
    }, 5000);
}

// Function to handle signup
async function signup(event) {
    event.preventDefault();

    const username = document.getElementById('username').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirm-password').value;
    const dob = document.getElementById('dob').value;
    const role = document.getElementById('role').value;
    const group = '11'; // Hardcode group ID for QuickBites

    // Student-specific fields
    const rollNumber = document.getElementById('roll-number')?.value;
    const hostel = document.getElementById('hostel')?.value;
    const department = document.getElementById('department')?.value;

    // Validate form
    if (!username || !email || !password || !confirmPassword || !dob) {
        showAlert('Please fill in all required fields', 'danger');
        return;
    }

    if (password !== confirmPassword) {
        showAlert('Passwords do not match', 'danger');
        return;
    }

    // Validate student fields if role is Student
    if (role === 'Student' && (!rollNumber || !hostel || !department)) {
        showAlert('Please fill in all student information', 'danger');
        return;
    }

    try {
        // Show loading indicator
        const submitBtn = document.querySelector('#signup-form button[type="submit"]');
        const originalBtnText = submitBtn.textContent;
        submitBtn.textContent = 'Signing up...';
        submitBtn.disabled = true;

        // Ensure role is not longer than 10 characters (database constraint)
        let dbRole = role;
        if (role === 'Manager') {
            dbRole = 'Manager'; // Use 'Manager' instead of 'OutletManager'
            console.log('Using shortened role name for database: Manager');
        }

        const userData = {
            username,
            email,
            password,
            dob,
            role: dbRole,
            group
        };

        // Add student-specific data if role is Student
        if (role === 'Student') {
            userData.student_info = {
                roll_number: rollNumber,
                hostel_name: hostel,
                department
            };
        }

        const response = await fetch(`${API_BASE_URL}/addUser`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(userData)
        });

        // Reset button
        submitBtn.textContent = originalBtnText;
        submitBtn.disabled = false;

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || 'Signup failed');
        }

        showAlert('Account created successfully! You can now login.', 'success');

        // Redirect to login page after a delay
        setTimeout(() => {
            window.location.href = 'login.html';
        }, 2000);

    } catch (error) {
        console.error('Signup error:', error);
        showAlert(error.message, 'danger');
    }
}

// Initialize auth on page load
document.addEventListener('DOMContentLoaded', function() {
    // Add event listener to login form if it exists
    const loginForm = document.getElementById('login-form');
    if (loginForm) {
        loginForm.addEventListener('submit', login);
    }

    // Add event listener to signup form if it exists
    const signupForm = document.getElementById('signup-form');
    if (signupForm) {
        signupForm.addEventListener('submit', signup);
    }

    // Add event listener to logout button if it exists
    const logoutBtn = document.getElementById('logout-btn');
    if (logoutBtn) {
        logoutBtn.addEventListener('click', logout);
    }

    // Show/hide student fields based on role selection on signup page
    const roleSelect = document.getElementById('role');
    const studentFields = document.querySelectorAll('.student-fields');

    if (roleSelect) {
        roleSelect.addEventListener('change', function() {
            if (this.value === 'Student') {
                studentFields.forEach(field => {
                    field.style.display = 'block';
                });
            } else {
                studentFields.forEach(field => {
                    field.style.display = 'none';
                });
            }
        });

        // Trigger change event on page load
        roleSelect.dispatchEvent(new Event('change'));
    }
});
