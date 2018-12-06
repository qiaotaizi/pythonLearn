#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
枚举
"""

__author__ = 'jaiz'

# 以月份的枚举为例
from enum import Enum, unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

# 枚举常量的引用
print(Month.Jan)

# 遍历枚举
# value属性是默认赋给成员的常量,从1开始
for name, member in Month.__members__.items():
    print(name, ',', member, ',', member.value)


# 定义枚举类
# unique装饰器可以帮助检查枚举类中的重复值
@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


# 枚举类中枚举值的调用
print(Weekday.Sun)
print(Weekday['Sat'])
print(Weekday(5))
# 遍历
for name, member in Weekday.__members__.items():
    print(name, ',', member, ',', member.value)
