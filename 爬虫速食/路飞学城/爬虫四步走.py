#requests 模块
#requests模块：python中原生的一款基于网络请求模块，功能强大，效率好 作用：模拟游览器发请求
#如何使用：（requests模块的编程流程）
# -指定URL（网址）-发起请求-获取响应数据-持久化存储
#环境安装：pip install requests
#实战编码——需求：爬取搜狗页面
import requests
#1.指定URL
url='https://www.baidu.com/'
#2.发起请求，get()方法会返回一个响应对象
response=requests.get(url=url)
#3.获取响应数据.text返回的是字符串形式的响应数据
page_text=response.text
print(page_text)
#4.持久化存储
with open('../../py速成/test2/baidu.html', 'w', encoding='utf-8') as fp:
    fp.write(page_text)
print("爬取数据结束")