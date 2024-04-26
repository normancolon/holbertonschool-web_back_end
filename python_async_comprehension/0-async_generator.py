#!/usr/bin/env python3
"""
Module to demonstrate asynchronous programming in Python
with a simple coroutine that waits for a random time.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay up to max_delay
    seconds and returns the duration of that delay.

    Args:
        max_delay (int): Maximum number of seconds to delay. Defaults to 10.

    Returns:
        float: The actual delay in seconds.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

# Example usage code, as seen in the provided commands:
if __name__ == "__main__":
    async def main():
        print(await wait_random())
        print(await wait_random(5))
        print(await wait_random(15))

    asyncio.run(main())
