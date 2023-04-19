from base_caching import BaseCaching

class FIFOCache(BaseCaching):
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        if key is None or item is None:
            return

        # Check if key already exists in cache
        if key in self.cache_data:
            print("Key already exists in cache")
            
        self.cache_data[key] = item

        # Check if cache has reached maximum capacity
        if len(self.cache_data) > self.MAX_ITEMS:
            # Get the first key in the cache
            first_key = next(iter(self.cache_data))
            # Remove the first item in the cache
            del self.cache_data[first_key]
            print(f"DISCARD: {first_key}\n")

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]


my_cache = FIFOCache()
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
