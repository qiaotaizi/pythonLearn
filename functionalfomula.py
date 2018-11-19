#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import reduce


# 函数式编程


# 变量可以指向函数
def func(x, y, f):
    return f(x) + f(y)


# 像是C#委托语法
print(func(-1, -5, abs))


# map和reduce
# map(function,Iterable)
# 将function作用于Iterable中的所有元素,并将结果作为新的Iterator返回
def f(x):
    return x * x


ll = [1, 2, 3, 4, 5, 6, 7]
print(list(map(f, ll)))


# reduce(function,list)
# 将一个接收两个参数的方法作用于list中的前两个值,计算的结果和list的第三个值再次传入function....
# reduce位于functools,使用时注意引用
# 例如使用reduce可以这样求和
def add(x, y):
    return x + y


print(reduce(add, ll))


# 再例如:定义一个将字符串转换为数字的函数
def str2int(string):
    def str2int_(e):
        digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        return digits[e]

    def combine_num(num1, num2):
        return num1 * 10 + num2

    return reduce(combine_num, list(map(str2int_, string)))


# 使用lambda表达式,使str2int函数的定义达到最简
def str2int_simple(s):
    DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

    def char2num(c):
        return DIGITS[c]

    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


print(str2int('102746531'))
print(str2int_simple('102746531'))


# filter
# map/reduce/filter类似于java8的流操作
# filter(fucntion,list)
# 将list中的元素依次传入function,根据返回的boolean值,决定是否保留该元素,并返回一个新的Iterator
def odd(x):
    return x % 2 == 0


print(list(filter(odd, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

# sorted
# sorted(list,key=function,reverse=True/False)
# 返回排序后的list,可选参数key,可以指定排序规则,可选参数reverse,指定是否倒序排列,默认为false
l = [1, 9, 0, 3, -7]
print(sorted(l))
print(sorted(l, key=abs))

# 练习,根据名字/成绩重新排列下面的list
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
    return str.lower(t[0])


def by_score(t):
    return t[1]


print(sorted(L, key=by_name))
print(sorted(L, key=by_score, reverse=True))
