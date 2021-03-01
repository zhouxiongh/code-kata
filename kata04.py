#!/usr/bin/env python
# -*- encoding=utf8 -*-
# Added by <zhouxiong.he@outlook.com>
# Added on 2021/3/1

"""
Data Munging
"""

# Part One: Weather Data
from itertools import islice


def min_temperature_spread(start=2, end=32):
    max_diff = 0
    with open('./data/weather.dat', 'r', encoding='utf-8') as f:
        for line in islice(f, start, end):
            row, max_temper, min_temper = process_line(line)
            diff_temper = max_temper - min_temper
            if diff_temper > max_diff:
                max_diff = diff_temper
                max_row = row
    return max_diff, max_row


#  return max temper and min temper
def process_line(line, tag=0, first=1, second=2):
    line_list = line.split()
    try:
        tag_name, first_f, second_f = line_list[tag].strip('.'), int(line_list[first].strip('*')), int(
            line_list[second].strip('*'))
    except Exception:
        # print('invalid line')
        return None
    else:
        return tag_name, first_f, second_f


# Part Two: Soccer League Table
def min_diff_goals(file, start, tag, first, second):
    max_diff = 0
    with open(file, 'r') as f:
        for line in islice(f, start, None):
            name, win_goals, lose_goals = process_line(line, tag, first, second)
            diff_goals = win_goals - lose_goals
            if diff_goals > max_diff:
                max_diff = diff_goals
                tag_name = name
    return tag_name, max_diff


# Part Three: DRY Fusion
def min_diff_xxx(file, start, tag, first, second):
    min_diff = 1000
    with open(file, 'r') as f:
        for line in islice(f, start, None):
            if not process_line(line, tag, first, second):
                continue
            name, win_goals, lose_goals = process_line(line, tag, first, second)
            diff_goals = abs(win_goals - lose_goals)
            if diff_goals < min_diff:
                min_diff = diff_goals
                tag_name = name
    return tag_name, min_diff


if __name__ == '__main__':
    max_rows, min_diff = min_diff_xxx('./data/weather.dat', 2, 0, 1, 2)
    print('min_diff value', min_diff, max_rows)
    r_name, min_diff = min_diff_xxx('./data/football.dat', 1, 1, 6, 8)
    print("min_diff value", min_diff, r_name)
