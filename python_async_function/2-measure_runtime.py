#!/usr/bin/env python3
"""Learning Async Programming"""
import time
import asyncio


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the average execution time per operation for the wait_n 
    coroutine.

    Parameters:
        n (int): Number of operations to run concurrently.
        max_delay (int): Max delay each operation can take in seconds.

    Returns:
        float: Average time per operation.
    """
    # Importing wait_n dynamically from a coroutine module
    wait_n = __import__('1-concurrent_coroutines').wait_n

    # Measure start time
    start_time = time.time()
    # Execute wait_n coroutine and wait for completion
    asyncio.run(wait_n(n, max_delay))
    # Measure end time
    end_time = time.time()

    # Calculate average time per operation
    return (end_time - start_time) / n


# Example usage block for when script is executed directly
if __name__ == "__main__":
    # Print average time for 5 operations with a max delay of 5 seconds
    print("Average time:", measure_time(5, 5))
    # Print average time for 10 operations with a max delay of 7 seconds
    print("Average time:", measure_time(10, 7))
    # Print average time for 10 operations with no delay
    print("Average time:", measure_time(10, 0))
