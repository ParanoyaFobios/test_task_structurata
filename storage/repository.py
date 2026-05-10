from typing import Dict, Optional
from sdk.schemas import Post


class InMemoryPostRepository(object):
    """A repository for storing posts in RAM."""

    def __init__(self) -> None:
        self._storage: Dict[int, Post] = {}

    def save(self, post: Post) -> None:
        """Saves the post to the dictionary."""
        self._storage[post.id] = post

    def get_by_id(self, post_id: int) -> Optional[Post]:
        """Returns a post by id if it exists.."""
        return self._storage.get(post_id)

    def delete(self, post_id: int) -> None:
        """Deletes a post from storage."""
        self._storage.pop(post_id, None)
