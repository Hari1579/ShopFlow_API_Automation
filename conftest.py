import pytest
from utils.api_client import APIClient

@pytest.fixture
def api_client():
    """
    This fixture initializes our custom API Client.
    Any test function that includes 'api_client' as an argument will automatically get this instance.
    """
    client = APIClient()
    return client