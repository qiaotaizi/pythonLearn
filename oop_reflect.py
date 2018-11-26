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
