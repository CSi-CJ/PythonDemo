#!/usr/bin/env python
# -*- coding:utf-8 -*-
# owner:CSi
# datetime:2020/11/12 16:22
# software: PyCharm


seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print(list(enumerate(seasons)))
print(list(enumerate(seasons, start=2)))


def enumerate(sequence, start=0):
    n = start
    for elem in sequence:
        yield n, elem
        print(n, elem)
        n += 1


enumerate(seasons)
