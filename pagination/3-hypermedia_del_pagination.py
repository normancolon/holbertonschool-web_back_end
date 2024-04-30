#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination for a database of popular baby names.
"""
import csv
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Load and cache the dataset if not already loaded."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                self.__dataset = [row for row in reader][1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """
        Create and return an indexed dataset up to the first 1000 records.
        """
        if self.__indexed_dataset is None:
            self.__indexed_dataset = {
                i: item for i, item in enumerate(self.dataset()[:1000])
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = 0, page_size: int = 10) -> Dict:
        """
        Return pagination details starting from a given index page size.
        Includes the current index, next index, page size, and page data.
        """
        current_data = self.dataset()
        next_index = index + page_size
        page_data = current_data[index:next_index]
        return {
            'index': index,
            'next_index': (next_index if next_index < len(current_data)
                           else len(current_data)),
            'page_size': page_size,
            'data': page_data
        }
