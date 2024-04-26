#!/usr/bin/env python3
"""Learning Async in Python using random delays with an async generator."""

import asyncio
import random


async def async_generator(max_delay: int = 10, count: int = 10) -> float:
    """
    Asynchronously generates random delays up to 'max_delay' seconds.

    Args:
        max_delay (int): Maximum delay in seconds. Default is 10.
        count (int): Number of random delays to generate. Default is 10.

    Yields:
        float: A random delay time that was awaited.
    """
    for _ in range(count):
        delay = random.uniform(0, max_delay)
        await asyncio.sleep(delay)
        yield delay

# Example usage (not part of the module):
if __name__ == "__main__":
    async def main():
        async for delay in async_generator(5, 5):
            print(delay)

    asyncio.run(main())
