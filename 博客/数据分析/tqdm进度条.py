#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2022/1/8 10:34
# @Author : 不知天文，不知地理
# @File : tqdm进度条.py
#tqdm 进度条  =  tqdm(iterator)
from tqdm import tqdm
from time import sleep
for i in tqdm(range(1000)):
    sleep(0.001)
print("完成")