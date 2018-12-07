#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
面向对象编程
使用元类
"""
# 声明作者
__author__ = 'jaiz'


# type函数的使用
# python的class是在运行期间动态声明的
# 使用type函数,既可以检测对象类型,也可以创建新的类
# 使用type创建类,在底层上与class定义类语法是一样的
class Hello(object):
    pass


hello = Hello()

print(type(hello))

print(type(Hello))


def say_hello(self):
    print('hello...')


def say_bye(self):
    print('bye...')


# 使用type动态创建类的语法:
# type('类名',(继承类数组),dict(类方法名=已定义的方法名))
Hello2 = type('Hello2', (object,), dict(h=say_hello, b=say_bye))

hello2 = Hello2()

hello2.h()

hello2.b()


# 使用metaclass(元类)
# 可将普通类理解为元类的实例
# 元类必须继承type
# 在元类中调用type()函数创建类
# python中使用元类的典型例子是编写orm框架

# 定义Field类,表示表字段与类成员的映射关系
class Field(object):
    def __init__(self, name, column_type):
        self.name = name;
        self.column_type = column_type

    def __str__(self):
        return '<%s%s>' % (self.__class__.__name__, self.name)


# 定义整型和字符串类型字段
class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')


class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')


# 编写元类
class ModelMetaClass(type):
    # new 方法
    # 参数表释义:
    # 参数0:要创建的类的对象
    # 参数1:类名
    # 参数2:继承类数组
    # 参数3:方法字典
    def __new__(cls, name, bases, attrs):
        # 排除对Model类的修改
        # 因为Model类会在下面使用class语法声明
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s==>%s' % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings  # 保存属性和列的映射关系
        attrs['__table__'] = name  # 假设表名和类型一致
        return type.__new__(cls, name, bases, attrs)


# 编写基类
class Model(dict, metaclass=ModelMetaClass):
    def __init__(self, **kwargs):
        super(Model, self).__init__(**kwargs)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError('\'Model\' object has no attribute \'%s\'' % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) valus (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('sql:', sql)
        print('args:', str(args))


# 编写一个继承Model的实体类
# 它可以调用save方法产生insert语句
class User(Model):
    id = IntegerField('id')
    name = StringField('name')
    email = StringField('email')
    password = StringField('password')


u = User(id=1, name='jzh', email='jzh@123.com', password='asf24sdf124')

u.save()
