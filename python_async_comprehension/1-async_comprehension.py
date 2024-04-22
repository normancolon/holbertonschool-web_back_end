#!/usr/bin/env python3
import asyncio
from typing import List

# Fetch the async_generator function
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collect and return 10 random numbers 
    comprehension from an async generator.
    """
    return [num async for num in async_generator()]

# Test section, not included main module.
if __name__ == "__main__":
    async def main():
        random_numbers = await async_comprehension()
        print(random_numbers)

    asyncio.run(main())
