#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    kata21.py
# @Author:      jason
# @Time:        2021/12/21 17:36

"""
Kata21: Simple Lists http://codekata.com/kata/kata21-simple-lists/
let’s write three implementations of the list
- A singly linked list (each node has a reference to the next node).
- A doubly linked list (each node has a reference to both the next and previous nodes).
- Some other implementation of your choosing,
except that it should use no references (pointers) to collect nodes together in the list.
"""
# from collections import UserList
from abc import ABC

# from typing import List


class Node:
    def __init__(self, val: str):
        self._val = val

    def value(self) -> str:
        return self._val


class List(ABC):
    def __init__(self):
        pass

    def add(self, word: str):
        pass

    def find(self, word: str) -> int:
        pass

    def delete(self, word: str):
        pass

    def values(self):
        pass


class SinglyLinkedList(List):
    pass


class DoublyLinkedList:
    pass
