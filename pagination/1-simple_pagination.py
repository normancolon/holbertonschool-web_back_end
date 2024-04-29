#!/usr/bin/env python3
""" simple pagination """
import csv
from typing import List


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Load and cache dataset if not already loaded."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                self.__dataset = [row for row in reader][1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Fetch a paginated slice of baby names, ensuring valid page inputs."""
        assert isinstance(page, int) and page > 0, "Page must be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, "Page size must be positive"
        
        range_start_end = self.index_range(page, page_size)
        return self.dataset()[range_start_end[0]:range_start_end[1]]

    def index_range(self, page, page_size) -> tuple:
        """ gets page """
        start = (page - 1) * page_size
        end = start + page_size
        return (start, end)


if __name__ == "__main__":
    server = Server()
    print(server.get_page(1, 10))  # Example usage

