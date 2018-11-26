#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
面向对象编程
获取对象信息
类似于java反射
"""
# 声明作者
__author__ = 'jaiz'

import types
from types import MethodType


# 使用type函数获取类型(函数)信息

class MyClass(object):
    # 类变量的定义
    static_attr = 'static attr'

    def __init__(self):
        self.__att = 'ok'


mc = MyClass()

print(type(mc))
print(type(123))
print(type('123'))
print(type(123.22))


def fn():
    pass


# 使用types模块的类型常量
b = type(fn) == types.FunctionType
print(b)
# FunctionType(函数),BuiltinFunctionType(内建函数,如abs)
# LambdaType(lambda表达式),GeneratorType(生成器)

# isinstance(obj,class)方法
# 类似于java instanceof关键字
# 还可以判断一个对象是否是多个类型中的一种
print(isinstance([1, 2, 3], (list, tuple)))

# dir()方法
# 获取一个对象的所有方法和属性(包括类属性和实例属性)
print(dir(mc))

# getattr() setattr() hasattr()
# 判断对象是否有某个属性,并操作该属性
if hasattr(mc, '_MyClass__att'):
    setattr(mc, '_MyClass__att', 'okokok')
    print(getattr(mc, '_MyClass__att'))

# 可以在获取属性时填写默认值
print(getattr(mc, 'att', 'ojbk'))

# 类属性和实例属性如果重名,实例属性的值会覆盖类属性的值
# (以obj.attr的形式调用时会覆盖,但以Obj.attr的形式调用不会)
# 可以用del obj.attr删除属性
print(MyClass.static_attr)
del MyClass.static_attr


class MyClass2(object):
    pass


# python允许动态给实例绑定属性和方法
mc2 = MyClass2()
# 实例绑定属性
mc2.name = 'mc2'
print(mc2.name)


# 实例绑定方法
def set_age(self, age):
    self.age = age


mc2.set_age = MethodType(set_age, mc2)

mc2.set_age(20)

print(mc2.age)


# 给一个实例绑定方法,对另外一个实例时无效的
# 为了给所有实例绑定方法,可以给类绑定方法
def set_score(self, score):
    self.score = score


MyClass2.set_score = set_score

mc2.set_score(90)
print(mc2.score)


# 使用slots限制实例属性的绑定
class MyClass3(object):
    # 定义__slots__之后,对象只能绑定__slots__声明的属性
    # __slots__不会对继承的子类起作用
    # 但是如果子类也定义了__slots__
    # 那么子类的可绑定属性是父类__slots__和自身__slots__的并集
    __slots__ = ('name', 'age')


# 使用装饰器对属性进行限制
class MyClass4(object):

    def __init__(self):
        self._score = 0

    # 相当于get_score
    @property
    def score(self):
        return self._score

    # 相当于set_score
    # 如果不定义该方法的话,score视为只读属性
    @score.setter
    def score(self, score):
        if not isinstance(score, int):
            raise ValueError("分数必须是整数")
        if score > 100:
            raise ValueError("分数不能超过100")
        self._score = score

    @property
    def level(self):
        if self._score<60:
            return '不及格'
        elif self._score<90:
            return '良好'
        else:
            return '优秀'


mc4 = MyClass4()
mc4.score = 10
print(mc4.score)
print(mc4.level)
mc4.score = 100
print(mc4.level)
