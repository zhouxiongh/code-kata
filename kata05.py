#!/usr/bin/env python
# -*- encoding=utf8 -*-
# Added by <zhouxiong.he@outlook.com>
# Added on 2021/3/2

"""
Bloom Filters
"""


class BloomFilter:

    def __init__(self, n, k):
        self.bit_array = [0 for i in range(n)]
        self.k = k

    def insert(self, item):
        for i in range(self.k):
            self.bit_array[self._my_hash(item, i)] = 1

    def __contains__(self, item):
        for i in range(self.k):
            if not self.bit_array[self._my_hash(item, i)]:
                return False
        return True

    def _my_hash(self, item, i):
        re = 0
        for c in item:
            re *= i
            re += ord(c)
        return re % len(self.bit_array)


if __name__ == '__main__':
    bloom_filter = BloomFilter(1000, 3)

