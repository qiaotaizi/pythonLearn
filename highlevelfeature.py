#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python高级特性

# 切片

# 取出tuple\list\字符串\dict的一部分

L = list(range(100))

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


