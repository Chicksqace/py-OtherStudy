#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2022/1/19 13:47
# @Author : 不知天文，不知地理
# @File : 06计算列表数字的和.py
# Input:[1,2,3,4]OutPut:10
# Input:[17,5,3,5]OutPut:30
def sum_of_list(param_list):
    total = 0
    for item in param_list:
        total+=item
    return total


list1 = [1, 2, 3, 4]
list2 = [17, 5, 3, 5]
print(f"sum of {list1},",sum_of_list(list1))
print(f"sum of {list2},",sum_of_list(list2))
print(f"sum of {list1},",sum(list1))
print(f"sum of {list2},",sum(list2))

