#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2023/3/12 15:01
# @File : 解码.py
import cv2
from pyzbar import pyzbar

# 读取图像
# 解码2.1中自己生成的EAN-13码
img = cv2.imread('ldn20212013225.png')
# 解码3.2中使用barcode库生成的39码
img_32 = cv2.imread('ldn20212013225_32.png')
# 解码4.2中生成的二维码
img_4 = cv2.imread('qr2.png')

# 解码条码
# decoded_objects = pyzbar.decode(img)
# decoded_objects = pyzbar.decode(img_32)
decoded_objects = pyzbar.decode(img_4)

# 打印解码结果
for obj in decoded_objects:
    print('Type:', obj.type)
    print('Data:', obj.data.decode())

