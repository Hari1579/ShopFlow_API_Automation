import os
from dotenv import load_dotenv

# This loads the variables from the .env file if it exists (local runs)
load_dotenv()

class Config:
    BASE_URL = "https://restful-booker.herokuapp.com"
    
    HEADERS = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    # Now we fetch credentials securely from the environment, not hardcoded text
    AUTH_USER = os.getenv("AUTH_USER", "default_user_if_missing")
    AUTH_PASS = os.getenv("AUTH_PASS", "default_pass_if_missing")