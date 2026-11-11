from faker import Faker
import random

fake = Faker()

def get_create_booking_payload():
    """Generates a dynamic payload for the Create Booking API using Faker."""
    return {
        "firstname": fake.first_name(),
        "lastname": fake.last_name(),
        "totalprice": random.randint(50, 999),
        "depositpaid": fake.boolean(),
        "bookingdates": {
            "checkin": "2026-12-01",
            "checkout": "2026-12-15"
        },
        "additionalneeds": random.choice(["Breakfast", "Late Checkout", "WiFi"])
    }