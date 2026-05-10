from sdk.client import JsonPlaceholderClient
from sdk.schemas import Post
from storage.repository import InMemoryPostRepository


class PostOrchestrator(object):
    """A service layer for coordinating post processing. It connects the API client and the data store.."""

    def __init__(
        self,
        client: JsonPlaceholderClient,
        repository: InMemoryPostRepository,
    ) -> None:
        self._client = client
        self._repository = repository

    def sync_post_by_id(self, post_id: int) -> Post:
        """Downloads a post from the API and saves it to local storage.."""

        post = self._client.fetch_post_by_id(post_id)
        self._repository.save(post)
        return post

    def sync_all_posts(self) -> int:
        """Syncs all posts and returns the number of saved posts."""
        posts = self._client.fetch_posts()
        for post in posts:
            self._repository.save(post)
        return len(posts)
