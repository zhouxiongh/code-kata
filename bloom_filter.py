#!/usr/bin/env python
# -*- encoding=utf8 -*-
# Added by <zhouxiong.he@outlook.com>
# Added on 2021/3/2

"""
Bloom Filters
"""
import hashlib


class BloomFilter:

    def __init__(self, n, k):
        self.bit_array = [0 for i in range(n)]
        self.k = k

    def insert(self, item):
        for i in range(self.k):
            self.bit_array[self._my_hash(item, i)] = 1

    def contains(self, item):
        for i in range(self.k):
            if not self.bit_array[self._my_hash(item, i)]:
                return False
        return True

    def _my_hash(self, item, i):
        start = 32 // self.k * i
        end = 32 // self.k * (i+1)
        md5 = hashlib.md5()
        md5.update(item.encode('utf-8'))
        re = md5.hexdigest()[start:end]
        return int(re, base=16) % len(self.bit_array)


if __name__ == '__main__':
    bloom_filter = BloomFilter(100000000, 5)
    with open('/usr/share/dict/words', 'r') as f:
        lines = (line.strip() for line in f)
        for line in lines:
            bloom_filter.insert(line)
    word = input('spell check word: ')
    if not bloom_filter.contains(word):
        print('typo')
    else:
        print('spell right')



