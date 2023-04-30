#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2022/1/5 20:47
# @Author : 不知天文，不知地理
# @File : xpath基础.py
from lxml import etree
#实例化好了一个etree对象，且将解析的源码加载到该对象中
tree=etree.parse('huazhuangpi.html')
# r=tree.xpath('/html/body/div')
# r=tree.xpath('/html//div')
# r=tree.xpath('//div')
#=tree.xpath('//div[@class="hzbscin"]')
# r=tree.xpath('//div[@class="song"]/p[3]')
# r=tree.xpath('//div[@class="tang"]//li[5]/a/text()')[0]
# r=tree.xpath('//li[7]//text()')[0]
r=tree.xpath('//div[@class="song"]/img/@src')
print(r)