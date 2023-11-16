import random
import functools
import time


def log(template):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            working_time = 5 * random.random()
            print(f'{template.format(working_time)}')
            time.sleep(working_time)
            return func(*args, **kwargs)

        return wrapper

    return decorator
