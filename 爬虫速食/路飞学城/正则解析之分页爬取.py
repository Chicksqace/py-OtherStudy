#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2021/12/14 15:08
# @Author : 陈攀宇
# @File : 正则解析之分页爬取.py
import requests
import re
import os
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
#创建一个文件夹，用来保存所糗图图片
if not os.path.exists('./qiutulibs'):
    os.mkdir('./qiutulibs')
#设置一个通用的url模板
url='https://www.qiushibaike.com/imgrank/page/%d/'
pagenum=1

for pagenum in range(1,3):
    #对应页码的url
    new_url=format(url%pagenum)
    #使用通用爬虫对url对应的一整页进行爬取
    page_text=requests.get(url=new_url,headers=headers).text
    #print(page_text)
    #使用聚焦爬虫将页面中所有的糗图进行解析/提取
    # ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
    ex = '<div class="thumb">.*?<img src="(.*?)" alt='
    img_src_list=re.findall(ex,page_text,re.S)
    #print(img_src_list)
    for src in img_src_list:
        #拼接处一个完整的图片url
        src='https:'+src
        #print(src)
        #请求到图片的二进制数据
        img_data=requests.get(url=src,headers=headers).content
        #生成图片名称
        img_name=src.split("/")[-1]
        #图片存储的路径
        imgpath="./qiutulibs"+img_name
        #print(imgpath)
        with open(imgpath,'wb') as fp:
            fp.write(img_data)
            print(img_name,"下载成功")