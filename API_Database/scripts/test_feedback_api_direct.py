"""
Script to test the feedback API directly
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
    """Test the feedback API endpoints directly"""
    
    try:
        # Test submitting feedback
        member_id = 1118  # Use a valid member ID
        feedback_data = {
            "member_id": member_id,
            "outlet_id": 3,  # Tea Post
            "rating": 4,
            "comments": "Test feedback from direct API test script"
        }
        
        logging.info(f"Submitting feedback: {feedback_data}")
        feedback_response = requests.post(
            f"{API_BASE_URL}/api/feedback",
            headers={"Content-Type": "application/json"},
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
            f"{API_BASE_URL}/api/feedback/member/{member_id}"
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
