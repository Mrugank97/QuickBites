"""
Script to test the feedback API
"""
import requests
import json
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# API base URL
API_BASE_URL = "http://localhost:5001"

def test_feedback_api():
    """Test the feedback API endpoints"""

    # First, login to get a session token
    login_data = {
        "username": "dd",  # Use a valid username from the database
        "password": "password",  # Try a common password
        "group": "11"
    }

    try:
        # Login
        logging.info("Logging in...")
        login_response = requests.post(
            f"{API_BASE_URL}/login",
            json=login_data
        )

        if not login_response.ok:
            logging.error(f"Login failed: {login_response.status_code} - {login_response.text}")
            return

        login_result = login_response.json()
        logging.info(f"Login successful: {login_result}")

        # Get the session token
        session_token = login_result.get('token')
        if not session_token:
            logging.error("No session token in login response")
            return

        # Set up headers with the session token
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {session_token}"
        }

        # Get the member ID
        member_id = login_result.get('member_id') or login_result.get('session_id')
        if not member_id:
            logging.error("No member ID in login response")
            return

        logging.info(f"Using member ID: {member_id}")

        # Test submitting feedback
        feedback_data = {
            "member_id": member_id,
            "outlet_id": 1,  # Dawat
            "rating": 5,
            "comments": "Test feedback from API test script"
        }

        logging.info(f"Submitting feedback: {feedback_data}")
        feedback_response = requests.post(
            f"{API_BASE_URL}/api/feedback",
            headers=headers,
            json=feedback_data
        )

        if not feedback_response.ok:
            logging.error(f"Feedback submission failed: {feedback_response.status_code} - {feedback_response.text}")
            return

        feedback_result = feedback_response.json()
        logging.info(f"Feedback submitted successfully: {feedback_result}")

        # Test getting feedback by member
        logging.info(f"Getting feedback for member {member_id}...")
        get_feedback_response = requests.get(
            f"{API_BASE_URL}/api/feedback/member/{member_id}",
            headers=headers
        )

        if not get_feedback_response.ok:
            logging.error(f"Getting feedback failed: {get_feedback_response.status_code} - {get_feedback_response.text}")
            return

        feedback_list = get_feedback_response.json()
        logging.info(f"Got {len(feedback_list)} feedback items")
        for feedback in feedback_list:
            logging.info(f"Feedback: {feedback}")

    except Exception as e:
        logging.error(f"Error in test_feedback_api: {str(e)}")

if __name__ == "__main__":
    test_feedback_api()
