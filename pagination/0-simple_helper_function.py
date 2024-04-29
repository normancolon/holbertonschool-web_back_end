#!/usr/bin/env python3
"""
Write a function `index_range` that calculates the start and end indexes
for pagination, given page numbers and page size, with 1-indexed pages.
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

