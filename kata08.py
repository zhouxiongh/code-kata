#!/usr/bin/env python
# -*- encoding=utf8 -*-
# Added by <zhouxiong.he@outlook.com>
# Added on 2021/3/3

"""
Conflicting Objectives: http://codekata.com/kata/kata08-conflicting-objectives/
"""

# The first version, make program as readable as you can make it.
from time import time


def n_leeter_word():
    smaller_words = []
    words = []
    re = []
    t1 = time()
    print('------------------')
    print('normal version')
    print("begin time:", t1)
    with open('/usr/share/dict/words', 'r') as f:
        lines = (line.strip() for line in f)
        for line in lines:
            if len(line) < 6:
                smaller_words.append(line)
            if len(line) == 6:
                words.append(line)

    t2 = time()
    print("t2 - t1:", t2 - t1)
    print("words:", words)
    print("smaller_words:", smaller_words)
    for word in words:
        for i in range(1, len(word)):
            if word[:i] in smaller_words and word[i:] in smaller_words:
                re.append(word)
                break

    t3 = time()
    print("total time:", t3 - t1)
    print("re:", re)


# The second version, optimize the program to run fast fast as you can make it.
def optimize_n_letter_word(n, dict_words):
    smaller_words = {}
    words = []
    re = []
    t1 = time()
    print('----------------')
    print('optimize version')
    print('begin time', t1)
    with open(dict_words, 'r') as f:
        lines = (line.strip() for line in f)
        for line in lines:
            if len(line) < n:
                smaller_words[line] = 1
            if len(line) == n:
                words.append(line)
    t2 = time()
    print('T2 - T1:', (t2 - t1))
    print("words:", words)
    print("smaller_words:", smaller_words)
    for word in words:
        for i in range(1, len(word)):
            if word[:i] in smaller_words and word[i:] in smaller_words:
                re.append(word)
                break

    t3 = time()
    print('total time:', (t3 - t1))
    print("re:", re)


# The third version, write as extendible a program as you can.

def extend_n_letter_word(n, dict_words):
    smaller_words = []
    words = []
    re = []
    t1 = time()
    print('---------------')
    print('extend version')
    print('begin time', t1)
    with open(dict_words, 'r') as f:
        lines = (line.strip() for line in f)
        for line in lines:
            if len(line) < n:
                smaller_words.append(line)
            if len(line) == n:
                words.append(line)
    t2 = time()
    print('T2 - T1:', (t2 - t1))
    print("words:", words)
    print("smaller_words:", smaller_words)
    for word in words:
        for i in range(1, len(word)):
            if word[:i] in smaller_words and word[i:] in smaller_words:
                re.append(word)
                break

    t3 = time()
    print('total time:', (t3 - t1))
    print("re:", re)
    print('----------------------')


if __name__ == '__main__':
    # n_leeter_word()
    optimize_n_letter_word(6, '/usr/share/dict/words')
    # extend_n_letter_word(6, '/usr/share/dict/words')
