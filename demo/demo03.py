#!/usr/bin/env python
# -*- coding:utf-8 -*-
# owner:CSi
# datetime:2020/11/12 15:04
# software: PyCharm
x = int(input("please enter an integer: "))
if x < 0:
    x = 0
    print('Negative changed to zero')
if x == 0:
    print('zero')
if x > 0:
    print('CNM')