#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# python模块
# 每个.py文件都是一个模块
# 自定义模块时,函数名尽量不要与内建模块函数名冲突
# 为了避免模块名冲突，Python又引入了按目录来组织模块的方法，称为包（Package）
# 每一个包目录下面都会有一个__init__.py的文件，这个文件是必须存在的，否则，Python就把这个目录当成普通目录
# 模块名不要和系统模块名冲突，最好先查看系统是否已存在该模块，
# 检查方法是在Python交互环境执行import abc，若成功则说明系统存在此模块。
# 这个文件的第一行和第二行是标准注释
# 创建文件注释
"""
my first module
"""
# 声明作者
__author__ = 'jaiz'
# 以上就是一个python文件的标准模板
import sys


def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello, world!')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')


# 运行测试的方式(相当于main方法)
if __name__ == '__main__':
    test()

# 变量/函数命名
# 普通变量,如abc,a123,PI等
# 特殊变量,__name__名称,__author__作者,__doc__文档注释 等等
# 私有变量/函数,如_xxx和__xxx,虽然也可以引用,但是习惯上不应该引用私有变量
# python无法限制私有变量和函数的引用

# 第三方模块的安装
# 1.使用pip命令一个一个安装
# 2.使用Anaconda
