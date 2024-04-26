#!/usr/bin/env python3
"""
Module to learn asynchronous programming through
generators that produce random floats.
"""
from typing import List
# Import async_generator from a separate module
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Runs async_generator 10 times to collect random floats.
    Returns these floats as a list.

    Returns:
        List[float]: A collection of random floats.
    """
    return [random_float async for random_float in async_generator()]
