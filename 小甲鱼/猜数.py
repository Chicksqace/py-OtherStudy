#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2022/1/11 21:04
# @Author : 不知天文，不知地理
# @File : 猜数.py
""" 用python设计第一个有些"""
import random
# answer=random.randint(1,10)
# counts=3
# while counts>0:
#     temp=input("不妨猜一下数")
#     guess=int(temp)
#     if guess==answer:
#         print("猜对了")
#         break
#     else:
#         if guess<answer:
#             print("小了")
#         else:
#             print("大了")
#     counts=counts-1
# answer_str=str(answer)
# print("游戏结束,答案是："+answer_str)
# counts=3
# while counts>0:
#     print("1")
#     counts=counts-1
x=random.getstate()#随机数内部生成器状态
#print(x)
y=random.randint(1,10)
print(y)
random.setstate(x)#setstate函数重新设置随机数生成器的内部状态
print(y)