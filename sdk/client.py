import requests
from sdk.schemas import Post


class JsonPlaceholderClient(object):
    """Client for working with the JSONPlaceholder API."""

    def __init__(self, base_url: str) -> None:
        self._base_url = base_url

    def fetch_posts(self) -> list[Post]:
        """Gets a list of all posts."""
        response = requests.get(f"{self._base_url}/posts", timeout=10)
        response.raise_for_status()
        posts_payload = response.json()
        return [
            self._map_post(post_payload)
            for post_payload in posts_payload
        ]

    def fetch_post_by_id(self, post_id: int) -> Post:
        """Gets a single post by its ID."""
        response = requests.get(f"{self._base_url}/posts/{post_id}", timeout=10)
        response.raise_for_status()
        payload = response.json()

        return Post(
            id=payload["id"],
            user_id=payload["userId"],
            title=payload["title"],
            body=payload["body"],
        )

    def _map_post(self, post_payload: dict) -> Post:
        """Helper method for data mapping."""
        return Post(
            id=post_payload["id"],
            user_id=post_payload["userId"],
            title=post_payload["title"],
            body=post_payload["body"],
        )
