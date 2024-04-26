#!/usr/bin/env python3
"""Async Programming"""
import time
import asyncio


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the average execution time the wait_n 
    coroutine.

    Parameters:
        n (int): Number of operations to run.
    Returns:
        float: Average time per operation.
    """

    wait_n = __import__('1-concurrent_coroutines').wait_n

    start_time = time.time()

    asyncio.run(wait_n(n, max_delay))

    end_time = time.time()

    return (end_time - start_time) / n


if __name__ == "__main__":

    print("Average time:", measure_time(5, 5))

    print("Average time:", measure_time(10, 7))

    print("Average time:", measure_time(10, 0))
