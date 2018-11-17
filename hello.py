#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释
# 第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。
# 申明了UTF-8编码并不意味着你的.py文件就是UTF-8编码的，必须并且要确保文本编辑器正在使用UTF-8 without BOM编码

# 导入外部文件
import func

# from filename import fun1,fun2
# 也可以以这种语法显式导入文件中的几个方法

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
t = (1, 2, 3, 4)
print(t)
# 只有一个元素的数组的写法
t1 = (1,)
print(t1)

# if/else
age = 25
if age > 17:
    print("adult")
else:
    print("child")

# if/elif/else
if age > 17:
    print("adult")
elif age > 6:
    print("teenager")
else:
    print("kid")
# 任意变量也可以作为if的条件,变量是非零数值\非空字符串\非空list时就是True,否则为False

# input接收的值类型是字符串
# int(s)将字符串转型为数值类型

# for循环
for name in classmates:
    print(name)

for num in t:
    print(num)

# 用range方法生成整数序列 并转化为list
print(list(range(5)))

# 循环的break/continue

# while循环
n = 0
while n < 10:
    n = n + 1
    print(n)

# 字典
d = {'k1': 'v1', 'k2': 'v2'}
print(d)
# 获取值的两种方式:d[key]不安全,如果key不存在会报错,d.get(key)会返回空值
print(d['k1'])
print(d.get('k2'))
# 检查字典是否包含元素
print('k3' in d)
# 删除元素
d.pop('k1')

# set
# set声明有两种语法,idea推荐下面这种
# s = set([1, 2, 2, 2, 3, 4])
s = {1, 2, 2, 2, 3, 4, 'ok'}
print(s)
s.add(5)
print(s)
s.remove(4)
print(s)
# s1 & s2 :求交集  s1 | s2 :求并集

# 函数的别名调用
a = abs
print(a(-1))

# 自定义函数的调用(引用语句在文件头)
print(func.my_abs(-1))

# 用作占位符的pass语句
num = -1
if num > 0:
    # 这里如果没有pass,解释器会报错
    pass
else:
    print(num)

# 返回多个值的函数,其实是返回一个数组
print(func.move(10, 5))

# 函数的默认参数
print(func.my_power(2, 4))
print(func.my_power(2))

# 一个函数中定义多个默认参数
func.enroll('小明', '男')
func.enroll('小华', '男', 8)
func.enroll('小强', '男', city='beijing')
func.enroll('小刚', '男', 9, city='beijing')

# 可变参数函数
func.calc('姜志恒', 1, 2, 3, 4, 5)
func.calc('姜志恒')

# 可变参数函数可以以下面的形式传递List/tuple/set参数
nums = [1, 2, 3, 4, 5]
func.calc('姜志恒', *nums)
nums_ = (1, 2, 3)
func.calc('姜志恒', *nums_)
nums__ = {1, 2, 3, 4, 5}
func.calc('姜志恒', *nums__)

# 关键字参数函数调用
func.person('姜志恒', 15)
func.person('周洁', 14, 学历='中专')
extra = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
func.person('姜志恒', 15, **extra)

# 限制关键字参数名的函数调用
func.person_opt('姜志恒', 15, city='shanghai', job='teacher')
extra = {'city': 'beijing', 'job': 'engineer'}
func.person_opt('姜志恒', 15, **extra)

# 带可变参数的命名关键字函数的调用
func.person_opt_('姜志恒', 15, **extra)
func.person_opt_('姜志恒', 15, 1, 2, 3, **extra)
func.person_opt_('姜志恒', 15, *nums, **extra)

# 参数组合的调用
func.param_conbine('姜志恒', 15, 1, 2, 3, city='shanghai', job='driver', k1='v1', k2='v2')

# 任何一个方法的调用,都可以归结为以下传参:
# method(*args,**kw)
arr = ('姜志恒', 15, 1, 2, 3)
di = {'city': 'shanghai', 'job': 'driver', 'k1': 'v1', 'k2': 'v2'}
func.param_conbine(*arr, **di)

print(func.fact(4))

print(func.fact_opt(4))
