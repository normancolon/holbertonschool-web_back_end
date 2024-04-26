#!/usr/bin/env python3
"""Module to create asyncio tasks using wait_random from a prior module."""

import asyncio


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio.Task that executes the wait_random coroutine with a specified delay.

    Args:
        max_delay (int): Maximum delay, in seconds, before the task completes.

    Returns:
        asyncio.Task: The task running the wait_random coroutine.
    """
    # Import the wait_random function dynamically to ensure modular flexibility
    wait_random = __import__('0-basic_async_syntax').wait_random

    # Create and return the task using the wait_random coroutine
    return asyncio.create_task(wait_random(max_delay))


# This testing block runs only if this script is executed directly.
if __name__ == "__main__":
    async def test(max_delay: int) -> None:
        task = task_wait_random(max_delay)
        await task  # Await the task to completion
        print(task.__class__)  # Print the class of the task to verify its type

    asyncio.run(test(5))
