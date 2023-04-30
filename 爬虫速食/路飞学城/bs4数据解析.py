#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2021/12/14 15:46
# @Author : 陈攀宇
# @File : bs4数据解析.py
from bs4 import BeautifulSoup
#想要将本地中的HTML文档中的数据加载到该对象中
fp=open('./kfc.html','r',encoding='utf-8')
soup=BeautifulSoup(fp,'lxml')             #第二个参数统一固定，使用lxml解析器，第一个参数为文件描述符
#print(soup)
# print(soup.html)#soup.tagName 返回的是HTML中第一次出现的tagName标签
#find('tagName'):等同于soup.div
#print(soup.find('p',class_='sss'))#class_如果不跟下划线，就是一个关键字了
# print(soup.find_all('p'))
# print(soup.select('.tang'))
print(soup.select('.tang > ul a')[0]['href'])#返回的是一个列表