#!/usr/bin/env python3
"""Learning Async in Python using random delays"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronously waits for a random time up to 'max_delay' seconds.

    Args:
        max_delay (int): Maximum delay in seconds. Default is 10.

    Returns:
        float: The actual delay time that was awaited.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

# Example usage (not part of the module):
if __name__ == "__main__":
    async def main():
        print(await wait_random())
        print(await wait_random(5))
        print(await wait_random(15))

    asyncio.run(main())
