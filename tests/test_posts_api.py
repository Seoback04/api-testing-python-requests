"""
JSONPlaceholder Posts API tests.
"""


class TestPostsAPI:
    """CRUD + query validation test suite."""

    def test_get_all_posts(self, api_client):
        response = api_client.get("/posts")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) > 0
        assert "userId" in data[0]
        assert "id" in data[0]
        assert "title" in data[0]
        assert "body" in data[0]

    def test_get_single_post(self, api_client):
        post_id = 1
        response = api_client.get(f"/posts/{post_id}")
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == post_id
        assert isinstance(data["userId"], int)
        assert isinstance(data["title"], str)
        assert len(data["title"]) > 0

    def test_create_post(self, api_client, test_post_data):
        response = api_client.post("/posts", test_post_data)
        assert response.status_code == 201
        data = response.json()
        assert data["title"] == test_post_data["title"]
        assert data["body"] == test_post_data["body"]
        assert data["userId"] == test_post_data["userId"]
        assert "id" in data

    def test_update_post(self, api_client, test_post_update):
        response = api_client.put("/posts/1", test_post_update)
        assert response.status_code == 200
        data = response.json()
        assert data["title"] == test_post_update["title"]
        assert data["body"] == test_post_update["body"]

    def test_delete_post(self, api_client):
        response = api_client.delete("/posts/1")
        assert response.status_code == 200

    def test_get_posts_with_query(self, api_client):
        response = api_client.get("/posts", params={"userId": 1, "_limit": 5})
        assert response.status_code == 200
        data = response.json()
        assert len(data) <= 5
        for post in data:
            assert post["userId"] == 1

    def test_post_not_found(self, api_client):
        response = api_client.get("/posts/99999")
        assert response.status_code == 200
        assert response.json() == {}
