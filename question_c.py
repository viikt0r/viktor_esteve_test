from collections import OrderedDict
import time
import datetime

class LRUCache(object):

    def __init__(self, max_size=1024):
        self.max_size = max_size
        self.__values = {}
        self.__access_times = OrderedDict()
        self.access_iter = 0

    def size(self):
        return len(self.__values)

    def clear(self):
        self.__values.clear()
        self.__access_times.clear()

    def contains(self, key):
        return self.has_key(key)
        
    def has_key(self, key):
        return key in self.__values

    def __setitem__(self, key, value):
        self.__values[key] = value
        self.__access_times[key] = self.access_iter
        self.access_iter += 1
        self.cleanup()

    def __getitem__(self, key):
        self.__access_times[key] = self.access_iter
        self.access_iter += 1
        return self.__values[key]

    def __delete__(self, key):
        if key in self.__values:
            del self.__values[key]
            del self.__access_times[key]

    def cleanup(self):
        t = int(time.time())
        #If we have more than self.max_size items, delete the oldest
        while (len(self.__values) > self.max_size):
            for k in self.__access_times:
                self.__delete__(k)
                break