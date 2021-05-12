#!/usr/bin/env python
# -*- encoding=utf8 -*-
# Added by <zhouxiong.he@outlook.com>
# Added on 2021/2/28

"""
Karate Chop: implement binary search in 5 ways
"""


# iteration version of binary search
# def chop(target, source):
#     start = 0
#     end = len(source) - 1
#     mid = start + (end - start) // 2
#
#     while start <= end:
#         if target == source[mid]:
#             return mid
#         elif target < source[mid]:
#             end = mid - 1
#         elif target > source[mid]:
#             start = mid + 1
#         mid = start + (end - start) // 2
#
#     return -1


# recursion version of binary search
def chop(target, source):
    start = 0
    end = len(source) - 1
    return chop_help(target, source, start, end)


def chop_help(target, source, start, end):
    if start <= end:
        mid = start + (end - start) // 2
        if target == source[mid]:
            return mid
        if target < source[mid]:
            return chop_help(target, source, start, mid - 1)
        if target > source[mid]:
            return chop_help(target, source, mid + 1, end)
    return -1
