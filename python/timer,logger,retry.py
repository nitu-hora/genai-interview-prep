import time
from functools import wraps 
import logging

logging.basicConfig(
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()

        result = func(*args, **kwargs)

        end = time.perf_counter()

        logging.info(
            "%s took %.4f seconds",
            func.__name__,
            end-start
        )

        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1.5)
    return "done"

slow_function()
# expected output: "slow_function took 1.50 seconds"

