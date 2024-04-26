#!/usr/bin/env python3
"""Learning Async in Python by running multiple async tasks concurrently."""

import asyncio
from typing import List


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Runs multiple instances of the task_wait_random coroutine concurrently
    and collects their results.

    Args:
        n (int): Number of coroutine instances to run.
        max_delay (int): Maximum delay for each coroutine in seconds.

    Returns:
        List[float]: List of completion times of the tasks, in the order
                     they finished.
    """
    # Import task creator dynamically for flexibility
    task_wait_random = __import__('3-tasks').task_wait_random
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    # Collecting results as tasks complete
    completed_tasks = []
    for task in asyncio.as_completed(tasks):
        completed_tasks.append(await task)

    return completed_tasks

# Example usage to test the coroutine when the script is run directly.
if __name__ == "__main__":
    async def main():
        results = await task_wait_n(5, 5)
        print("Task completion times:", results)
        results = await task_wait_n(10, 7)
        print("Task completion times:", results)
        results = await task_wait_n(10, 0)
        print("Task completion times:", results)

    asyncio.run(main())
