#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import reduce
import functools


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


# 函数作为返回值(闭包)
def lazy_sum(*args):
    def sum_():
        return reduce(add, args)

    return sum_


f = lazy_sum(1, 2, 3, 4, 5, 6)
print(f())


# 在函数中定义函数,内层函数可以调用外层函数的参数和局部变量,且内层函数作为外层函数的返回值,这种结构称为闭包
# 在上面的例子中,变量f在定义时指向了lazy_sum返回的函数,当f()被调用时,才真正执行计算
# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。


# 练习:闭包实现计数器
def create_counter():
    i = [0]

    def count():
        i[0] += 1
        return i[0]

    return count


counter = create_counter()
print(counter(), counter(), counter())

counter_ = create_counter()
print(counter_(), counter_(), counter_(), counter_())


# 匿名函数:lambda表达式语法
# 可以简化代码,无需担心方法名冲突
# 例如
def is_odd(n):
    return n % 2 == 1


L = list(filter(is_odd, range(1, 20)))

print(L)
# 使用lambda简化后
print(list(filter(lambda n: n % 2 == 1, range(1, 20))))


# 装饰器
# 闭包结构实现类似spring aop语法
def log(func):
    def wrapper(*args, **kw):
        print('call %s ():' % func.__name__)
        obj = func(*args, **kw)
        print('%s ()的返回值是:' % func.__name__, obj)
        return obj

    return wrapper


# __name__获取函数名


@log
def now():
    print('现在时间是:', '2018年11月20日', '16点33分')


now()

# @log
# def now():
#       ...
# 相当于执行了语句:
# now=log(now)
print('====')


# 装饰器本身也可以支持传递额外参数
# 需要将装饰器函数再进行一层闭包
def log(text='execute'):
    def decorator(funct):
        def wrapper(*args, **kwargs):
            print('%s %s' % (text, funct.__name__))
            return funct(*args, **kwargs)

        return wrapper

    return decorator


@log('execute')
def now_():
    print('ok')


now_()
# 3层嵌套的装饰器,相当于执行now_=log('execute')(now_)
# log('execute')返回decorator函数
# 再用decorator(now_)将now_函数作为参数传入

# 无论是两层装饰器还是三层装饰器
# 最后都是返回一个wrapper函数
print(now_.__name__)
print('===========')


# 打印结果也是wrapper
# 使用python内建装饰器
# @functools.wraps来恢复函数名


def log_final(text='execute'):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print('%s %s' % (text, func.__name__), '参数:', args, kwargs)
            return func(*args, **kwargs)

        return wrapper

    return decorator


@log_final('call')
def say(text, *, job):
    print('say %s' % text)
    print(job)


say('你好', job='okok')
print(say.__name__)
print('===')

# 偏函数
# 使用functools.partial创建偏函数
# 把一个函数的部分参数固定住(也就是设置默认值),返回一个新的函数,新函数的调用更加简单
# 例如:
int2 = functools.partial(int, base=2)

print(int2('110110101'))
