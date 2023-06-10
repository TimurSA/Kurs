from functools import wraps
from timeit import default_timer as timer


def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kvargs):
        start = timer()

        func(*args, **kvargs)

        end = timer()

        print(f'Function {func.__name__} took {end - start} for execution')

    return wrapper
