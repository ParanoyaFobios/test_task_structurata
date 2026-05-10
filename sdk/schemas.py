from dataclasses import dataclass


@dataclass(frozen=True)
class Post(object):
    """Data model for the post."""

    id: int
    user_id: int
    title: str
    body: str
