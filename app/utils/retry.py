"""
    This file implements the basic retry logic using tenacity. Change configuration if required.
"""



from tenacity import retry, stop_after_attempt, wait_exponential

retry_llm = retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=10),
)