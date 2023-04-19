#!/usr/bin/python3
from base_caching import BaseCaching
"""
class MRUCache that inherits from BaseCaching and is a caching system
"""


class MRUCache(BaseCaching):
    """class MRUCache that inherits from BaseCaching and is a
    caching system that uses the MRU algorithm"""

    def __init__(self):
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Assign to the dictionary self.cache_data the item
        value for the key key, using the MRU algorithm."""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            mru_key = self.order.pop()
            del self.cache_data[mru_key]
            print("DISCARD: {}".format(mru_key))

        self.order.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """Returns the value of the item with the
        specified key from the cache."""
        if key is None or key not in self.cache_data:
            return None

        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
