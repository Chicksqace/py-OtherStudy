#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2023/3/14 14:39
# @File : Pyzbar.py
import cv2
from pyzbar import pyzbar
# 读图片
img = cv2.imread('code39.png')
# 解码条码
decoded_objects = pyzbar.decode(img)
# 打印解码结果
for obj in decoded_objects:
    print('Type:', obj.type)
    print('Data:', obj.data.decode())