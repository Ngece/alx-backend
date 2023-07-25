$ cat base_caching.py
#!/usr/bin/python3
""" BaseCaching module
"""

class BaseCaching():
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initiliaze
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache
        """
        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """ Get an item by key
        """
        raise NotImplementedError("get must be implemented in your cache class")






0-basic_cache.py                a class BasicCache that inherits from BaseCaching and is a caching system.

    You must use self.cache_data - dictionary from the parent class BaseCaching
    This caching system doesn’t have limit
    def put(self, key, item):
        Must assign to the dictionary self.cache_data the item value for the key key.
        If key or item is None, this method should not do anything.
    def get(self, key):
        Must return the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist in self.cache_data, return None.




1-fifo_cache.py                 a class FIFOCache that inherits from BaseCaching and is a caching system.
    Uses self.cache_data - dictionary from the parent class BaseCaching
    def put(self, key, item):
        If key or item is None, this method does not do anything.
        If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
            It discards the first item put in cache (FIFO algorithm)
            and prints DISCARD: with the key discarded and following by a new line
    def get(self, key):
        Returns the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist in self.cache_data, returns None.





2-lifo_cache.py                 a class LIFOCache that inherits from BaseCaching and is a caching system.
    Uses self.cache_data - dictionary from the parent class BaseCaching
    def put(self, key, item):
        Assigns to the dictionary self.cache_data the item value for the key key.
        If key or item is None, this method does not do anything.
        If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
            It discards the last item put in cache (LIFO algorithm)
            and prints DISCARD: with the key discarded and following by a new line
    def get(self, key):
        Returns the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist in self.cache_data, return None.





3-lru_cache.py                  a class MRUCache that inherits from BaseCaching and is a caching system.
    Uses self.cache_data - dictionary from the parent class BaseCaching
        Assigns to the dictionary self.cache_data the item value for the key key.
        If key or item is None, this method does not do anything.
        If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
            It discards the least recently used item (LRU algorithm)
            and prints DISCARD: with the key discarded and following by a new line
    def get(self, key):
        Returns the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist in self.cache_data, return None.





4-mru_cache.py                  a class LFUCache that inherits from BaseCaching and is a caching system.
    Uses self.cache_data - dictionary from the parent class BaseCaching
    def put(self, key, item):
        Assigns to the dictionary self.cache_data the item value for the key key.
        If key or item is None, this method does not do anything.
        If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
            It discards the most recently used item (MRU algorithm)
            and prints DISCARD: with the key discarded and following by a new line
    def get(self, key):
        Returns the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist in self.cache_data, return None.





100-lfu_cache.py                  a class MRUCache that inherits from BaseCaching and is a caching system.
    Uses self.cache_data - dictionary from the parent class BaseCaching
    def put(self, key, item):
        Assigns to the dictionary self.cache_data the item value for the key key.
        If key or item is None, this method does not do anything.
        If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
            It discard the least frequency used item (LFU algorithm)
            if there's more than 1 item to discard, it uses the LRU algorithm to discard only the least recently used
            and prints DISCARD: with the key discarded and following by a new line
    def get(self, key):
        Return the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist in self.cache_data, return None.
