#!/usr/bin/env python3
"""
Module containing the wait_n coroutine for concurrently executing multiple
instances of the wait_random coroutine and returning the results in the order
they complete.
"""
import asyncio
from typing import List

# Import wait_random from the file where it is defined.
wait_random = __import__('0-async_generator').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Executes 'n' instances of wait_random concurrently with the given 'max_delay'.
    Returns a list of delays experienced, ordered by completion time.

    Args:
        n (int): Number of wait_random instances to run.
        max_delay (int): Max delay for each wait_random call.

    Returns:
        List[float]: Delays in the order of completion.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]

# Example usage and testing
if __name__ == "__main__":
    async def main():
        results = await wait_n(5, 5)
        print(results)
        results = await wait_n(10, 7)
        print(results)
        results = await wait_n(10, 0)
        print(results)

    asyncio.run(main())
