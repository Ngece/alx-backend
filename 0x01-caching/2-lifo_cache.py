#!/usr/bin/env python3
""" LIFO caching system """

from base_caching import BaseCaching

class LIFOCache(BaseCaching):
    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            pass
        else:
            if len(self.cache_data) >= self.MAX_ITEMS:
                if key not in self.cache_data.keys():
                    discard = self.queue.pop()
                    del self.cache_data[discard]
                    print("DISCARD: {}".format(discard))
            self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data.keys():
            return None
        else:
            return self.cache_data[key] 