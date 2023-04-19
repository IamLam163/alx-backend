from collections import deque
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """class LRUCache that inherits from BaseCaching and is a
    caching system"""

    def __init__(self):
        super().__init__()
        self.order = deque()

    def put(self, key, item):
        """assign to the dictionary self.cache_data the item
        value for the key key"""
        if key is None or item is None:
            return

        elif key in self.cache_data:
            self.order.remove(key)
            self.order.append(key)
            self.cache_data[key] = item
        elif len(self.cache_data) < BaseCaching.MAX_ITEMS:
            self.order.append(key)
            self.cache_data[key] = item
        else:
            last_elm = self.order.popleft()
            del self.cache_data[last_elm]
            print("DISCARD: {}".format(last_elm))
            self.order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """Returns the value of the item with the
        specified key from the cache."""
        if key is None or key not in self.cache_data:
            return None
        if key in self.order:
            self.order.remove(key)
            self.order.append(key)
        return self.cache_data.get(key)
