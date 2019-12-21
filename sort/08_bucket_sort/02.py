#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
桶排序

处理负数

[-45, -5, -2]
min: -45
max: -2
bucket_len: -2 - (-45) + 1 = 44

{
-45: 0
-44: 0
-43: 0
...
-2: 0
}

[0, 0,  0,  0, ..., 0]
-45 -44 -43 -42     -2

"""


def bucket_sort(my_list):
    result = []
    if len(my_list) <= 1:
        return my_list

    max_value = max(my_list)
    min_value = min(my_list)
    bucket_len = max_value - min_value + 1
    buckets = [0 for _ in range(bucket_len)]

    for i in my_list:
        buckets[i-min_value] += 1

    for index in range(bucket_len):
        for _ in range(buckets[index]):
            result.append(index-abs(min_value))

    return result


if __name__ == '__main__':
    unsorted = [2, 2, 3, 5]
    print(unsorted)
    print(bucket_sort(unsorted))

    unsorted = [2, 5, 3, 0, 2, 3, 0, 3]
    print(unsorted)
    print(bucket_sort(unsorted))

    unsorted = [0, 2, 2, 3, 5]
    print(unsorted)
    print(bucket_sort(unsorted))

    unsorted = []
    print(unsorted)
    print(bucket_sort(unsorted))

    unsorted = [-45, -5, -2]
    print(unsorted)
    print(bucket_sort(unsorted))
