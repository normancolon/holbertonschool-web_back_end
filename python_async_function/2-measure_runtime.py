#!/usr/bin/env python3
"""Measure runtime of asynchronous tasks."""

import time
import asyncio


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the average execution time of wait_n function with n tasks and max_delay.

    Args:
        n (int): Number of asynchronous tasks to run.
        max_delay (int): Maximum delay each task waits before completion.

    Returns:
        float: The average time per task.
    """
    # Import the wait_n function from the module where it's defined.
    wait_n = __import__('1-concurrent_coroutines').wait_n

    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()

    total_time = end_time - start_time
    return total_time / n


# Example usage
if __name__ == "__main__":
    n = 5
    max_delay = 9
    print(measure_time(n, max_delay))
