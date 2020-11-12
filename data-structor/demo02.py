#!/usr/bin/env python
# -*- coding:utf-8 -*-
# owner:CSi
# datetime:2020/11/12 17:51
# software: PyCharm


#  把列表当作队列使用

from collections import deque

queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")  # Terry arrives
queue.append("Graham")  # Graham arrives
print(queue.popleft())  # The first to arrive now leaves
'Eric'
print(queue.popleft())  # The second to arrive now leaves
'John'
print(queue)  # Remaining queue in order of arrival
deque(['Michael', 'Terry', 'Graham'])
