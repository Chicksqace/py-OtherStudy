#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2023/3/12 14:49
# @File : qrcode_test.py
import qrcode
# 4.1 使用默认模式生成二维码
content1 = 'ldn20212013225'
qr1 = qrcode.QRCode()
qr1.add_data(content1)
qr1.make()
img1 = qr1.make_image()
img1.save('qr1.png')

# 4.2 指定二维码的尺寸位最大177*177，校验等级为最高
content2 = 'http://www.zjiet.edu.cn/'
qr2 = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr2.add_data(content2)
qr2.make(fit=True)
img2 = qr2.make_image(fill_color="black", back_color="white")
img2.save('qr2.png')

# 4.3 自由调整边框像素值、二维码颜色等内容
content3 = 'http://www.zjiet.edu.cn/'
qr3 = qrcode.QRCode(
    version=10,
    error_correction=qrcode.constants.ERROR_CORRECT_Q,
    box_size=5,
    border=6,
)
qr3.add_data(content3)
qr3.make(fit=True)
img3 = qr3.make_image(fill_color="#00BFFF", back_color="#FFFFFF")
img3.save('qr3.png')