#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2022/1/22 11:55
# @Author : 不知天文，不知地理
# @File : 09怎样对列表元素去重.py
# 输入，包含重复元素的原始列表：
# 【10,20,30,10,20】
# 返回：
# 【10,20,30】
def get_unique_list(lista):
    result=[]
    for item in lista:
        if item not in result:
            result.append(item)
    return result
lista=[10,20,30,10,20]
print(f"source list {lista},unique list:",get_unique_list(lista))
print(f"source list {lista},unique list:",list(set(lista)))#set函数是集合的概念，不会包含重复元素