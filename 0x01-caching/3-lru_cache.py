#!/usr/bin/env python3
""" LRU Caching """

from base_caching import BaseCaching

class LRUCache(BaseCaching):
    """ LRU Caching """
    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.queue = []
        self.cache_data = {}

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            pass
        else:
            if len(self.cache_data) >= self.MAX_ITEMS:
                if key not in self.cache_data.keys():
                    discard = self.queue.pop(0)
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
            self.queue.remove(key)
            self.queue.append(key)
            return self.cache_data[key]