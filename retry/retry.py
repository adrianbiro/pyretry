import logging
import time
from functools import wraps


def retry(
    times: int,
    exceptions: tuple, #https://peps.python.org/pep-0484/#exceptions
    sleep: bool | int | float = False,
    increment_sleep: bool | int | float = False,
):
    def decorator(func):
        @wraps(func)
        def newfn(*args, **kwargs):
            nonlocal sleep, increment_sleep, exceptions
            attempt = 0
            while attempt < times:
                try:
                    return func(*args, **kwargs)
                except exceptions as excaption:
                    logging.info(
                        "Exception %s thrown when attempting to run %s, attempt %s of %s.%s",
                        type(excaption).__name__,
                        func.__name__,
                        attempt,
                        times,
                        (
                            f" Sleepening before next attemt for {sleep} seconds."
                            if sleep
                            else ""
                        ),
                    )
                    attempt += 1
                    if sleep:
                        time.sleep(sleep)
                    if sleep and increment_sleep:
                        sleep += increment_sleep
            return func(*args, **kwargs)

        return newfn

    return decorator
