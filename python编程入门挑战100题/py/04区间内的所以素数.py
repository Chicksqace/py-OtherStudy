#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2022/1/17 14:54
# @Author : 不知天文，不知地理
# @File : 04区间内的所以素数.py
# 输入开始数字和结束数字，打印区间内所有的素数
#     比如：输入11和25，打印11——25的所以素数，包括25
# 素数：如果数字只能被1和自己整除就是素数，否则不是素数
#     比如3是素数，4不是素数
def is_primes(number):#判断是否为素数
    if number in (1,2):#number是1或者2，它肯定是一个素数
        return True
    for idx in range (2,number):#2到number-1如果有数被整除了，那么它就不是素数。不包含number本身
        if number % idx==0:
            return False
    return True
def print_primes(begin,end):#遍历区间
    for number in range(begin,end+1):#包含end
        if is_primes(number):#是素数
            print(f"{number} is a prime")
begin=11
end=25
print_primes(begin,end)#print_primes方法名，begin,end参数
