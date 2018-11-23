#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
面向对象编程
"""
# 声明作者
__author__ = 'jaiz'


# 类的声明:
# class类型(继承类):
class Student(object):
    # pass
    # __init__方法,相当于java带参构造
    # 第一个参数必须是self
    def __init__(self, name, score):
        self.name = name
        self.score = score


# 类对象的实例化
lily = Student()
print(lily)

# 可以给对象绑定任意属性
lily.age = 20
print(lily.age)

# 调用带参构造

