import logging
from sdk.client import JsonPlaceholderClient
from sdk.schemas import PostSchema
from sdk.exceptions import ApiNetworkError, ApiValidationError
from storage.repository import InMemoryPostRepository

logger = logging.getLogger(__name__)


class PostOrchestrator(object):
    """A service layer for coordinating post processing. It connects the API client and the data store.."""

    def __init__(
        self,
        client: JsonPlaceholderClient,
        repository: InMemoryPostRepository,
    ) -> None:
        self._client = client
        self._repository = repository

    def sync_post_by_id(self, post_id: int) -> PostSchema:
        try:
            post = self._client.posts.get_by_id(post_id)
        except ApiNetworkError:
            logger.error("Network problem, please try again later.")
            raise
        except ApiValidationError as error:
            logger.error(f"Data parsing error: {error}")
            raise

        self._repository.save(post)
        return post

    def sync_all_posts(self) -> int:
        """Syncs all posts and returns the number of saved posts."""
        try:
            posts = self._client.posts.get_all()
        except (ApiNetworkError, ApiValidationError) as error:
            logger.error(f"Bulk sync failed: {error}")
            raise

        for post in posts:
            self._repository.save(post)
        return len(posts)
