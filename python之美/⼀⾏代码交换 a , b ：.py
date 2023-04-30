#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2022/4/6 16:39
# @Author : 不知天文，不知地理
# @File : ⼀⾏代码交换 a , b ：.py
#python中是没有变量的，所以int a=1 这种写法是错误的
a=1
b=2
print(a,b)
c=3
d=4
a,b=b,a
print(a,b)
