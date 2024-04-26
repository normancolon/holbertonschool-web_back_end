#!/usr/bin/env python3
"""Learning Async Programming"""
import time
import asyncio


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the average execution time of wait_n(n, max_delay) per execution.

    Args:
        n (int): The number of times to run the coroutine.
        max_delay (int): The maximum delay each coroutine waits before returning.

    Returns:
        float: The average time taken per execution of wait_n.
    """
    # Import wait_n at the function level to avoid import-time side effects.
    wait_n = __import__('1-concurrent_coroutines').wait_n
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start_time

    return total_time / n


# Example test code.
if __name__ == "__main__":
    n = 5
    max_delay = 9
    print(measure_time(n, max_delay))
