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


# 面向对象的几个特殊方法
class MyClass(object):
    def __init__(self, name):
        self.name = name

    # __str__相当于java toString
    def __str__(self):
        return 'Student object (name:%s)' % self.name

    # 类似于__str__,但用于调试的__repr__
    __repr__ = __str__

    # 定义__iter__方法后对象可以被迭代
    # 要和__next__方法一起定义
    # __getitem__方法使得对象获得根据下标获取元素和切片的能力,类似于list
    # __iter__,__next__和__getitem__的应用参考下方Fib类
    def __iter__(self):
        pass

    def __next__(self):
        pass

    def __getitem__(self):
        pass


print(MyClass('Micheal'))


class Fib(object):
    # init方法定义两个初始值
    def __init__(self):
        self.a = 0
        self.b = 1

    def __iter__(self):
        # 实例本身就是迭代对象,返回自己
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        # 停止遍历的条件
        if self.a > 1000:
            raise StopIteration()
        return self.a

    # list可能根据索引获取单个元素,也可能根据切片获取一个新的list
    # 要使得自己Fib类实例获取切片的能力
    # 需要这样编写getitem
    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L


# 构造函数返回可迭代对象,直接用于for循环
# 每次循环调用__next__函数获取下一个值
fib = Fib()
for n in fib:
    print(n)

print(fib[10])

print(fib[5:10])
