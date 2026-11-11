class Config:
    # We are using Restful Booker as our practice target
    BASE_URL = "https://restful-booker.herokuapp.com"
    
    # We define standard headers here so we don't type them repeatedly
    HEADERS = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }