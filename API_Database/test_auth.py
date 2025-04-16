"""
Test script for authentication flow
"""
import requests
import json

BASE_URL = 'http://localhost:5001'

def test_login():
    """Test the login endpoint"""
    print("Testing login...")
    
    # Login credentials
    credentials = {
        "username": "testuser123",
        "password": "testuser123",
        "group": "11"
    }
    
    # Send login request
    response = requests.post(
        f"{BASE_URL}/login",
        json=credentials
    )
    
    # Print response
    print(f"Status code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    
    # Get cookies
    cookies = response.cookies
    print(f"Cookies: {cookies}")
    
    # Return session token
    return response.json().get('token'), cookies

def test_auth(token, cookies):
    """Test the isAuth endpoint"""
    print("\nTesting authentication...")
    
    # Send auth request with cookies
    response = requests.get(
        f"{BASE_URL}/isAuth",
        cookies=cookies
    )
    
    # Print response
    print(f"Status code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2) if response.ok else response.text}")
    
    # Try with Authorization header
    print("\nTesting authentication with Authorization header...")
    response = requests.get(
        f"{BASE_URL}/isAuth",
        headers={"Authorization": f"Bearer {token}"}
    )
    
    # Print response
    print(f"Status code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2) if response.ok else response.text}")

def test_members(token, cookies):
    """Test the members endpoint"""
    print("\nTesting members endpoint...")
    
    # Send request with cookies
    response = requests.get(
        f"{BASE_URL}/members?group=11",
        cookies=cookies
    )
    
    # Print response
    print(f"Status code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2) if response.ok else response.text}")
    
    # Try with Authorization header
    print("\nTesting members endpoint with Authorization header...")
    response = requests.get(
        f"{BASE_URL}/members?group=11",
        headers={"Authorization": f"Bearer {token}"}
    )
    
    # Print response
    print(f"Status code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2) if response.ok else response.text}")

if __name__ == "__main__":
    token, cookies = test_login()
    if token:
        test_auth(token, cookies)
        test_members(token, cookies)
    else:
        print("Login failed, cannot continue tests")
