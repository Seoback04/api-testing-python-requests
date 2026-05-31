"""
API Client for making HTTP requests.
"""

from typing import Any, Dict, Optional

import requests


class APIClient:
    """Custom API client for HTTP requests."""

    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
        self.session.headers.update(
            {
                "Content-Type": "application/json",
                "User-Agent": "API-Testing-Python/1.0",
            }
        )

    def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> requests.Response:
        url = f"{self.base_url}{endpoint}"
        return self.session.get(url, params=params, timeout=30)

    def post(self, endpoint: str, data: Dict[str, Any]) -> requests.Response:
        url = f"{self.base_url}{endpoint}"
        return self.session.post(url, json=data, timeout=30)

    def put(self, endpoint: str, data: Dict[str, Any]) -> requests.Response:
        url = f"{self.base_url}{endpoint}"
        return self.session.put(url, json=data, timeout=30)

    def delete(self, endpoint: str) -> requests.Response:
        url = f"{self.base_url}{endpoint}"
        return self.session.delete(url, timeout=30)

    def close(self) -> None:
        self.session.close()
