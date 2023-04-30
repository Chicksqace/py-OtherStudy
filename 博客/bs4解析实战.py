#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2021/12/20 14:50
# @Author : 陈攀宇
# @File : bs4解析实战.py
import requests
from bs4 import BeautifulSoup
#需求：爬取三国演义所以章节和内容https://www.shicimingju.com/book/sanguoyanyi.html
#对首页的页面数据进行爬取
url="https://www.shicimingju.com/book/sanguoyanyi.html"
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
#page_text==requests.get(url=url,headers=headers).text
page_text = requests.get(url,headers)#编码方式不同
page_text.encoding = page_text.apparent_encoding
page_text = page_text.text

#需要在首页中解析出章节的标题和详情页的url
#实例化Beautifulsoup对象，需要将页面源码数据加载到该对象中
soup=BeautifulSoup(page_text,'lxml')
#解析章节标题和详情页的url
li_list=soup.select('.book-mulu > ul > li')
fp=open('./sg.txt','w',encoding='utf-8')
for li in li_list:
    title=li.a.string
    detail_url="https://www.shicimingju.com"+li.a['href']
    #print(detail_url)
    #对详情页发起请求，解析出章节内容
    detail_page_text=requests.get(url=detail_url,headers=headers).text
    detail_page_text = detail_page_text.encode('iso-8859-1')
    # detail_page_text=requests.get(url,headers)
    # detail_page_text.encoding=detail_page_text.apparent_encoding
    # detail_page_text=detail_page_text.text
    #解析出详情页中的相关的章节内容
    detail_soup=BeautifulSoup(detail_page_text,'lxml')
    div_tag=detail_soup.find('div',class_= "chapter_content")
    #解析到章节的内容
    content=div_tag.text
    #print(div_tag)
    fp.write(title+':'+content+'\n')
    print(title,'爬取成功')
