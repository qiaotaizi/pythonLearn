#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
面向对象编程
继承与多态
"""
# 声明作者
__author__ = 'jaiz'


# 基类:object

# 父类的定义
class Animal(object):
    def run(self):
        print('animal is running')


# 子类的定义
class Dog(Animal):
    # 覆盖(重写)
    def run(self):
        print('Dog is running')


class Cat(Animal):
    def run(self):
        print('Cat is running')


animal = Animal()
animal.run()
animal = Dog()
animal.run()
animal = Cat()
animal.run()


def animal_run(a):
    a.run()


animal_run(animal)


# 鸭子类型:
# 一只鸟,只要它叫起来像鸭子,跑起来像鸭子,游泳时像鸭子,我们就认为它是只鸭子
# 对于类似python的动态语言,
# 方法在传参和定义时,编译器(解释器)不会立刻检查参数的类型,
# 仅关注方法的调用,如果传入一个对象,该对象没有调用的方法,
# 则会在运行期抛出异常.

# 多继承(MixIn)
# 例如Tiger继承了Animal类,同时还要继承Runable(可奔跑)和Carnivorous(肉食性)
# 就可以这样设计
class RunableMixIn(object):
    def move(self):
        print("move as run")


class CarnivorousMixIn(object):
    def eat(self):
        print("eat meat")


class Tiger(Animal, RunableMixIn, CarnivorousMixIn):
    pass


tiger = Tiger()

tiger.run()
tiger.move()
tiger.eat()
