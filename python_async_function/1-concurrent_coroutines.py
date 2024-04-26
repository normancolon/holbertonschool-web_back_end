#!/usr/bin/env python3
"""Learning Async Programming"""
import asyncio
from typing import List


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Runs multiple coroutines of wait_random and returns their delays.

    Parameters:
        n (int): Number of wait_random coroutines to run.
        max_delay (int): Maximum delay for wait_random.

    Returns:
        List[float]: List of delays from the completed tasks.
    """
    # Importing wait_random function dynamically.
    wait_random = __import__('0-basic_async_syntax').wait_random
    tasks = [wait_random(max_delay) for _ in range(n)]

    # Assembling results as tasks complete.
    completed_tasks = []
    for task in asyncio.as_completed(tasks):
        completed_tasks.append(await task)

    return completed_tasks

# Example usage for testing the function when this script is run.
if __name__ == "__main__":
    async def main():
        results = await wait_n(5, 5)
        print("Delays: ", results)
        results = await wait_n(10, 7)
        print("Delays: ", results)
        results = await wait_n(10, 0)
        print("Delays: ", results)

    asyncio.run(main())
