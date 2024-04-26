#!/usr/bin/env python3
"""Learning Async Programming"""
import time
import asyncio


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the average execution time the wait_n 
    coroutine.

    Parameters:
        n (int): Number of operations to run concurrently.
        max_delay (int): Max delay each operation can take in seconds.

    Returns:
        float: Average time per operation.
    """

    wait_n = __import__('1-concurrent_coroutines').wait_n

    # Measure start time
    start_time = time.time()
    # Execute wait_n coroutine and wait for completion
    asyncio.run(wait_n(n, max_delay))
    # Measure end time
    end_time = time.time()

    # Calculate average time per operation
    return (end_time - start_time) / n


if __name__ == "__main__":

    print("Average time:", measure_time(5, 5))

    print("Average time:", measure_time(10, 7))

    print("Average time:", measure_time(10, 0))
