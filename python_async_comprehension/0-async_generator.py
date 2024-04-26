#!/usr/bin/env python3
"""
Module dedicated to learning asynchronous programming with a focus on
generators in Python.
"""
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronously generates and yields a random floating-point number
    between 0 and 10. This function runs ten times, with a one-second
    delay between each number generation.

    Yields:
        float: A random float between 0 and 10, yielded once every second.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
