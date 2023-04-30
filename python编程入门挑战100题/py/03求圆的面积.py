#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2022/1/16 14:36
# @Author : 不知天文，不知地理
# @File : 03求圆的面积.py
#输入半径，返回圆的面积
import math
def 计算圆的面积(半径):
    return round(math.pi*半径*半径,2)#return math.pi*半径*半径这样求出的小数长度比较长，保留俩位
print("圆的面积为",计算圆的面积(1))
print("圆的面积为",计算圆的面积(2))
print("圆的面积为",计算圆的面积(3))