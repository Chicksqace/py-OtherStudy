#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2022/1/28 16:11
# @Author : 不知天文，不知地理
# @File : 15统计目录下所有文件大小.py
import os
print(os.path.getsize("英文.txt"))

sum_size=0
for file in os.listdir("."):
    if os.path.isfile(file):#判断是目录还是普通文件，过滤
        sum_size+=os.path.getsize(file)

print("all of dir :",sum_size/1024)#将B转换为kb