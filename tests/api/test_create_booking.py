import pytest
from test_data.payloads import get_create_booking_payload

def test_create_booking_success(api_client):
    """
    Test Objective: Verify that the API successfully creates a booking 
    when provided with a valid, dynamic JSON payload.
    """
    payload = get_create_booking_payload()
    response = api_client.post("/booking", payload=payload)
    
    assert response.status_code == 200, f"Expected 200 OK, but got {response.status_code}"
    
    response_data = response.json()
    assert "bookingid" in response_data, "Response is missing 'bookingid'"
    assert response_data["booking"]["firstname"] == payload["firstname"], "Firstname mismatch in response"


@pytest.mark.parametrize("missing_field", [
    "firstname", 
    "bookingdates", 
    "totalprice"
])
def test_create_booking_missing_required_fields(api_client, missing_field):
    """
    Test Objective: Verify the API's error handling when required fields are missing.
    Known Bug: The API currently returns a 500 Internal Server Error instead of a 400 Bad Request.
    """
    # 1. Arrange: Get a valid payload, then intentionally delete the required field
    payload = get_create_booking_payload()
    del payload[missing_field]
    
    # 2. Act: Send the bad request
    response = api_client.post("/booking", payload=payload)
    
    # 3. Assert: Validate the known bug behavior (expecting 500)
    assert response.status_code == 500, f"Expected 500 error for missing {missing_field}, but got {response.status_code}"