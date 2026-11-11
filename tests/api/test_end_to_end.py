from test_data.payloads import get_create_booking_payload

def test_booking_lifecycle(api_client):
    """
    Test Objective: Verify the full lifecycle of a booking.
    Steps: Create -> Extract ID -> Delete -> Verify Deletion (404)
    """
    # 1. CREATE BOOKING
    payload = get_create_booking_payload()
    create_response = api_client.post("/booking", payload=payload)
    assert create_response.status_code == 200
    
    # Extract the booking ID from the response
    booking_id = create_response.json()["bookingid"]
    print(f"\n[Test] Created Booking ID: {booking_id}")

    # 2. DELETE BOOKING (The APIClient will automatically fetch the auth token)
    delete_response = api_client.delete(f"/booking/{booking_id}")
    assert delete_response.status_code == 201, f"Expected 201 Created/Deleted, got {delete_response.status_code}"

    # 3. VERIFY DELETION
    get_response = api_client.get(f"/booking/{booking_id}")
    assert get_response.status_code == 404, "Expected 404 Not Found after deletion"