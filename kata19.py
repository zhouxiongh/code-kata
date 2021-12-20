#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    kata19.py
# @Author:      jason
# @Time:        2021/12/20 21:14

"""
Kata19: Word Chains http://codekata.com/kata/kata19-word-chains/
"""
import collections


def word_chain(start, target, bank):
    def valid_mutation(s1, s2):
        if len(s1) != len(s2):
            return False
        counter = 0
        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                counter += 1
            if counter > 1:
                return False
        return True

    ans = 0
    queue = collections.deque()
    queue.append(start)
    visited = set()
    while queue:
        size = len(queue)
        while size:
            size -= 1
            cur = queue.popleft()
            if cur == target:
                return ans
            for b in bank:
                if valid_mutation(cur, b) and b not in visited:
                    visited.add(b)
                    queue.append(b)
        ans += 1
    return -1
