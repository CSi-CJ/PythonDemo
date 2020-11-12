#!/usr/bin/env python
# -*- coding:utf-8 -*-
# owner:CSi
# datetime:2020/11/11 17:42
# software: PyCharm

# 浮点数
floatNum = 3.14159

print(floatNum, type(floatNum))

n1 = 1.1
n2 = 2.2
n3 = 2.1
print(n1 + n2)
print(n1 + n3)

# 解决浮点数相加不准确问题
from decimal import Decimal
print('use Decimal', Decimal('1.1') + Decimal('2.2'))


print(9//-4)
print(-9//4) #一正一负的整数公式，向下取整

print(9%-4) #公式： 余数 = 被除数-除数 * 商 9-(-4)*(-3)   -3
print(-9%4)  # -9 - 4 * (-3)   3