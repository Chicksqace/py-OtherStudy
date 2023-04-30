#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2021/12/14 0:03
# @Author : 陈攀宇
# @File : 爬取图片.py
import requests
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
url="https://pic.qiushibaike.com/system/pictures/12482/124822595/medium/8FL1GFRKLGEBL43W.jpg"
#content返回的是二进制的图片数据
#text（字符串） conten（二进制）json（对象）
img_data=requests.get(url=url).content
with open('./qiutu.jpg','wb') as fp:
    fp.write(img_data)