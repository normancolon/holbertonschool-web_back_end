#!/usr/bin/env python3
"""
Replicate the functionality to paginate a database and extend it to include
hypermedia information such as pagination details.
"""
import csv
import math
from typing import List, Dict, Tuple


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Load and cache the dataset if not already loaded."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                self.__dataset = [row for row in reader][1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Fetch a paginated slice of baby names, ensuring valid page inputs.
        """
        assert isinstance(page, int) and page > 0, \
            "Page must be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, \
            "Page size must be positive"

        range_start_end = self.index_range(page, page_size)
        return self.dataset()[range_start_end[0]:range_start_end[1]]

    def index_range(self, page, page_size) -> Tuple[int, int]:
        """
        Calculate start and end indices for pagination based on the page number
        and size.
        """
        start = (page - 1) * page_size
        end = start + page_size
        return (start, end)

    def get_hyper(self, page: int, page_size: int) -> Dict[str, any]:
        """
        Generate hypermedia pagination details.
        """
        data = self.get_page(page, page_size)
        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)

        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': page + 1 if page * page_size < total_items else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_pages
        }
