#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2023/3/14 14:30
# @File : Qrcode.py
import qrcode
# 二维码内容
content = 'http://www.baidu.com/'
# 二维码配置
qr = qrcode.QRCode(
    version=10,
    error_correction=qrcode.constants.ERROR_CORRECT_Q,
    box_size=5,
    border=6,
)
# 添加数据
qr.add_data(content)
# 转存写入
qr.make(fit=True)
# 图片样式
img = qr.make_image(fill_color="#00BFFF", back_color="#FFFFFF")
# 保存图片
img.save('qr.png')