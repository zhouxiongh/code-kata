#!/usr/bin/env python
# -*- encoding=utf8 -*-
# Added by <zhouxiong.he@outlook.com>
# Added on 2021/3/4

"""
Kata11: Sorting It Out
http://codekata.com/kata/kata11-sorting-it-out/
"""
import unittest


class Rack:
    def __init__(self):
        self.balls = []
        pass

    def add(self, num):
        pass


class TestSort(unittest.TestCase):

    def test_ball(self):
        rack = Rack()
        self.assertEqual([], rack.balls)
        rack.add(20)
        self.assertEqual([20], rack.balls)
        rack.add(10)
        self.assertEqual([10, 20], rack.balls)
        rack.add(30)
        self.assertEqual([10, 20, 30], rack.balls)

    def test_characters(self):
        """
        :input: When not studying nuclear physics, Bambi likes to play
beach volleyball.
        :return: aaaaabbbbcccdeeeeeghhhiiiiklllllllmnnnnooopprsssstttuuvwyyyy
        """
        pass
