#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2022/1/23 19:03
# @Author : 不知天文，不知地理
# @File : 10怎样对简单列表元素排序.py
# 怎样对简单列表排序？
# 简单列表：元素类型不是复合类型（列表/元组/字典）
# 形式1：【20,50,10,40,30】
# 形式2：【'bb','ee','aa','dd','cc'】
# 知识点
# 怎样原地排序？怎样不改变原列表排序？
# 怎样指定是升序还是降序排序？
lista=[20,50,10,40,30]
#lista.sort()#lista本身被改变了
listb=sorted(lista,reverse=True)
print(f"lista is {lista}")
print(f"lista is {listb}")