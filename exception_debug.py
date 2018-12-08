#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
异常处理与调试
"""
# 声明作者
__author__ = 'jaiz'

import logging

# python异常处理语法
try:
    print('try...')
    print(10 / 0)
except ZeroDivisionError as e:
    # 使用logging模块打印异常
    logging.exception(e)
else:
    print('else语句可有可无,如果没有抛出异常,else语句块中的逻辑会被执行')
finally:
    print('finally...')
print('END')


# python异常的基类是BaseException
# 当编写multi except语法时
# 如果父类异常先于子类异常被捕获
# 则子类异常的except语句则不会执行

# 自定义异常
class MyError(BaseException):
    pass


try:
    raise MyError('')
except BaseException as e:
    logging.exception(e)
finally:
    print('finally...')
print('END')


# 可以在except语句中再次使用不带参的raise语句抛出被捕获的异常,以便后续程序追踪
# 也可以使用带参raise语句抛出一个新的异常类型


# 调试
# assert:断言
# 调试时,遇到assert语句,会根据assert后面的布尔表达式判断
# 如果为true,程序继续执行
# 如果false,抛出AssertionError并打印布尔表达式后面的语句
# 可以使用python -0 xx.py在运行时忽略断言
def foo(x):
    y = 10 // x
    assert x != 0, 'x is 0'
    return y

# logging的4个级别
# debug,info,warning,error
# 使用logging.basicConfig(level=logging.XXXX)来指定输出的日志级别
# 低于指定级别的logging将被忽略

# pdb
# 使用python -m pdb xx.py
# 可以以debug模式运行python文件
# pdb模式命令:
# l:查看附近代码
# n:执行下一句
# p 变量名:查看变量值
# c:继续执行到下一个断点,如果没有断点,将文件执行到结尾并再次停止在第一行
# q:退出调试
# 在代码中使用
# import pdb
# pdb.set_trace()
# 可以在代码中指定断点
# 结合c命令,提高pdb调试的效率

# python单元测试,文档测试
# 略过
