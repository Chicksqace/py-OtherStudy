#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2021/12/11 14:10
# @Author : 陈攀宇
# @File : testUrllib.py
import urllib.request
#获取get请求
'''
response=urllib.request.urlopen("http://www.baidu.com")
print(response.read().decode('utf-8'))#对获取到的网页源码进行utf-8解码
'''
#获取post请求 发送表单，可以把用户名和密码加密
#测试网站http://httpbin.org/
import urllib.parse#解析器
# data=bytes(urllib.parse.urlencode({"hello":"world"}),encoding="utf-8")#二进制，封装
# response=urllib.request.urlopen("http://httpbin.org/post",data=data)
# print(response.read().decode("utf-8"))

# try:
#     response=urllib.request.urlopen("http://httpbin.org/get",timeout=0.01)#timeout：超时处理
#     print(response.read().decode("utf-8"))
# except urllib.error.URLError as e:
#     print("out!")


# response=urllib.request.urlopen("http://www.baidu.com")
# #print(response.status)
# print(response.getheaders())



headers={
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
url="http://httpbin.org/post"
data=bytes(urllib.parse.urlencode({'name':'Jack'}),encoding="utf-8")#urlencode
req=urllib.request.Request(url=url,data=data,headers=headers,method="POST")#data:带数据，header：返回信息,method:方式
response=urllib.request.urlopen(req)
print(response.read().decode("utf-8"))

# url="https://douban.com"
# headers={
# "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
# }
# req=urllib.request.Request(url=url,headers=headers)
# response=urllib.request.urlopen(req)
# print(response.read().decode("utf-8"))
































