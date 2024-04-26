#!/usr/bin/env python3
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits (inclusive).
    It returns the actual delay.

    Args:
    max_delay (int): The maximum delay time in seconds.

    Returns:0-basic_async_syntax.py
    float: The actual delay time.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
