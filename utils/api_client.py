import requests
from config.config import Config

class APIClient:
    def __init__(self):
        self.base_url = Config.BASE_URL
        self.headers = Config.HEADERS

    def post(self, endpoint, payload=None):
        """Custom POST method that automatically constructs the full URL and handles headers."""
        url = f"{self.base_url}{endpoint}"
        print(f"\n[APIClient] Executing POST request to: {url}")
        print(f"[APIClient] Payload: {payload}")
        
        response = requests.post(url, json=payload, headers=self.headers)
        
        print(f"[APIClient] Response Status: {response.status_code}")
        return response

    def get(self, endpoint):
        """Custom GET method."""
        url = f"{self.base_url}{endpoint}"
        print(f"\n[APIClient] Executing GET request to: {url}")
        
        response = requests.get(url, headers=self.headers)
        
        print(f"[APIClient] Response Status: {response.status_code}")
        return response