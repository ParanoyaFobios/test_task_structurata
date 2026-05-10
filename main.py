import logging
from sdk.client import JsonPlaceholderClient
from storage.repository import InMemoryPostRepository
from services.orchestrator import PostOrchestrator


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main() -> None:
    """The main function of launching the application."""
    orchestrator = PostOrchestrator(
        client=JsonPlaceholderClient("https://jsonplaceholder.typicode.com"),
        repository=InMemoryPostRepository(),
    )

    try:
        post = orchestrator.sync_post_by_id(1)
    except Exception as error:
        logger.error(f"An error occurred: {error}")
        return

    logger.info(f"Success: {post.title}")


if __name__ == "__main__":
    main()
