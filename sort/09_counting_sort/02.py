#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
计数排序

https://juejin.im/post/5cac107ee51d456e7079f1d5

collection: [-5, -2, 2, 5, 3, 0, 2, 3, 0, 3]
result: [None, None, None, None, None, None, None, None, None, None]
min_value: -5
max_value: 5
c: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
c: [1, 0, 0, 1, 0, 2, 0, 2, 3, 0, 1]
    0  1  2  3  4  5  6  7  8  9  10
   -5 -4 -3 -2 -1  0  1  2  3  4  5
c: [1, 1, 1, 2, 2, 4, 4, 6, 9, 9, 10]
[-5, -2, 0, 0, 2, 2, 3, 3, 3, 5]


collection: [6, 1, 2, 7, 9, 3, 4, 5, 10, 8]
result: [None, None, None, None, None, None, None, None, None, None]
min_value: 1
max_value: 10
c: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
c: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    0  1  2  3  4  5  6  7  8  9
    1  2  3  4  5  6  7  8  9  10
c: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

"""


def counting_sort(collection):
    # print('collection: %s' % collection)
    if len(collection) <= 1:
        return collection

    result = [None] * len(collection)
    min_value = min(collection)
    max_value = max(collection)
    # print('result: %s' % result)
    # print('min_value: %s' % min_value)
    # print('max_value: %s' % max_value)

    c = [0] * (max_value - min_value + 1)
    # print('c: %s' % c)

    for number in collection:
        c[number - min_value] += 1
    # print('c: %s' % c)

    for i in range(len(c)):
        if i > 0:
            c[i] = c[i] + c[i-1]
    # print('c: %s' % c)

    for number in collection:
        result[c[number - min_value]-1] = number
        c[number - min_value] -= 1

    return result


if __name__ == '__main__':
    for unsorted in [
        [], [0], [2], [3, 5], [5, 3], [5, 5], [0, 0, 0, 0], [1, 1, 1, 1], [2, 2, 3, 5],
        [2, 5, 3, 0, 2, 3, 0, 3], [0, 2, 2, 3, 5],
        [103, 9, 1, 7, 11, 15, 25, 201, 209, 107, 5],
        [6, 1, 2, 7, 9, 3, 4, 5, 10, 8], [0, 2, 2, -6, -1, 3, 5],
        [-45, -2, -5]
    ]:
        print(unsorted)
        print(counting_sort(unsorted))
        print()
