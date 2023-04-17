#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import Dict, List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """function returns a dictionary with key valu pairs"""
        data = self.indexed_dataset()
        assert index is not None and index >= 0 and index < 1000
        page = (index + page_size) // page_size
        end_idx = index + page_size
        page_data = []
        for i in range(index, end_idx):
            try:
                page_data.append(data[i])
            except Exception:
                end_idx += 1
        page_info = {
            "index": index,
            "data": page_data,
            "page_size": page_size,
            "next_index": end_idx
        }
        return page_info
