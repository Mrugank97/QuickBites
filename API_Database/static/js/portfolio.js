// Portfolio management functions

// Function to normalize role to one of the three allowed roles: student, outletmanager, admin
function normalizeRole(role) {
    if (!role) return 'Student';

    const roleLower = role.toLowerCase();

    if (roleLower.includes('admin')) {
        return 'Admin';
    } else if (roleLower.includes('outlet') || roleLower.includes('manager')) {
        return 'Outlet Manager';
    } else {
        return 'Student';
    }
}

// Function to load portfolio data
async function loadPortfolio(memberId = null) {
    try {
        // Check authentication first
        const user = await checkAuth();
        if (!user) {
            throw new Error('Authentication required');
        }

        // Show loading spinner
        const portfolioContainer = document.getElementById('portfolio-container');
        portfolioContainer.innerHTML = '<div class="spinner"></div>';

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

        // Build URL with optional member ID
        let url = `${API_BASE_URL}/portfolio`;
        if (memberId) {
            url += `?member_id=${memberId}`;
        }

        console.log('Loading portfolio from:', url);

        const response = await fetch(url, {
            method: 'GET',
            headers: headers,
            credentials: 'include'
        });

        if (!response.ok) {
            const errorText = await response.text();
            let errorMessage;
            try {
                const errorData = JSON.parse(errorText);
                errorMessage = errorData.error || 'Failed to load portfolio';
            } catch (e) {
                errorMessage = errorText || 'Failed to load portfolio';
            }
            throw new Error(errorMessage);
        }

        const data = await response.json();
        console.log('Portfolio data loaded:', data);
        displayPortfolio(data);

    } catch (error) {
        console.error('Error loading portfolio:', error);
        document.getElementById('portfolio-container').innerHTML = `
            <div class="alert alert-danger">
                Error loading portfolio: ${error.message}
            </div>
        `;
    }
}

// Function to display portfolio data
async function displayPortfolio(data) {
    const portfolioContainer = document.getElementById('portfolio-container');

    // Get current user from localStorage
    const currentUser = JSON.parse(localStorage.getItem('user'));
    const isOwnProfile = currentUser && currentUser.username === data.username;
    const isAdmin = currentUser && currentUser.role === 'admin';

    // Determine if user is an outlet manager
    const normalizedRole = normalizeRole(data.role);
    const isOutletManager = normalizedRole === 'Outlet Manager';

    // If user is an outlet manager, fetch outlet information
    let outletInfo = null;
    if (isOutletManager) {
        try {
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

            const response = await fetch(`${API_BASE_URL}/api/outlet/manager/${data.member_id}`, {
                method: 'GET',
                headers: headers,
                credentials: 'include',
                cache: 'no-store' // Add cache-busting to ensure fresh data
            });

            if (response.ok) {
                outletInfo = await response.json();
                console.log('Outlet info loaded:', outletInfo);
            }
        } catch (error) {
            console.error('Error loading outlet information:', error);
        }
    }

    // Create HTML for portfolio
    let html = `
        <div class="profile">
            <div class="profile-sidebar">
                <img src="${data.image || 'static/img/default-avatar.png'}" alt="${data.username}" class="profile-image">
                <div class="profile-info">
                    <h3>${data.username}</h3>
                    <p>${data.email || ''}</p>
                    <p>Role: ${normalizedRole}</p>
                </div>
                ${(isOwnProfile || isAdmin) ? `
                <div class="mt-3">
                    <button id="edit-portfolio-btn" class="btn btn-block">Edit Profile</button>
                </div>` : ''}
            </div>
            <div class="profile-main">
                <div class="profile-section">
                    <h3>Personal Information</h3>
                    <table class="profile-table">
                        <tr>
                            <th>Name:</th>
                            <td>${data.username}</td>
                        </tr>
                        <tr>
                            <th>Email:</th>
                            <td>${data.email || 'Not provided'}</td>
                        </tr>
                        <tr>
                            <th>Date of Birth:</th>
                            <td>${data.date_of_birth ? new Date(data.date_of_birth).toLocaleDateString() : 'Not provided'}</td>
                        </tr>
                        <tr>
                            <th>Role:</th>
                            <td>${normalizedRole}</td>
                        </tr>
                        ${isOutletManager ? `
                        <tr>
                            <th>Outlet Name:</th>
                            <td>${outletInfo ? outletInfo.name : 'Not assigned'}</td>
                        </tr>
                        <tr>
                            <th>Outlet Location:</th>
                            <td>${outletInfo ? outletInfo.location : 'Not available'}</td>
                        </tr>
                        ` : `
                        <tr>
                            <th>Roll Number:</th>
                            <td>${data.student_info ? data.student_info.roll_number || 'Not provided' : 'Not provided'}</td>
                        </tr>
                        <tr>
                            <th>Hostel:</th>
                            <td>${data.student_info ? data.student_info.hostel_name || 'Not provided' : 'Not provided'}</td>
                        </tr>
                        <tr>
                            <th>Department:</th>
                            <td>${data.student_info ? data.student_info.department || 'Not provided' : 'Not provided'}</td>
                        </tr>
                        `}
                    </table>
                </div>
            </div>
        </div>
    `;

    portfolioContainer.innerHTML = html;

    // Add event listener to edit button
    const editBtn = document.getElementById('edit-portfolio-btn');
    if (editBtn) {
        editBtn.addEventListener('click', () => showEditPortfolioForm(data));
    }
}

// Function to show edit portfolio form
async function showEditPortfolioForm(data) {
    const portfolioContainer = document.getElementById('portfolio-container');

    // Determine if user is an outlet manager
    const normalizedRole = normalizeRole(data.role);
    const isOutletManager = normalizedRole === 'Outlet Manager';

    // If user is an outlet manager, fetch outlet information and available outlets
    let outletInfo = null;
    let availableOutlets = [];

    if (isOutletManager) {
        try {
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

            // Fetch current outlet assignment
            const outletResponse = await fetch(`${API_BASE_URL}/api/outlet/manager/${data.member_id}`, {
                method: 'GET',
                headers: headers,
                credentials: 'include',
                cache: 'no-store' // Add cache-busting to ensure fresh data
            });

            if (outletResponse.ok) {
                outletInfo = await outletResponse.json();
                console.log('Outlet info loaded for edit form:', outletInfo);
            }

            // Fetch all outlets with assignment information
            const allOutletsResponse = await fetch(`${API_BASE_URL}/api/outlets?include_assignments=true`, {
                method: 'GET',
                headers: headers,
                credentials: 'include',
                cache: 'no-store' // Add cache-busting to ensure fresh data
            });

            if (allOutletsResponse.ok) {
                const allOutlets = await allOutletsResponse.json();
                console.log('All outlets loaded:', allOutlets);

                // Filter to get unassigned outlets or the current outlet
                availableOutlets = allOutlets.filter(outlet =>
                    !outlet.assigned ||
                    (outletInfo && outlet.outlet_id === outletInfo.outlet_id)
                );

                console.log('Available outlets:', availableOutlets);
            }

            // Also fetch specifically available outlets as a backup
            const availableResponse = await fetch(`${API_BASE_URL}/api/outlets/available`, {
                method: 'GET',
                headers: headers,
                credentials: 'include',
                cache: 'no-store' // Add cache-busting to ensure fresh data
            });

            if (availableResponse.ok) {
                const unassignedOutlets = await availableResponse.json();
                console.log('Unassigned outlets loaded:', unassignedOutlets);

                // Merge with available outlets if not already included
                for (const outlet of unassignedOutlets) {
                    if (!availableOutlets.some(o => o.outlet_id === outlet.outlet_id)) {
                        availableOutlets.push(outlet);
                    }
                }
            }
        } catch (error) {
            console.error('Error loading outlet information for edit form:', error);
        }
    }

    const html = `
        <div class="form-container">
            <h2 class="form-title">Edit Profile</h2>
            <form id="edit-portfolio-form" enctype="multipart/form-data">
                <input type="hidden" id="member-id" value="${data.member_id}">

                <div class="form-group text-center">
                    <div class="profile-image-container">
                        <img src="${data.image || 'static/img/default-avatar.png'}" alt="${data.username}" class="edit-profile-image" id="profile-image-preview">
                        <div class="image-upload-overlay">
                            <i class="fas fa-camera"></i>
                            <span>Change Photo</span>
                        </div>
                    </div>
                    <input type="file" id="profile-image" class="form-control-file" accept="image/*" style="display: none;" />
                    <button type="button" id="upload-image-btn" class="btn btn-sm mt-2">Upload New Image</button>
                </div>

                <div class="form-group">
                    <label for="email">Email</label>
                    <input type="email" id="email" class="form-control" value="${data.email || ''}" />
                </div>

                <div class="form-group">
                    <label for="dob">Date of Birth</label>
                    <input type="date" id="dob" class="form-control" value="${data.date_of_birth ? data.date_of_birth.split('T')[0] : ''}" />
                </div>

                ${isOutletManager ? `
                <div class="form-group">
                    <label for="outlet-select">Assigned Outlet</label>
                    <select id="outlet-select" class="form-control">
                        ${availableOutlets.map(outlet => `
                            <option value="${outlet.outlet_id}" ${outletInfo && outlet.outlet_id === outletInfo.outlet_id ? 'selected' : ''}>
                                ${outlet.name} (${outlet.location || 'No location'})
                            </option>
                        `).join('')}
                    </select>
                    <small class="form-text text-muted">Select the outlet you want to manage. Each outlet can have only one manager.</small>
                </div>

                <div class="form-group">
                    <label for="outlet-name">Outlet Name</label>
                    <input type="text" id="outlet-name" class="form-control" value="${outletInfo ? outletInfo.name : 'Not assigned'}" />
                    <small class="form-text text-muted">You can update the outlet name here.</small>
                </div>

                <div class="form-group">
                    <label for="outlet-location">Outlet Location</label>
                    <input type="text" id="outlet-location" class="form-control" value="${outletInfo ? outletInfo.location : 'Not available'}" />
                    <small class="form-text text-muted">You can update the outlet location here.</small>
                </div>

                <input type="hidden" id="outlet-id" value="${outletInfo ? outletInfo.outlet_id : ''}" />
                ` : `
                <div class="form-group">
                    <label for="roll-number">Roll Number</label>
                    <input type="text" id="roll-number" class="form-control" value="${data.student_info?.roll_number || ''}" />
                </div>

                <div class="form-group">
                    <label for="hostel">Hostel</label>
                    <input type="text" id="hostel" class="form-control" value="${data.student_info?.hostel_name || ''}" />
                </div>

                <div class="form-group">
                    <label for="department">Department</label>
                    <input type="text" id="department" class="form-control" value="${data.student_info?.department || ''}" />
                </div>
                `}

                <div class="form-group">
                    <button type="submit" class="btn btn-success btn-block">Save Changes</button>
                    <button type="button" id="cancel-edit" class="btn btn-block mt-2">Cancel</button>
                </div>
            </form>
        </div>
    `;

    portfolioContainer.innerHTML = html;

    // Add event listeners
    document.getElementById('edit-portfolio-form').addEventListener('submit', updatePortfolio);
    document.getElementById('cancel-edit').addEventListener('click', () => loadPortfolio(data.member_id));

    // Image upload functionality
    const uploadBtn = document.getElementById('upload-image-btn');
    const fileInput = document.getElementById('profile-image');
    const imagePreview = document.getElementById('profile-image-preview');

    uploadBtn.addEventListener('click', () => {
        fileInput.click();
    });

    fileInput.addEventListener('change', (event) => {
        const file = event.target.files[0];
        if (file) {
            // Preview the image
            const reader = new FileReader();
            reader.onload = (e) => {
                imagePreview.src = e.target.result;
            };
            reader.readAsDataURL(file);

            // Upload the image immediately
            uploadProfileImage(file, data.member_id);
        }
    });
}

// Function to update portfolio
async function updatePortfolio(event) {
    event.preventDefault();

    const memberId = document.getElementById('member-id').value;
    const email = document.getElementById('email').value;
    const dob = document.getElementById('dob').value;

    // Get current user from localStorage to determine role
    const currentUser = JSON.parse(localStorage.getItem('user') || '{}');
    const normalizedRole = normalizeRole(currentUser.role);
    const isOutletManager = normalizedRole === 'Outlet Manager';

    // Prepare the request body
    const requestBody = {
        member_id: memberId,
        email,
        dob
    };

    // Add role-specific fields based on user role
    if (isOutletManager) {
        // Get outlet-specific fields
        const outletName = document.getElementById('outlet-name')?.value;
        const outletLocation = document.getElementById('outlet-location')?.value;
        const outletId = document.getElementById('outlet-id')?.value;

        // Get the selected outlet from dropdown
        const outletSelect = document.getElementById('outlet-select');
        const selectedOutletId = outletSelect ? outletSelect.value : null;

        requestBody.outlet_info = {
            outlet_id: outletId || '',
            name: outletName || '',
            location: outletLocation || ''
        };

        // If the selected outlet is different from the current one, add it to the request
        if (selectedOutletId && selectedOutletId !== outletId) {
            requestBody.outlet_info.new_outlet_id = selectedOutletId;
            console.log(`Changing outlet assignment from ${outletId} to ${selectedOutletId}`);
        }
    } else {
        // Get student-specific fields if they exist
        const rollNumber = document.getElementById('roll-number')?.value;
        const hostel = document.getElementById('hostel')?.value;
        const department = document.getElementById('department')?.value;

        requestBody.student_info = {
            roll_number: rollNumber || '',
            hostel_name: hostel || '',
            department: department || ''
        };
    }

    try {
        const response = await fetch(`${API_BASE_URL}/portfolio`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(requestBody),
            credentials: 'include'
        });

        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.error || 'Failed to update profile');
        }

        showAlert('Profile updated successfully', 'success');
        loadPortfolio(memberId);

    } catch (error) {
        console.error('Error updating profile:', error);
        showAlert(`Error updating profile: ${error.message}`, 'danger');
    }
}

// Function to load recent orders
async function loadRecentOrders(memberId) {
    try {
        const recentOrdersContainer = document.getElementById('recent-orders');

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

        const response = await fetch(`${API_BASE_URL}/api/orders/member/${memberId}?limit=3`, {
            method: 'GET',
            headers: headers,
            credentials: 'include'
        });

        if (!response.ok) {
            throw new Error('Failed to load recent orders');
        }

        const orders = await response.json();

        if (orders.length === 0) {
            recentOrdersContainer.innerHTML = '<p>No orders found. <a href="place-order.html">Place your first order!</a></p>';
            return;
        }

        let html = '<div class="order-list">';

        orders.forEach(order => {
            html += `
                <div class="order-item">
                    <div class="order-header">
                        <h4>Order #${order.order_id}</h4>
                        <span class="order-date">${new Date(order.order_time).toLocaleString()}</span>
                    </div>
                    <div class="order-details">
                        <p><strong>Outlet:</strong> ${order.outlet_name}</p>
                        <p><strong>Total:</strong> ₹${order.total_amount.toFixed(2)}</p>
                        <p><strong>Status:</strong> <span class="status-${order.order_status.toLowerCase()}">${order.order_status}</span></p>
                    </div>
                    <div class="order-actions">
                        <a href="order-details.html?id=${order.order_id}" class="btn btn-sm">View Details</a>
                    </div>
                </div>
            `;
        });

        html += '</div>';
        html += '<div class="mt-3"><a href="order-history.html" class="btn">View All Orders</a></div>';

        recentOrdersContainer.innerHTML = html;

    } catch (error) {
        console.error('Error loading recent orders:', error);
        document.getElementById('recent-orders').innerHTML = `
            <p>Unable to load recent orders. <a href="order-history.html">Try viewing all orders</a>.</p>
        `;
    }
}

// Function to upload profile image
async function uploadProfileImage(file, memberId) {
    try {
        const formData = new FormData();
        formData.append('image', file);
        formData.append('member_id', memberId);

        const response = await fetch(`${API_BASE_URL}/upload-image`, {
            method: 'POST',
            body: formData,
            credentials: 'include'
        });

        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.error || 'Failed to upload image');
        }

        const data = await response.json();
        showAlert('Profile image updated successfully', 'success');

        // Update the image in localStorage if it's the current user
        const currentUser = JSON.parse(localStorage.getItem('user'));
        if (currentUser && currentUser.member_id === memberId) {
            currentUser.image = data.image_url;
            localStorage.setItem('user', JSON.stringify(currentUser));
        }

    } catch (error) {
        console.error('Error uploading image:', error);
        showAlert(`Error uploading image: ${error.message}`, 'danger');
    }
}

// Function to load favorite outlets
async function loadFavoriteOutlets(memberId) {
    try {
        const favoriteOutletsContainer = document.getElementById('favorite-outlets');

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

        // First, get all outlets
        const outletsResponse = await fetch(`${API_BASE_URL}/api/outlets`, {
            method: 'GET',
            headers: headers,
            credentials: 'include'
        });

        if (!outletsResponse.ok) {
            throw new Error('Failed to load outlets');
        }

        const outlets = await outletsResponse.json();

        // Then, get order history to determine favorite outlets
        const ordersResponse = await fetch(`${API_BASE_URL}/api/orders/member/${memberId}`, {
            method: 'GET',
            headers: headers,
            credentials: 'include'
        });

        if (!ordersResponse.ok) {
            throw new Error('Failed to load order history');
        }

        const orders = await ordersResponse.json();

        // Count orders by outlet
        const outletCounts = {};
        orders.forEach(order => {
            if (!outletCounts[order.outlet_id]) {
                outletCounts[order.outlet_id] = 0;
            }
            outletCounts[order.outlet_id]++;
        });

        // Sort outlets by order count
        const favoriteOutlets = outlets
            .filter(outlet => outletCounts[outlet.outlet_id])
            .sort((a, b) => outletCounts[b.outlet_id] - outletCounts[a.outlet_id])
            .slice(0, 3);

        if (favoriteOutlets.length === 0) {
            favoriteOutletsContainer.innerHTML = '<p>No favorite outlets yet. <a href="place-order.html">Start ordering</a> to build your preferences!</p>';
            return;
        }

        let html = '<div class="outlet-list">';

        favoriteOutlets.forEach(outlet => {
            html += `
                <div class="outlet-card">
                    <h4>${outlet.name}</h4>
                    <p>${outlet.location}</p>
                    <p><strong>Orders:</strong> ${outletCounts[outlet.outlet_id]}</p>
                    <div class="outlet-actions">
                        <a href="place-order.html?outlet=${outlet.outlet_id}" class="btn btn-sm btn-success">Order Again</a>
                    </div>
                </div>
            `;
        });

        html += '</div>';

        favoriteOutletsContainer.innerHTML = html;

    } catch (error) {
        console.error('Error loading favorite outlets:', error);
        document.getElementById('favorite-outlets').innerHTML = `
            <p>Unable to load favorite outlets. <a href="place-order.html">Browse all outlets</a>.</p>
        `;
    }
}
