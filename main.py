""""""
import logging

from retry import retry


@retry(times=3, exceptions=(ValueError, TypeError), sleep=1, increment_sleep=0.5)
def do_and_raise():
    print("working")
    raise ValueError("Some error")


if __name__ == "__main__":
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(message)s",
        style="%",
        datefmt="%Y-%m-%d %H:%M",
        level=logging.INFO,
    )
    do_and_raise()
