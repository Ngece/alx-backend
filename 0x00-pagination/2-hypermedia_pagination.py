#!/usr/bin/env python3
""" Implements a method named get_page that takes two 
integer arguments page with default value 1 and page_size 
with default value 10.
"""

import csv
import math
from typing import List, Tuple, Dict

def index_range(page: int, page_size: int) -> tuple:
    """ return a tuple of size two containing a start 
    index and an end index. 
    """
    return ((page - 1) * page_size, page * page_size)

class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]: # type: ignore
        """ Finds the correct indexes to paginate dataset correctly """
        try:
            assert type(page) is int and type(page_size) is int
            assert page > 0 and page_size > 0
        except AssertionError:
            raise AssertionError
        
        self.dataset()
        if page > len(self.__dataset) or page_size > len(self.__dataset):
            return []
        indexes = index_range(page, page_size)
        return self.__dataset[indexes[0]:indexes[1]]
    
    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """ returns a dictionary containing key-value pairs """
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.__dataset) / page_size)
        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': page + 1 if page < total_pages else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_pages
        }