#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    Kata15.py
# @Author:      jason
# @Time:        2021/12/20 16:55

"""
A Diversion http://codekata.com/kata/kata15-a-diversion/
"""
import itertools


def foo(bin_num):
    for i in range(len(bin_num) - 1):
        if bin_num[i] == 1 and bin_num[i + 1] == 1:
            return False
    return True


def bar(repeat):
    ans = 0
    for bin_num in list(itertools.product(range(2), repeat=repeat)):
        if foo(bin_num):
            ans += 1
    return ans


if __name__ == "__main__":
    for i in [3, 4, 5, 8, 9, 10]:
        print(bar(i))
