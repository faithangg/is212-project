import requests

def test_post_job_application():
    # Create a new job listing
    listing_id = 4

    # Create a new staff member
    staff_id = 1

    # Apply for the role
    data = {
        "staff_id": staff_id,
        "listing_id": listing_id
    }
    
    response = requests.post('http://127.0.0.1:5000/staff/apply_for_role', json=data)
    print(response)
    assert response.status_code == 200

test_post_job_application()