#!/usr/bin/env python
# -*- encoding=utf8 -*-
# Added by <zhouxiong.he@outlook.com>
# Added on 2021/3/24

""" 
Tom Swift Under the Milkwood
http://codekata.com/kata/kata14-tom-swift-under-the-milkwood/
"""
from collections import defaultdict


def gen_dict(words):
    foo = defaultdict(tuple)
    for i in range(len(words) - 2):
        word1 = words[i]
        word2 = words[i + 1]
        word3 = words[i + 2]
        if word1 != ' ' and word2 != ' ' and word3 != ' ':
            if not foo[(word1, word2)]:
                foo[(word1, word2)] = []
            foo[(word1, word2)].append(word3)
    return foo


def gen_text(start, d, max_size=100):
    text = ' '.join(start)
    prev, cur = start
    next_words = d[(prev, cur)]
    next_word = max(next_words, key=next_words.count)
    while next_word:
        if len(text.split(" ")) > max_size:
            break
        text = text + " " + next_word
        prev, cur = cur, next_word
        next_words = d[(prev, cur)]
        next_word = max(next_words, key=next_words.count)

    return text


if __name__ == '__main__':
    input_text = "it was in the wind that was what he thought was his companion. I think would be a good one and accordingly the ship their situation improved. Slowly so slowly that it beat the band! You’d think no one was a low voice. “Don’t take any of the elements and the inventors of the little Frenchman in the enclosed car or cabin completely fitted up in front of the gas in the house and wringing her hands. “I’m sure they’ll fall!” She looked up at them. He dug a mass of black vapor which it had refused to accept any. As for Mr. Swift as if it goes too high I’ll warn you and you can and swallow frequently. That will make the airship was shooting upward again and just before the raid wouldn’t have been instrumental in capturing the scoundrels right out of jail"
    words_dict = gen_dict(input_text.split())
    print(words_dict)
    start_words = ("it", "was")
    print(words_dict[start_words])
    output_text = gen_text(start_words, words_dict)
    print(output_text)

