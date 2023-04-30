#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2022/1/20 19:42
# @Author : 不知天文，不知地理
# @File : 07计算数字范围中所以的偶数.py
# 输入开始和结束值（不包含），得到所有偶数
# 偶数：能被2所整除的整数，是2的倍数
# 输入：begin=4，end=15
# 返回：【4,6,8,10,12,14,】
begin=4
end=15
def get_even_numbers(begin,end):
    result=[]
    for item in range(begin,end):
        if item%2==0:
            result.append(item)#满足列表元素被2整除，result添加这个元素
    return result
print(f"begin={begin},end={end},even numbers:",get_even_numbers(begin,end))
#列表推导式
data=[ item for item in range(begin,end) if item % 2==0]
print(f"begin={begin},end={end},even numbers:",data)