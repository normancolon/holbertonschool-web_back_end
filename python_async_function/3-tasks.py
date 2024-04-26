#!/usr/bin/env python3
"""Module to create asyncio tasks using wait_random from a prior module."""

import asyncio


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio.Task that executes the wait_random coroutine
    with a specified delay.

    Args:
        max_delay (int): Maximum delay, in seconds, before the task completes.

    Returns:
        asyncio.Task: The task running the wait_random coroutine.
    """
    # Dynamically import wait_random for modular flexibility
    wait_random = __import__('0-basic_async_syntax').wait_random

    # Create and return the task
    return asyncio.create_task(wait_random(max_delay))


# Testing block runs only if script is executed directly.
if __name__ == "__main__":
    async def test(max_delay: int) -> None:
        task = task_wait_random(max_delay)
        await task  # Await the task to completion
        print(task.__class__)  # Verify the task's class type

    asyncio.run(test(5))
