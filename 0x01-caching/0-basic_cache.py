#!/usr/bin/env python3
""" A caching system doesn’t have limit"""

from base_caching import BaseCaching

class BasicCache():
    """ A caching system doesn’t have limit"""
    def __init__(self):
        """ Initiliaze
        """
        self.cache_data = {}

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data.keys():
            return None
        else:
            return self.cache_data[key]