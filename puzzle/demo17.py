#!/usr/bin/env python
# -*- coding:utf-8 -*-
# owner:CSi
# datetime:2020/11/12 17:42
# software: PyCharm

# 4.7.7. 函数注解
def f(ham: 42, eggs: int = 'spam') -> "Nothing to see here":
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)


f('wonderful')
