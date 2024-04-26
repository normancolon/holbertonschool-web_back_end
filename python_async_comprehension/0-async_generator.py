#!/usr/bin/env python3
"""Module for exploring asynchronous generators in Python."""

import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronously generates and yields ten random floats between 0 and 10,
    with a one-second delay between each generation.

    Each yield returns a random float, simulating a process where each step
    takes some time (e.g., data retrieval or computation).

    Yields:
        float: A random float between 0 and 10 after a 1-second delay.
    """
    for _ in range(10):  # Use '_' when the index is not utilized
        await asyncio.sleep(1)  # Delay to simulate an asynchronous operation
        yield random.uniform(0, 10)  # Yield a random floating-point number

# Example usage of the async generator, if this script is executed directly.
if __name__ == "__main__":
    async def display_numbers():
        async for number in async_generator():
            print(f"Generated number: {number}")

    asyncio.run(display_numbers())
