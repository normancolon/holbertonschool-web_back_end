#!/usr/bin/env python3
'''
Test file for checking the functionality of the wait_n coroutine
'''
import asyncio
from typing import List

# Assuming wait_random is imported from the previous module
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with the specified max_delay. Collect
    and return the delays in ascending order as they complete.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay for wait_random.

    Returns:
        List[float]: A list of completion times in ascending order.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    completed_delays = []
    for future in asyncio.as_completed(tasks):
        result = await future
        completed_delays.append(result)
    return completed_delays

# Testing code below (not part of the module)
if __name__ == "__main__":
    async def main():
        print(await wait_n(5, 5))
        print(await wait_n(10, 7))
        print(await wait_n(10, 0))

    asyncio.run(main())
