#!/usr/bin/env python3
""" LFU Caching """

from base_caching import BaseCaching

class LFUCache(BaseCaching):
    """ LFU Caching """
    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.queue = []
        self.cache_data = {}
        self.freq = {}

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
            if key not in self.freq.keys():
                self.freq[key] = 0
            self.freq[key] += 1

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data.keys():
            return None
        else:
            self.queue.remove(key)
            self.queue.append(key)
            self.freq[key] += 1
            return self.cache_data[key]