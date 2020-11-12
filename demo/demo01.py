#!/usr/bin/env python
# -*- coding:utf-8 -*-
# owner:CSi
# datetime:2020/11/11 17:42
# software: PyCharm

# 变量多次赋值
name = '关之琳'
name = '林美玲'

print(name)
# 当变量被多次赋值之后，内存空间的指向会发生变化，之前不再被引用的值将会在内存中变成内存垃圾，会被python的回收机制回收