#!/usr/bin/env python3
"""
function returns the start and end index of a page
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """function returns a tuple containing the start & end idx"""
    start_idx = (page - 1) * page_size
    end_idx = start_idx + page_size
    return (start_idx, end_idx)
