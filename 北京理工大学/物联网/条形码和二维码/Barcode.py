#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2023/3/14 14:13
# @File : Barcode.py
# import barcode
# from barcode.writer import ImageWriter
# EAN=barcode.get_barcode_class('ean13')
# ean = EAN(u'4260165185431',writer=ImageWriter())
# ean.save('ean13')

import barcode
from barcode.writer import ImageWriter
EAN=barcode.get_barcode_class('code39')
ean = EAN(u'4260165185431',writer=ImageWriter())
ean.save('code39')