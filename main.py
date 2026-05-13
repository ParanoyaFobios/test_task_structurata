import logging
from sdk.client import JsonPlaceholderClient
from sdk.exceptions import StructurataSdkError
from services.orchestrator import PostOrchestrator
from storage.repository import InMemoryPostRepository


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main() -> None:
    """The main function of launching the application."""
    orchestrator = PostOrchestrator(
        client=JsonPlaceholderClient("https://jsonplaceholder.typicode.com"),
        repository=InMemoryPostRepository(),
    )

    try:
        _run_sync(orchestrator)
    except StructurataSdkError as error:
        logger.error(f"Business application error: {error}")
    except Exception as error:
        logger.critical(f"Unexpected system error: {error}")


def _run_sync(orchestrator: PostOrchestrator) -> None:
    """Solving Jones Complexity problem and evade Python crash report."""
    orchestrator.sync_all_posts()
    post = orchestrator.sync_post_by_id(1)
    logger.info(f"The post has been successfully synchronized: {post.title}")


if __name__ == "__main__":
    main()
