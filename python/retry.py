import time
from functools import wraps

def retry(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(times):
                
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"attempt {attempt + 1} failed : {e}")

                    if attempt == times -1:
                        raise e

        return wrapper
    return decorator



import random

@retry(times=3)
def unstable_api_call():
    if random.random() < 0.7:   # fails 70% of the time
        raise ConnectionError("API failed")
    return "success"

result = unstable_api_call()
print(result)