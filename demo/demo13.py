#!/usr/bin/env python
# -*- coding:utf-8 -*-
# owner:CSi
# datetime:2020/11/12 16:46
# software: PyCharm

# 可变参数列表 *name: 可以接受多个参数  **name: 可以接受key-value多个参数


def cheeseshop(kind, *arguments, **keywords):
    a = ['a', 'b', 'c', 'd', 'A', 'B']
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    keys = sorted(keywords.keys())
    for kw in keys:
        print(kw, ":", keywords[kw])


cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")
