import logging

LOGGER = logging.getLogger(__name__)

logging.basicConfig(
    format="%(asctime)s [%(levelname)s] - <%(name)s> - %(message)s",
    level=logging.INFO,
    handlers=[logging.StreamHandler()],
)

try:
    from dotenv import load_dotenv

    assert load_dotenv(), "No .env file found, have you copied .env.tmpl to .env?"
except ImportError:
    LOGGER.warning("No .env file found, this is expected if running via Docker.")
