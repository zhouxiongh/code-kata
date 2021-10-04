#!/usr/bin/env python
# -*- encoding=utf8 -*-
# Added by <zhouxiong.he@outlook.com>
# Added on 2021/3/4

"""
Kata13: Counting Code Lines
http://codekata.com/kata/kata13-counting-code-lines/
"""
from abc import ABCMeta, abstractmethod

class Dave(ABCMeta):
    @abstractmethod
    def count_lines(self):
        pass
