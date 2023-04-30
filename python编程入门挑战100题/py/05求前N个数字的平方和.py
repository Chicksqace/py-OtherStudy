#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2022/1/18 15:24
# @Author : 不知天文，不知地理
# @File : 05求前N个数字的平方和.py
# 输入：数字N
# 计算：1^2+2^2+……+N^
def sum_of_square(n):
    result= 0
    for number in range(1,n+1):
        result+=number*number
    return result
print("sum of square 3:",sum_of_square(3))
print("sum of square 6:",sum_of_square(6))
print("sum of square 9:",sum_of_square(9))

