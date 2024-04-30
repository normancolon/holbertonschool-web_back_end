#!/usr/bin/env python3
"""
This module defines the index_range function, which calculates the start and
end indexes for a pagination mechanism given the page number and page size.
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Calculate the start and end index for pagination page_size.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple containing the start and end index of the items for
               the page.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
