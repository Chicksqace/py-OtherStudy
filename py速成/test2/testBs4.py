#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2021/12/14 13:34
# @Author : 陈攀宇
# @File : testBs4.py
'''
BeautifulSoup4将复杂HTML文档转化为一个复杂的树形结构，每个节点都是python对象，所有对象可以归纳为4种：
-Tag
-NavigableString
-Beautifulsop
-Comment
'''

from bs4 import BeautifulSoup

file=open("./baidu.com","rb")
html=file.read()
bs=BeautifulSoup(html,"html.parser")
# print(bs.title)
# #1.Tag 标签及其内容：拿到它所在的第一个内容
# print(bs.title.string)
# #2.NavigableString 标签里面的内容（字符串）
#
# print(bs.a.attrs)
# print(bs.name)
# #3.Beautifulsop 表示整个文档
#
#
# print(bs)
#
# print(bs.a.string)
# #Comment 是一个特殊的navigableString，输出内容不包含注释符号


#文档的遍历
# print(bs.head.contens)
# print(bs.head.contens[1])






import re
#文档的搜索
#(1)find_all查找所有
#字符串过滤：会查找与字符串完全匹配的内容
# t_list=bs.find_all("a")
#正则表达式搜索：使用search（）方法来匹配内容
# t_list=bs.find_all(re.compile("a"))


#方法：传入一个函数（方法），根据函数的要求来搜索
# def name_is_exists(tag):
#     return tag.has_attr("name")
# t_list=bs.find_all(name_is_exists)


#2.kwarge 参数
# t_list=bs.find_all(id="head")

#3.text参数
# t_list=bs.find_all(text="head")
# t_list=bs.find_all(text=re.compile("\d"))#应用正则表达式来查找包含特定文本的内容（标签里的字符串）
# #4。limit 帮你获取几个
# t_list=bs.find_all("a",limit=3)



#css选择器

#print(bs.select('title')) #通过标签来查找
t_list=bs.select(".mnav")  #通过类名来查找

t_list=bs.select("#u1")   #通过id来查找

t_list=bs.select["a[class='bri]"] #通过属性来查找
t_list=bs.select("head>title") #通过子标签来查找































