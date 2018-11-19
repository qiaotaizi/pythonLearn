#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import Iterable, Iterator
import os

# python高级特性

# 切片

# 取出tuple\list\字符串\dict的一部分

L = list(range(30))

# 取出0-2的元素(有头没有尾)
print(L[0:3])

# 如果起始索引是0,可以省略
print(L[:3])

# 倒序切片
print(L[-3:-1])
# 同理,如果要取到最后一个元素,:后面的索引可省略
print(L[-3:])

# 倒序切片时,且冒号两端都有值时,两个值都为负数
print(L[-3:1])

# 每隔n个元素取值的切片方式
print(L[10:20:2])
print(L[:20:5])
print(L[::10])
# 复制list
print(L[:])

# 迭代
# for循环可以用于list/tuple/set/dict/字符串/生成器等所有可迭代的对象上
# 例如dict的迭代
d = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
for key in d:
    print(key)

# 迭代dict的value
for value in d.values():
    print(value)

# 同时迭代key和value
for k, v in d.items():
    print(k, '=', v)

# 迭代字符串
for c in 'hello':
    print(c)

# from collections import Iterable
# 使用Iterable判断对象是否可迭代
print(isinstance('hello', Iterable))
print(isinstance([1, 2, 3], Iterable))
print(isinstance(123, Iterable))

# 在遍历时获取索引
for i, e in enumerate([1, 2, 3, 4, 5, 6]):
    print('第', i, '个值是:', e)

# 列表生成式
# 一种生成列表的简洁语法
# 结构为:[表达式 for循环1 for循环2 ... if语句]
# 生成[1*1,2*2,....,10*10]
print([n * n for n in range(1, 11)])
# 仅生成偶数的平方
print([n * n for n in range(1, 11) if n % 2 == 0])
# 两层循环嵌套
print([m + n for m in 'ABC' for n in 'XYZ'])
# 获取目录下所有文件和目录
print(os.listdir('G:/py'))
print([d for d in os.listdir('G:/py')])

# 生成器
# generator保存列表生成的算法
# 在遍历中不断推算下一个元素的值
# 而不是立刻生成一个数组/列表
# 可以起到节约内存的作用
g = (x * x for x in range(1, 11) if x % 2 == 0)
for y in g:
    print(y)


# 也可以用next(g)获取下一个值


# yield和generator
# 例如写一个斐波那契数列函数
def fib(m):
    n, a, b = 0, 0, 1
    while n < m:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'


print('测试fib')
fib(6)


# 将fib函数改写为一个generator
def fib_g(m):
    n, a, b = 0, 0, 1
    while n < m:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


gg = fib_g(6)
print('测试fib_g')
for x in gg:
    print(x)


# fib_g和fib的区别在于,fib顺序执行,遇到return时返回结果,
# fib_g在next()调用时执行,遇到yield返回结果,在下次next()调用时,从之前执行停止的地方继续执行

# generator函数也有返回值,在所有yield执行结束后,再度next()调用时,该返回值会包含在StopIteration错误中


# 练习:杨辉三角生成器
def triangles():
    lt = [1]
    while True:
        yield lt
        lt = [1] + [lt[n] + lt[n + 1] for n in range(len(lt) - 1)] + [1]


g_triangles = triangles()

for i in range(0, 11):
    print(next(g_triangles))

# Iterable和Iterator
# 可以直接作用于for循环的对象统称为可迭代对象,使用isinstance(x,Iterable)判断是否时可迭代对象
# 可以被next()调用,不断返回下一个值的对象成为迭代器,使用isinstance(x,Iterator)判断是否是迭代器
# 可以使用iter()方法将Iterable转化为Iterator
print(isinstance([], Iterable))
print(isinstance([], Iterator))
print(isinstance(iter([]), Iterator))
# Iterator表示的对象是一个数据流,无法知道流的长度,但可以通过next()不断获取下一个对象
# Iterable对象无法表示整个自然数集等元素数量为无穷的集合,但Iterator对象可以
