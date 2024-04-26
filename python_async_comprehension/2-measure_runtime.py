#!/usr/bin/env python3
"""
Exploration of asynchronous programming with a focus on runtime
measurement.
"""
import time
import asyncio
# Import async_comprehension from its respective module
async_comprehension = __import__(
    '1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Execute async_comprehension four times concurrently,
    measure and return the execution time.

    Returns:
        float: Total time in seconds for all tasks to complete.
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.time()

    return end_time - start_time
