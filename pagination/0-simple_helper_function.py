#!/usr/bin/env python3
"""
calculates the start and end indexes
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Calculate start and end index for pagination.
    """
    if page < 1 or page_size < 1:
        exit(1)
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)

