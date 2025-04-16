// Admin functions for member management

// Function to load all members (admin only)
async function loadMembers() {
    try {
        // Ensure user is admin
        const user = await requireAdmin();
        if (!user) {
            throw new Error('Authentication required');
        }

        console.log('Loading members for user:', user);

        // Show loading spinner
        const membersContainer = document.getElementById('members-container');
        membersContainer.innerHTML = '<div class="spinner"></div>';

        // Get token from sessionStorage or localStorage as backup
        let token = sessionStorage.getItem('session_token');
        if (!token) {
            const storedUser = JSON.parse(localStorage.getItem('user') || '{}');
            token = storedUser.token;
        }

        console.log('Using token:', token ? 'Found' : 'Not found');

        // Prepare headers
        const headers = {
            'Content-Type': 'application/json'
        };

        // Add token to headers if available
        if (token) {
            headers['Authorization'] = `Bearer ${token}`;
        }

        console.log('Fetching members with headers:', headers);

        // Fetch members from Group 11
        const response = await fetch(`${API_BASE_URL}/members?group=11`, {
            method: 'GET',
            headers: headers,
            credentials: 'include'
        });

        if (!response.ok) {
            const errorText = await response.text();
            let errorMessage;
            try {
                const errorData = JSON.parse(errorText);
                errorMessage = errorData.error || 'Failed to load members';
            } catch (e) {
                errorMessage = errorText || 'Failed to load members';
            }
            throw new Error(errorMessage);
        }

        const data = await response.json();
        displayMembers(data);

    } catch (error) {
        console.error('Error loading members:', error);
        document.getElementById('members-container').innerHTML = `
            <div class="alert alert-danger">
                Error loading members: ${error.message}
            </div>
        `;
    }
}

// Function to display members in a table
function displayMembers(members) {
    const membersContainer = document.getElementById('members-container');

    if (!members || members.length === 0) {
        membersContainer.innerHTML = '<div class="alert alert-info">No members found</div>';
        return;
    }

    let html = `
        <div class="table-container">
            <table class="table">
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Username</th>
                        <th>Email</th>
                        <th>Role</th>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody>
    `;

    members.forEach(member => {
        html += `
            <tr>
                <td>${member.member_id}</td>
                <td>${member.username}</td>
                <td>${member.email || 'N/A'}</td>
                <td>${member.role || 'Member'}</td>
                <td>
                    <button class="btn btn-sm" onclick="viewMemberProfile(${member.member_id})">View</button>
                    <button class="btn btn-danger btn-sm" onclick="confirmDeleteMember(${member.member_id}, '${member.username}', '${member.role}')">Delete</button>
                </td>
            </tr>
        `;
    });

    html += `
                </tbody>
            </table>
        </div>
    `;

    membersContainer.innerHTML = html;
}

// Function to show add member form
function showAddMemberForm() {
    const formContainer = document.getElementById('add-member-container');

    formContainer.innerHTML = `
        <div class="form-container">
            <h2 class="form-title">Add New Member</h2>
            <form id="add-member-form">
                <div class="form-group">
                    <label for="username">Username</label>
                    <input type="text" id="username" class="form-control" required>
                </div>

                <div class="form-group">
                    <label for="email">Email</label>
                    <input type="email" id="email" class="form-control" required>
                </div>

                <div class="form-group">
                    <label for="password">Password</label>
                    <input type="password" id="password" class="form-control" required>
                </div>

                <div class="form-group">
                    <label for="dob">Date of Birth</label>
                    <input type="date" id="dob" class="form-control">
                </div>

                <div class="form-group">
                    <label for="role">Role</label>
                    <select id="role" class="form-control" required>
                        <option value="user">User</option>
                        <option value="admin">Admin</option>
                    </select>
                </div>

                <div class="form-group">
                    <button type="submit" class="btn btn-success btn-block">Add Member</button>
                </div>
            </form>
        </div>
    `;

    // Add event listener to form
    document.getElementById('add-member-form').addEventListener('submit', addMember);
}

// Function to add a new member
async function addMember(event) {
    event.preventDefault();

    const username = document.getElementById('username').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const dob = document.getElementById('dob').value;
    const role = document.getElementById('role').value;

    try {
        // Show loading indicator
        const submitBtn = event.target.querySelector('button[type="submit"]');
        const originalBtnText = submitBtn.textContent;
        submitBtn.textContent = 'Adding...';
        submitBtn.disabled = true;

        // Get token from sessionStorage or localStorage as backup
        let token = sessionStorage.getItem('session_token');
        if (!token) {
            const storedUser = JSON.parse(localStorage.getItem('user') || '{}');
            token = storedUser.token;
        }

        // Prepare headers
        const headers = {
            'Content-Type': 'application/json'
        };

        // Add token to headers if available
        if (token) {
            headers['Authorization'] = `Bearer ${token}`;
        }

        console.log('Adding member with headers:', headers);

        const response = await fetch(`${API_BASE_URL}/addUser`, {
            method: 'POST',
            headers: headers,
            body: JSON.stringify({
                username,
                email,
                password,
                DoB: dob,
                role,
                group_id: 11 // Group 11
            }),
            credentials: 'include'
        });

        // Reset button
        submitBtn.textContent = originalBtnText;
        submitBtn.disabled = false;

        const responseText = await response.text();
        let data;
        try {
            data = JSON.parse(responseText);
        } catch (e) {
            console.error('Failed to parse response:', responseText);
            throw new Error('Invalid response from server');
        }

        if (!response.ok) {
            throw new Error(data.error || 'Failed to add member');
        }

        showAlert('Member added successfully', 'success');

        // Clear form
        document.getElementById('add-member-form').reset();

        // Reload members list
        loadMembers();

    } catch (error) {
        console.error('Error adding member:', error);
        showAlert(`Error adding member: ${error.message}`, 'danger');
    }
}

// Function to confirm member deletion
function confirmDeleteMember(memberId, username, role) {
    if (confirm(`Are you sure you want to delete ${username}?`)) {
        deleteMember(memberId, username, role);
    }
}

// Function to delete a member
async function deleteMember(memberId, username, role) {
    try {
        const response = await fetch(`${API_BASE_URL}/deleteUser`, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                member_id: memberId,
                username,
                role,
                group_id: 11 // Group 11
            }),
            credentials: 'include'
        });

        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.error || 'Failed to delete member');
        }

        showAlert('Member deleted successfully', 'success');

        // Reload members list
        loadMembers();

    } catch (error) {
        console.error('Error deleting member:', error);
        showAlert(`Error deleting member: ${error.message}`, 'danger');
    }
}

// Function to view a member's profile
function viewMemberProfile(memberId) {
    window.location.href = `profile.html?id=${memberId}`;
}

// Initialize admin page
document.addEventListener('DOMContentLoaded', function() {
    // Check if user is admin
    requireAdmin().then(user => {
        if (user) {
            // Load members list
            loadMembers();

            // Add event listener to add member button
            const addMemberBtn = document.getElementById('add-member-btn');
            if (addMemberBtn) {
                addMemberBtn.addEventListener('click', showAddMemberForm);
            }
        }
    });
});
