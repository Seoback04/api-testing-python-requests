"""
Pytest shared fixtures and setup.
"""

import pytest

from utils.api_client import APIClient


@pytest.fixture(scope="session")
def api_client():
    client = APIClient(base_url="https://jsonplaceholder.typicode.com")
    yield client
    client.close()


@pytest.fixture
def test_post_data():
    return {
        "title": "Test Post from Python",
        "body": "This is a test post created with Python requests",
        "userId": 1,
    }


@pytest.fixture
def test_post_update():
    return {
        "title": "Updated Title",
        "body": "Updated body content",
        "userId": 1,
    }
