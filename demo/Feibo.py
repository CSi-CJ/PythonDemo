#!/usr/bin/env python
# -*- coding:utf-8 -*-
# owner:CSi
# datetime:2020/11/12 14:57
# software: PyCharm



# a, b = 0, 1
# while a < 10000:
#     print(a, end=',')
#     a, b = b, a + b


def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
fib(20)