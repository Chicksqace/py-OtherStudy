#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2023/3/12 12:22
# @File : cv2_test1.py
import numpy as np
import cv2

img=np.zeros((200,400,3),np.uint8)
# 最后以为0 代表的是蓝通道 1代表的是绿通道 2代表红通道
img[0:100,0:200,0]=255
# 第一个参数是高度 第二个是宽度
img[100:200,0:200,1]=255
# 灰
img[0:100,200:400,0]=128
img[0:100,200:400,1]=128
img[0:100,200:400,2]=128

img[100:200,200:400,2]=255

cv2.imshow('color',img)
cv2.waitKey(0)


