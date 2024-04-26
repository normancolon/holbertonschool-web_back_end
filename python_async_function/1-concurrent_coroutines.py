#!/usr/bin/env python3
"""Async Programming"""
import asyncio
from typing import List


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Executes multiple instances of the wait_random coroutine
    collecting and returning the delays as they complete.

    Parameters:
        n (int): The number of times to run the coroutine.
        max_delay (int): maximum delay each coroutine.

    Returns:
        List[float]: list of floating-point numbers representing  delays,
                     returned in  order that the tasks complete.
    """
    # Import wait_random inside the function to avoid potential import issues at the module level.
    wait_random = __import__('0-basic_async_syntax').wait_random

    # Create a list of coroutine objects using a list comprehension.
    tasks = [wait_random(max_delay) for _ in range(n)]

    # Collect completed tasks using asyncio.as_completed to maintain the order of completion.
    return [await task for task in asyncio.as_completed(tasks)]

# Testing the function if the script is run as the main module.
if __name__ == "__main__":
    async def main():
        results = await wait_n(5, 5)
        print(results)
        results = await wait_n(10, 7)
        print(results)
        results = await wait_n(10, 0)
        print(results)

    asyncio.run(main())
