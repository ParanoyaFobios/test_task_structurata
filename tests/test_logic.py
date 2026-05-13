from sdk.schemas import PostSchema
from storage.repository import InMemoryPostRepository
from unittest.mock import MagicMock, patch
import pytest
import requests
from sdk.client import PostResource
from sdk.exceptions import ApiNetworkError


def test_save_and_get_post() -> None:
    """Testing saving and retrieving a post from storage."""
    repo = InMemoryPostRepository()
    test_post = PostSchema(
        id=1,
        userId=1,
        title="Test",
        body="Content"
    )

    repo.save(test_post)
    retrieved = repo.get_by_id(1)

    assert retrieved is not None
    assert retrieved.title == "Test"


@patch("sdk.client.requests.get")
def test_get_by_id_returns_validated_post(mock_get: MagicMock) -> None:
    """SDK maps JSON to a typed model (including API field aliases)."""
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "id": 1,
        "userId": 10,
        "title": "Hello",
        "body": "World",
    }
    post = PostResource("https://example.com").get_by_id(1)
    mock_get.assert_called_once_with("https://example.com/posts/1", timeout=10)
    assert isinstance(post, PostSchema)
    assert post.id == 1
    assert post.user_id == 10
    assert post.title == "Hello"


@patch("sdk.client.requests.get")
def test_get_by_id_request_exception(
    mock_get: MagicMock,
) -> None:
    """Callers can catch one SDK exception type for transport failures."""
    mock_get.side_effect = requests.ConnectionError("refused")
    with pytest.raises(ApiNetworkError) as exc_info:
        PostResource("https://example.com").get_by_id(1)
    assert "Connection failed" in str(exc_info.value)
