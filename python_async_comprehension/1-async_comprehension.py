#!/usr/bin/env python3
import asyncio
from typing import List

# Import the async_generator function from the specified module.
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Asynchronously collect and return 10 random numbers from an async generator.
    This function uses asynchronous comprehension to gather the numbers.

    Returns:
        List[float]: A list of 10 random float numbers.
    """
    # Ensure async_generator() is correctly called if it needs to be invoked repeatedly.
    return [num async for num in async_generator()]

# This section is for testing and is not part of the module's main functionality.
if __name__ == "__main__":
    async def main():
        random_numbers = await async_comprehension()
        print(random_numbers)

    asyncio.run(main())
