import requests
from pydantic import ValidationError
from sdk.exceptions import ApiNetworkError, ApiValidationError
from sdk.schemas import PostSchema


class BaseResource(object):
    """A basic resource with common query logic."""

    def __init__(self, base_url: str) -> None:
        self._base_url = base_url

    def _make_request(self, endpoint: str) -> dict:
        """Internal method for network calls."""
        url = f"{self._base_url}{endpoint}"

        try:
            response = requests.get(url, timeout=10)
        except requests.RequestException as error:
            raise ApiNetworkError(f"Connection failed: {error}") from error

        try:
            response.raise_for_status()
        except requests.RequestException as error:
            raise ApiNetworkError(f"Connection failed: {error}") from error

        return response.json()


class PostResource(BaseResource):
    """A resource for working with posts."""

    def get_all(self) -> list[PostSchema]:
        """Receives and validates all posts."""
        payload = self._make_request("/posts")

        try:
            return [PostSchema.model_validate(mistake) for mistake in payload]
        except ValidationError as error:
            raise ApiValidationError(f"Invalid list format: {error}") from error

    def get_by_id(self, post_id: int) -> PostSchema:
        """Receives and validates one post."""
        payload = self._make_request(f"/posts/{post_id}")

        try:
            return PostSchema.model_validate(payload)
        except ValidationError as error:
            raise ApiValidationError(f"Data corruption for ID {post_id}: {error}") from error


class JsonPlaceholderClient(object):
    """Main SDK client."""

    def __init__(self, base_url: str) -> None:
        """Initialization of resources."""
        self.posts = PostResource(base_url)
