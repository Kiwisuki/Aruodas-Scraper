import logging
from random import random
from time import sleep
from typing import Callable


def exception_handler(func: Callable):
    """Exception handler decorator that logs the exception and returns None."""

    def inner(*args, **kwargs):
        """Inner function that wraps the function and handles the exception."""
        try:
            return func(*args, **kwargs)
        except Exception as exception:
            logging.error(f'Exception in {func.__name__}: {exception}')
            return None

    return inner


def retry(max_retries: int = 3, wait_time: float = 5, random_wait: bool = True):
    """Retry decorator when function fails and raises an exception."""
    if random_wait:
        wait_time = random() * wait_time

    def decorator(func):
        """Decorator that retries the function when it fails."""

        def wrapper(*args, **kwargs):
            """Wrapper that retries the function when it fails."""
            retry_count = 0
            while retry_count < max_retries:
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception as e:
                    retry_count += 1
                    logging.error(
                        f'Exception in {func.__name__}: {e}, retrying in {round(wait_time)} seconds ({retry_count}/{max_retries})'
                    )
                    if retry_count == max_retries:
                        raise e
                    sleep(wait_time)

        return wrapper

    return decorator
