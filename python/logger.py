import logging
from functools import wraps

log = logging.getLogger(__name__)
logging.basicConfig(level = logging.INFO,format="%(asctime)s - %(levelname)s - %(message)s")

def logger(func):
    @wraps(func)
    def wrapper(*args):
        log.info("Calling %s with %s", func.__name__, args)

        result = func(*args)

        log.info("%s returned %s", func.__name__, result)

        return result

    return wrapper

@logger
def add(a, b):
    return a + b

add(3, 5)

