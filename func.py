#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 函数的定义,按照PEP 8规范,函数前应有两个空行
# 函数注释写在函数后面


def my_abs(x):
    if x >= 0:
        return x
    return -x


# 自定义abs函数


def my_abs_opt(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operate type')
    else:
        return my_abs(x)


# 优化my_abs,进行类型检查


def move(a, b):
    na = a * 10
    nb = b * 5
    return na, nb


# 返回多个值的方法(实质上是返回了一个tuple)


def my_power(x, n=2):
    t = 1
    while n > 0:
        t = t * x
        n = n - 1
    return t


# 默认参数值的定义


def enroll(name, gender, age=7, city='shanghai'):
    print('学生' + name + ',' + gender + ',' + str(age) + '岁,来自' + city)


# 多默认参数方法定义
# 定义默认参数要牢记一点：默认参数必须指向不变对象！


def calc(caller_name, *nums):
    print('调用者是:' + caller_name)
    temp = 0
    for i in nums:
        temp = temp + i * i
    print(temp)


# 可变参数定义,可变参数实际上是被当作数组来看待


def person(name, age, **kw):
    print("名字=" + name + ",年龄=" + str(age) + "," + str(kw))


# 定义关键字参数的函数,**kw表示该参数将以dict的形式接受,关键字参数是可选参数


def person_opt(name, age, *, city, job):
    print(name, age, city, job)


# 限制关键字参数名的函数(命名关键字函数)定义

def person_opt_(name, age, *args, city, job):
    print(name, age, args, city, job)


# 带有可变参数的命名关键字函数定义


def param_conbine(name, age, *args, city, job, **kwargs):
    print(name, age, args, city, job, kwargs)


# 参数组合,必须按照:[位置参数,可变参数,命名关键字参数,关键字参数] 的顺序来定义

# 递归函数:函数的自身调用
# 尾递归优化:
# 部分编程语言的解释器/编译器有尾递归优化的特性(python没有)
# 具体的优化方法是:
# 在函数返回时,调用方法本身,而非一个表达式
# 如果解释器/编译器可以尾递归优化,那么这种方法调用的栈帧只有一个
# 以阶乘函数来举例说明尾递归优化的方法
def fact(n):
    if n == 1:
        return n
    return n * fact(n - 1)


def fact_opt(n):
    return fact_help(n)


def fact_help(n, product=1):
    if n == 1:
        return product
    return fact_help(n - 1, n * product)
