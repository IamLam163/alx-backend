#!/usr/bin/python3
"""
class LIFOCache that inherits from BaseCaching and is a caching system
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """class LIFOCache that inherits from BaseCaching
    and is a caching system"""

    def __init__(self):
        super().__init__()
        self.order = []

    def put(self, key, item):
        """assign to the dictionary self.cache_data the item
        value for the key key"""
        if key is None or item is None:
            return

        elif (key in self.cache_data):
            self.order.remove(key)
            self.order.append(key)
            self.cache_data[key] = item
        if len(self.cache_data) < BaseCaching.MAX_ITEMS:
            self.order.append(key)
            self.cache_data[key] = item
        else:
            last_elm = self.order.pop(-1)
            del self.cache_data[last_elm]
            print("DISCARD: {}".format(last_elm))
            self.order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """Returns the value of the item with the
        specified key from the cache."""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)


my_cache = LIFOCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
my_cache.put("F", "Mission")
my_cache.print_cache()
my_cache.put("G", "San Francisco")
my_cache.print_cache()
