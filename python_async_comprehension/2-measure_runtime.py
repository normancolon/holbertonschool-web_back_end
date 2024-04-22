#!/usr/bin/env python3
import asyncio
import time

# Import the async_comprehension
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure the runtime ."""
    start_time = time.time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end_time = time.time()
    return end_time - start_time

# This section is for testing
if __name__ == "__main__":
    async def main():
        runtime = await measure_runtime()
        print(runtime)

    asyncio.run(main())
