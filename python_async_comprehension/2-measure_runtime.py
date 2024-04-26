#!/usr/bin/env python3
"""Explore asynchronous programming with a focus on generators."""

import time
import asyncio


fetch_async_data = __import__('1-async_comprehension').async_comprehension


async def calculate_parallel_execution_time() -> float:
    """
    Measure the time taken to concurrently execute the fetch_async_data function

    Returns:
        float: The total elapsed time in seconds to complete all four operations.
    """
    start_time = time.time()
    # Execute four instances of the asynchronous comprehension concurrently
    await asyncio.gather(*(fetch_async_data() for _ in range(4)))
    end_time = time.time()

    return end_time - start_time

if __name__ == "__main__":
    async def main():
        execution_time = await calculate_parallel_execution_time()
        print(f"Total parallel execution time: {execution_time} seconds")

    asyncio.run(main())
