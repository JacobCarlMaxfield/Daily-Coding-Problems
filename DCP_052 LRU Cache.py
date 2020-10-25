"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Implement an LRU (Least Recently Used) cache. It should be able to be initialized with a cache size n, and contain the following methods:

set(key, value): sets key to value. If there are already n items in the cache and we are adding a new item, then it should also remove the least recently used item.
get(key): gets the value at key. If no such key exists, return null.
Each operation should run in O(1) time.
"""

class LRU():
    def __init__(self, d=dict(), n=1) -> None:
        self.cache = [x for x in d][:n]
        self.d = d
        self.n = n

    def set(self, key, value):
        self.d[key] = value
        if key in self.cache:
            self.cache.remove(key)
        self.cache.append(key)
        if len(self.cache) > self.n:
            del self.cache[0]
            
    def get(self, key):
        if key in self.d:
            return self.d[key]
        return None

x = LRU({'a':5, 'b':2, 'c':9}, 3)

print(x.d, x.cache)
x.set('a', 7)
print(x.d, x.cache)
print(x.get('b'))
x.set('d', 29)
print(x.d, x.cache)


