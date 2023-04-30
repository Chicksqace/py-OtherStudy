#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : DATEDATE{TIME}
# @Author : 陈攀宇
# @File : spider.py
from bs4 import BeautifulSoup#网页解析，获取数据
import re#正则表达式，进行文字匹配
import urllib.request,urllib.error#制定url，获取网页数据
import xlwt #进行Excel操作
import sqlite3 #进行SQLite数据库的操作
def main():
    baseurl="https://movie.douban.com/top250?start="
    #1.爬取网页
    datalist=getData(baseurl)
    savepath=".\\豆瓣电影Top250.xls"
    #3.保存数据
    askURL("https://movie.douban.com/top250?start=0")
#爬取网页
def getData(baseurl):
    datalist=[]
    for i in range(0,10):                #调用获取页面信息的函数10次
        url=baseurl+str(i*25)
        html=askURL(url)            #保存获取到的网页源码
    #2.逐一解析数据
    return datalist
#得到指定一个url的网页内容
def askURL(url):
    head={                               #模拟浏览器头部信息，向服务器发送信息
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 91.0.4472.124Safari / 537.36"
    } #用户代理，告诉豆瓣服务器，我们是什么类型的机器，游览器（本质上是告诉游览器，我们可以接收什么水平的文件内容）
    request=urllib.request.Request(url,headers=head)
    html=""
    try:
        response=urllib.request.urlopen(request)
        html=response.read().decode("utf-8")
        print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html


#保存数据
def saveData(savepath):
    pass
if __name__ == "__main__":       #当程序执行时
#调用函数
    main()






























