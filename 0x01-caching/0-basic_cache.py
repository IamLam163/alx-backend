#!/usr/bin/python3
"""
class BasicCache that inherits from BaseCaching and is a caching system
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache that inherits from BaseCaching"""

    def __init__(self):
        super().__init__()
        self.cache_data = {}

    def put(self, key, item):
        """assign to the dictionary item value for the key"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """return the value in self.cache_data linked to key"""
        if key is None or key not in self.cache_data:
            return
        return self.cache_data.get(key)
