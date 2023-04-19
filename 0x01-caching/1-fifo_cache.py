#!/usr/bin/python3
"""
class FIFOCache that inherits from BaseCaching and is a caching system
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """class FIFOCache that inherits from BaseCaching
    and is a caching system"""

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """assign to the dictionary self.cache_data the
        item value for the key key"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_item = next(iter(self.cache_data))
            del self.cache_data[first_item]
            print("DISCARD: {}".format(first_item))

    def get(self, key):
        """returns the value in self.cache_data linked to key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
