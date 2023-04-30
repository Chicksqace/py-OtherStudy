#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2023/3/12 14:12
# @File : barcode_test.py
import barcode
# pip install python-barcode包
from barcode.writer import ImageWriter
EAN=barcode.get_barcode_class('ean13')
ean = EAN(u'4260165185431',writer=ImageWriter())
ean.save('ldn20212013225')
import barcode
from barcode.writer import ImageWriter
EAN=barcode.get_barcode_class('code39')
ean = EAN(u'ldn20212013225',writer=ImageWriter())
ean.save('ldn20212013225_32')
# import qrcode
# # qr = qrcode.QRCode()
# qr = qrcode.QRCode(
#     version=1,#版本
#     error_correction=qrcode.constants.ERROR_CORRECT_L,#纠错等级
#     box_size=10,
#     border=4,
# )
# qr.add_data('cpy20212013206')
# qr.make(fit=True)
#
# img = qr.make_image(fill_color="black", back_color="white")
# img.save("qrcode1.png")
# qr = qrcode.QRCode(
#     version=2,#版本
#     error_correction=qrcode.constants.ERROR_CORRECT_L,#纠错等级
#     box_size=10,
#     border=1,
# )
# qr.add_data('cpy20212013206hihi')
# qr.make(fit=True)
#
# img = qr.make_image(fill_color="black", back_color="white")
# img.save("qrcode2.png")



# isbn
from barcode import EAN13
from barcode.writer import ImageWriter
from PIL import Image

isbn = '9787308185110'  # ISBN号码

# 创建条码对象
ean = EAN13(isbn, writer=ImageWriter())

# 保存条码图片
ean.save('isbn_barcode')

# 打开并显示条码图片
barcode_image = Image.open('isbn_barcode.png')
barcode_image.show()
