#!/usr/bin/env python3
"""Module defining a function to create asyncio tasks."""

import asyncio


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio.Task that executes the wait_random coroutine
    with a specified delay.

    Args:
        max_delay (int): Maximum delay in seconds before the task completes.

    Returns:
        asyncio.Task: Task executing the wait_random coroutine.
    """
    # Dynamic import for modular flexibility
    wait_random = __import__('0-basic_async_syntax').wait_random

    # Create and return the task
    return asyncio.create_task(wait_random(max_delay))


# Example test function to demonstrate task execution
if __name__ == "__main__":
    async def test(max_delay: int) -> None:
        task = task_wait_random(max_delay)
        await task  # Wait for the task to complete
        print(f'Task completed with delay: {max_delay}')

    asyncio.run(test(5))
