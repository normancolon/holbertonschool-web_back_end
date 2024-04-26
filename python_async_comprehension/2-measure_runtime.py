#!/usr/bin/env python3
"""
Module for learning async programming through practical
application.
"""

import time
import asyncio

# Import the async_comprehension coroutine from another module
async_comprehension = __import__(
    '1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the runtime of executing the async_comprehension
    coroutine four times concurrently.

    This function utilizes asyncio.gather to run multiple
    instances of async_comprehension simultaneously and
    measures the total runtime.

    Returns:
        float: The total time taken to execute the coroutine
               four times, measured in seconds.
    """
    start = time.time()
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    end = time.time()
    return end - start  # Calculate and return the elapsed time

# Testing and demonstration of the measure_runtime function.
if __name__ == "__main__":
    async def main():
        runtime = await measure_runtime()
        print(f"Total execution time: {runtime} seconds")

    asyncio.run(main())
