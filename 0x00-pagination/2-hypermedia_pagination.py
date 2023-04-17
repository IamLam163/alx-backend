#!/usr/bin/env python3
"""
function returns the start and end index of a page
"""


import csv
from typing import Dict, List, Tuple
import math


def index_range(page: int, page_size: int) -> Tuple:
    """function returns a tuple containing the start & end idx"""
    start_idx = (page - 1) * page_size
    end_idx = start_idx + page_size
    return (start_idx, end_idx)


class Server:
    """class to paginate a database of popular baby names"""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """get page based on the csv file"""
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        data = self.dataset()
        if start >= len(data):
            return []
        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """returns a Dictionary"""
        page_data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        page_details = {
            'page_size': len(page_data),
            'page': page,
            'data': page_data,
            'next-page': None if page >= total_pages else page + 1,
            'prev_page': None if page - 1 == 0 else page - 1,
            'total_pages': total_pages,
        }
        return page_details



server = Server()

print(server.get_hyper(1, 2))
print("---")
print(server.get_hyper(2, 2))
print("---")
print(server.get_hyper(100, 3))
print("---")
print(server.get_hyper(3000, 100))
