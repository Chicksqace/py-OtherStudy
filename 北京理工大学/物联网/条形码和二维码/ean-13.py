#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2023/3/12 12:12
# @File : ean-13.py
import cv2
import numpy as np

def generate_ean13_code(country_code, manufacturer_code, product_code):
    # 计算校验码
    ean13_code = country_code + manufacturer_code + product_code
    check_code =str((10 - (3*int(ean13_code[0])+int(ean13_code[1])+3*int(ean13_code[2])+int(ean13_code[3])+3*int(ean13_code[4])+int(ean13_code[5])+3*int(ean13_code[6])+int(ean13_code[7])+3*int(ean13_code[8])+int(ean13_code[9])+3*int(ean13_code[10])+int(ean13_code[11])) % 10))
    ean13_code += check_code

    # 生成数字内容图像
    num_image = np.ones((50, 565, 3), dtype=np.uint8) * 255
    cv2.putText(num_image, ean13_code, (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)

    # 生成条形码图像
    code_image = np.ones((346, 565, 3), dtype=np.uint8) * 255

    # 生成左侧6个数字的条形码
    for i in range(6):
        binary_code = '{0:07b}'.format(int(ean13_code[i]))
        for j, bit in enumerate(binary_code):
            if bit == '1':
                cv2.rectangle(code_image, (5+(j+i*7)*5, 0), (5+(j+i*7)*5+5, 346), (0, 0, 0), -1)

    # 中间加入间隔线
    cv2.rectangle(code_image, (35*5, 0), (35*5+5, 346), (255, 255, 255), -1)

    # 生成右侧6个数字的条形码
    for i in range(6, 12):
        binary_code = '{0:07b}'.format(int(ean13_code[i]))
        for j, bit in enumerate(binary_code):
            if bit == '1':
                cv2.rectangle(code_image, (40+(j+(i-6)*7)*5, 0), (40+(j+(i-6)*7)*5+5, 346), (0, 0, 0), -1)

    # 合并数字内容和条形码图像
    code_image = np.concatenate((code_image,num_image), axis=0)

    return ean13_code, code_image

# 示例调用
code, image = generate_ean13_code('123', '4567', '7654321')
cv2.imshow('EAN-13 Code: {}'.format(code), image)
cv2.waitKey(0)
cv2.imwrite('me.png',image)
cv2.destroyAllWindows()
