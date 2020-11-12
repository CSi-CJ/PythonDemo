#!/usr/bin/env python
# -*- coding:utf-8 -*-
# owner:CSi
# datetime:2020/11/12 16:09
# software: PyCharm

# for语句
words = ['gzl', 'lml', 'wsl']
for val in words:
    print(val, len(val))

for v in words[:]:
    if v == 'wsl':
        words.insert(0, v)
print(words)

# range()函数
for i in range(5):
    print(i)
    # 生成一个链表
for num in range(5, 10):
    print(num)

for nu in range(0, 10, 3):
    print(nu)
