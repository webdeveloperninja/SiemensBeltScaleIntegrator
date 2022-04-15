from time import sleep
from typing import Callable


def try_or_retry_times(action: Callable, number_of_tries: int, retry_interval_seconds=60):
    for i in range(number_of_tries):
        try:
            action()
        except:
            if i < number_of_tries - 1:
                sleep(retry_interval_seconds)
                continue
            else:
                raise
        break