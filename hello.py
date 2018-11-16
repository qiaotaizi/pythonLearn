#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释
# 第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。
# 申明了UTF-8编码并不意味着你的.py文件就是UTF-8编码的，必须并且要确保文本编辑器正在使用UTF-8 without BOM编码

# ctrl+alt+L快速格式化代码

# python中的空格/tab缩进很重要
print('hello, python')
print('hello,', 'i\'m', 'jaiz')

# r表示后面的字符默认不转义,有缺陷,如果字符串最后追加一个\,解释器文认为要转义最后的引号
print(r'\t\n\r\\\\')

# 字符串换行
print('''ok,
ok, ok
ok, ok
ok''')

# boolean值
print(True)
print(False)
print(1 > 2)
# 使用and or not进行且或非运算
print(True and False)
print(True or False)
print(not False)

# 空值
print(None)

# 除和地板除
print(10 / 3)
# 结果3.3333....
print(10 // 3)
# 结果3

# 字符和整数互换
print(ord('a'))
print(chr(66))
print(ord('中'))

# 16进制表示字符
print('\u4e2d\u6587')

# 解释一下
# '中'->20013(10进制)->01001110,00101101(2进制)->4e2d(16进制)

# 字符(串)转字节,只能转ASCII码中包含的字符集
print(b'a')

# 以特定编码将字符转化字节
print('abc'.encode('ascii'))
print('中文'.encode('utf-8'))

# 解码
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
# 解码时忽略少量编码错误
print(b'\xe4\xb8\xad\x96\x87\xe4\xb8\xad\xe6\x87'.decode('utf-8', errors='ignore'))

# 字符串长度
print(len('ABC'))

# 格式化输出
print('%%亲爱的%s您好,您是第%d位用户,id:%03d,您的话费余额是%.2f%%' % ('jaiz', 1, 1, 50.1))
print('%亲爱的{0}您好,您是第{1:d}位用户,id:{2:03d},您的话费余额是{3:.2f}%'.format('jaiz', 1, 1, 50.1))

# list 相当于java中的List
classmates = ['小明', '小华', '小强', '小刚']
print(classmates)
print(len(classmates))
print(classmates[0])
# 索引值为负数时表示倒叙获取list中的内容,注意数值过小时也会越界
print(classmates[-1])
# list末尾追加
classmates.append('小丽')
print(classmates)
# list指定位置插入
classmates.insert(1, '小黑')
print(classmates)
# list删除末尾元素
classmates.pop()
print(classmates)
# list删除指定位置元素
classmates.pop(1)
print(classmates)
# list元素可以不同类型,list也可以是另一个list的元素

# tuple 相当于java中的数组
t = (1, 2)
print(t)
# 只有一个元素的数组的写法
t1 = (1,)
print(t1)
