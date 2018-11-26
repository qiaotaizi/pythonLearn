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

    # 类私有变量__xxx
    # 私有变量无法直接从外部进行访问
    # 需要通过get_xxx()/set_xxx(xx)来进行读写
    # 解释器会将私有变量__xxx解释为_classname_xxx
    # 从外部可以直接访问_classname_xxx来读写私有变量
    # 但是不建议这样做

    # __init__方法,相当于java带参构造
    # 第一个参数必须是self
    def __init__(self, name='', score=0):
        # self.name = name
        # self.score = score
        self.__name = name
        self.__score = score

    # 类方法的定义
    def print_score(self):
        print(self.__name, '的分数是:', self.__score)

    # get/set方法定义
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        self.__score = score


# 类对象的实例化
lily = Student()
print(lily)

# 可以给对象绑定任意属性
lily.age = 20
print(lily.age)

# 调用带参构造
lily = Student('lily', 90)
print(lily.get_name(), lily.get_score())

lily.print_score()

# get/set方法调用
lily.set_name('liu')
lily.set_score(89)
lily.print_score()
