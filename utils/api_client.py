import requests
from config.config import Config

class APIClient:
    def __init__(self):
        self.base_url = Config.BASE_URL
        self.headers = Config.HEADERS
        self.token = None  # Stores the token once generated

    def get_token(self):
        """Calls the auth endpoint to generate a token and stores it."""
        url = f"{self.base_url}/auth"
        payload = {
            "username": Config.AUTH_USER,
            "password": Config.AUTH_PASS
        }
        response = requests.post(url, json=payload, headers=self.headers)
        if response.status_code == 200:
            self.token = response.json().get("token")
            print(f"\n[APIClient] Token generated successfully: {self.token}")
        else:
            raise Exception(f"Failed to get token. Status: {response.status_code}")

    def get_secure_headers(self):
        """Returns headers including the Cookie authorization required by Restful Booker."""
        if not self.token:
            self.get_token()
        secure_headers = self.headers.copy()
        secure_headers["Cookie"] = f"token={self.token}"
        return secure_headers

    def post(self, endpoint, payload=None):
        url = f"{self.base_url}{endpoint}"
        print(f"\n[APIClient] POST {url}")
        return requests.post(url, json=payload, headers=self.headers)

    def get(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        print(f"\n[APIClient] GET {url}")
        return requests.get(url, headers=self.headers)

    def delete(self, endpoint):
        """Secure DELETE request that requires authentication."""
        url = f"{self.base_url}{endpoint}"
        print(f"\n[APIClient] DELETE {url}")
        # Notice we use get_secure_headers() here instead of self.headers
        return requests.delete(url, headers=self.get_secure_headers())