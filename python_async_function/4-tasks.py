#!/usr/bin/env python3
"""Learning Async with multiple coroutine executions."""

import asyncio
from typing import List


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Executes multiple asyncio tasks concurrently and collects their results.

    Args:
        n (int): Number of asyncio tasks to run.
        max_delay (int): The maximum delay each task waits before completing.

    Returns:
        List[float]: A list of elapsed times from each completed task.
    """
    # Importing the task creator function within the function scope
    task_wait_random = __import__('3-tasks').task_wait_random
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]

# If this script is executed as the main module, run a simple test.
if __name__ == "__main__":
    async def main():
        results = await task_wait_n(5, 5)
        print(f"Task completion times: {results}")

    asyncio.run(main())
