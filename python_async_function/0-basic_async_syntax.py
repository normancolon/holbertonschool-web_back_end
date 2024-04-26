#!/usr/bin/env python3
"""Module for demonstrating asynchronous waiting with random
delays in Python."""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronously waits for a random duration up to max_delay seconds.

    Args:
        max_delay (int): Maximum delay in seconds, default is 10.

    Returns:
        float: The actual delay time in seconds.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)  # Pause for the delay duration
    return delay  # Return how long it actually waited
