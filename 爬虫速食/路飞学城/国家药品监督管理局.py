#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2021/12/10 20:39
# @Author : 陈攀宇
# @File : 国家药品监督管理局.py
#动态加载数据？？在首页中的企业是通过ajax动态请求到的
# http://scxk.nmpa.gov.cn:81/xk/itownet/portal/dzpz.jsp?id=a17b1a0ba1f44ae98699be82f69ff032
# http://scxk.nmpa.gov.cn:81/xk/itownet/portal/dzpz.jsp?id=af4832c505b749dea76e22a193f873c6
#通过对详细对详情页的url的观察发现：
# -url的域名都是一样的，只有携带的参数（ID）不一样
# ID值可以从首页对应的ajax请求到的json串中获取
# 域名和ID值拼接处有一个完整的企业对应的详情页的url
#详情页的企业详情数据也是动态加载出来的
# http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById
# http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById
#观察后发现：所以的post请求的url都是一样的，只有ID参数不一样。
#如果我们可以批量获取多家企业的ID后，就可以将ID和url形成一个完整的详情页对应数据的ajax请求的url
import requests
url="http://scxk.nmpa.gov.cn:81/xk/"
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
page_text=requests.get(url=url,headers=headers).text
with open('./huazhuangpi.html','w',encoding='utf-8') as fp:
    fp.write(page_text)