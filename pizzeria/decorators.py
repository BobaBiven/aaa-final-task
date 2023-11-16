import random
import functools
import time


def log(template):
    """
    A decorator that logs the time it takes for a function to execute.

    Args:
    - template (str): The template string used to format the log message.

    Returns:
    - decorator: The decorator function.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            working_time = 5 * random.random()
            print(f'{template.format(working_time)}')
            time.sleep(working_time)
            return func(*args, **kwargs)

        return wrapper

    return decorator
