#!/usr/bin/env python3
""" FIFO caching system """

from base_caching import BaseCaching

class FIFOCache(BaseCaching):
    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.cache_data = {}
        self.queue = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            pass
        else:
            if len(self.cache_data) >= self.MAX_ITEMS:
                if key not in self.cache_data.keys():
                    first = self.queue.pop(0)
                    del self.cache_data[first]
                    print("DISCARD: {}".format(first))
            self.queue.append(key)
            self.cache_data[key] = item