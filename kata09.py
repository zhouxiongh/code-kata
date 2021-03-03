#!/usr/bin/env python
# -*- encoding=utf8 -*-
# Added by <zhouxiong.he@outlook.com>
# Added on 2021/3/3

""" 
Enter module description here
"""
import unittest
from itertools import islice


class CheckOut:
    def __init__(self, pricing_rules):
        self.total = 0
        with open(pricing_rules, 'r') as f:
            lines = (line.strip() for line in f)
            for line in islice(lines, 3, None):
                print(line)

    def scan(self, item):
        pass


RULES = "./data/pricing_rules.dat"


def price(goods):
    co = CheckOut(RULES)
    for good in list(goods):
        co.scan(good)
    return co.total


class TestPrice(unittest.TestCase):

    def test_totals(self):
        self.assertEqual(0, price(""))
        self.assertEqual(0, price(""))
        self.assertEqual(50, price("A"))
        self.assertEqual(80, price("AB"))
        self.assertEqual(115, price("CDBA"))

        self.assertEqual(100, price("AA"))
        self.assertEqual(130, price("AAA"))
        self.assertEqual(180, price("AAAA"))
        self.assertEqual(230, price("AAAAA"))
        self.assertEqual(260, price("AAAAAA"))

        self.assertEqual(160, price("AAAB"))
        self.assertEqual(175, price("AAABB"))
        self.assertEqual(190, price("AAABBD"))
        self.assertEqual(190, price("DABABA"))

    def test_incremental(self):
        co = CheckOut(RULES)
        # self.assertEqual(0, co.total)
        # co.scan("A")
        # self.assertEqual(50, co.total)
        # co.scan("B")
        # self.assertEqual(80, co.total)
        # co.scan("A")
        # self.assertEqual(130, co.total)
        # co.scan("A")
        # self.assertEqual(160, co.total)
        # co.scan("B")
        # self.assertEqual(175, co.total)
