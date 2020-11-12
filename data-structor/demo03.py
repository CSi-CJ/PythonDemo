#!/usr/bin/env python
# -*- coding:utf-8 -*-
# owner:CSi
# datetime:2020/11/12 18:12
# software: PyCharm

# 列表推导式
squares = []
for x in range(10):
    squares.append(x ** 2)

print(squares)

squares = list(map(lambda x: x ** 2, range(10)))
print(squares)

squares = [x ** 2 for x in range(10)]

arr = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(arr)

combs = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combs.append((x, y))

print(combs)
