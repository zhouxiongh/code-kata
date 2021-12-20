#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    kata18.py
# @Author:      jason
# @Time:        2021/12/20 18:33

""" 
Kata18: Transitive Dependencies http://codekata.com/kata/kata18-transitive-dependencies/
"""
from typing import List
import collections


class Dependencies:
    def __init__(self):
        self._dependencies = collections.defaultdict(list)

    def add_direct(self, u, v):
        for dependency in v:
            if dependency not in self._dependencies[u]:
                self._dependencies[u].append(dependency)

    def dependencies_for(self, u) -> List[str]:
        return self._dependencies_for(u, u)

    def _dependencies_for(self, u, origin) -> List[str]:
        ans = []
        for dependency in self._dependencies[u]:
            if dependency == origin:
                raise TypeError
            if dependency not in ans:
                ans.append(dependency)
                if dependency in self._dependencies:
                    ans.extend(self._dependencies_for(dependency, origin))

        return sorted(ans)
