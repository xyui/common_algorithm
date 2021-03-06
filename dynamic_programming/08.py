#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
https://mp.weixin.qq.com/s/usWZHQgF2c11Q-V34gMKKQ

给定一个三角形，找出自顶向下的最小路径和。
每一步只能移动到下一行中相邻的结点上。也就等同于，每一步我们只能往下移动一格或者右下移动一格

例如，给定三角形：

[

     [2],

    [3,4],

   [6,5,7],

  [4,1,8,3]

]

自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。

分析:
    0 1 2 3
    -------
0 | 2
1 | 3 4
2 | 6 5 7
3 | 4 1 8 3

opt(3, 3) -> 13+3 = 16
    opt(2, 3) -> None
    opt(2, 2) -> 6+7 = 13
        opt(1, 2) -> None
        opt(1, 1) -> 2+4 = 6
            opt(0, 1) -> None
            opt(0, 0) -> 2

opt(3, 2) -> 10+8 = 18
    opt(2, 2) -> 6+7=13
        opt(1, 2) -> None
            opt(0, 2) -> None
            opt(0, 1) -> None
        opt(1, 1) -> 2+4 = 6
            opt(0, 1) -> None
            opt(0, 0) -> 2
    opt(2, 1) -> 5+5 = 10
        opt(1, 1) -> 2+4 = 6
            opt(0, 1) -> None
            opt(0, 0) -> 2
        opt(1, 0) -> 2+3 = 5
            opt(0, 0) -> 2
            opt(0, -1) -> None

opt(3, 1) -> 10+1 = 11
    opt(2, 1) -> 5+5 = 10
        opt(1, 1) -> 2+4 = 6
            opt(0, 1) -> None
            opt(0, 0) -> 2
        opt(1, 0) -> 2+3 = 5
            opt(0, 0) -> 2
            opt(0, -1) -> None
    opt(2, 0) -> 5+6 = 11
        opt(1, 0) -> 2+3 = 5
            opt(0, 0) -> 2
            opt(0, -1) -> None
        opt(1, -1) -> None
            opt(0, -1) -> None
            opt(0, -2) -> None

opt(3, 0) -> 11+4 = 15
    opt(2, 0) -> 5+6 = 11
        opt(1, 0) -> 2+3 = 5
            opt(0, 0) -> 2
            opt(0, -1) -> None
        opt(1, -1) -> None
    opt(2, -1) -> None

"""
