from sdk.schemas import Post
from storage.repository import InMemoryPostRepository


def test_save_and_get_post() -> None:
    """Тестирование сохранения и получения поста из хранилища."""
    repo = InMemoryPostRepository()
    test_post = Post(id=1, user_id=1, title="Test", body="Content")

    repo.save(test_post)
    retrieved = repo.get_by_id(1)

    assert retrieved is not None
    assert retrieved.title == "Test"
