#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2022/1/21 13:25
# @Author : 不知天文，不知地理
# @File : 08移除列表的多个元素.py
# 输入：
# 原始列表：【3,5,7,9,11,13】
# 移除元素：【7,11】
# 返回：
# 【3,5,7,9,13】
def remove_elements_from_list(lista,listb):
    for item in listb:
        lista.remove(item)
    return lista
lista=[3,5,7,9,11,13]
listb=[7,11]
print(f"from {lista} remove {listb},result : ",remove_elements_from_list(lista,listb))
data=[item for item in lista if item not in listb]#lista中的元素没有在listb中就返回item
print(f"from {lista} remove {listb},result : ",data)