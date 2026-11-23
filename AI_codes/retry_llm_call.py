import logging
import time

# save logging into file
logging.basicConfig(
    filename = "llm_calls.log",
    level = logging.WARNING
)

def rety_llm_call(func, retries = 3, backoff =2):
    for attempt in range(retries):
        try:
            return func()
        except Exception as e:
            wait = backoff ** attempt
            logging.warning(f"Attempt {attempt} failed : {e}. Retrying in {wait}s")

            if attempt == retries-1:
                raise e
            time.sleep(wait)


            

