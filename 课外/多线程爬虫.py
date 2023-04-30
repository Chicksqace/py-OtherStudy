#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2022/11/7 19:07
# @Author : 不知天文，不知地理
# @File : 多线程爬虫.py
import datetime
import time
import requests
import threading
import csv
from bs4 import BeautifulSoup
from datetime import datetime

count = [0, 0, 0]


def find_id(movie_href: str):  # 从链接中取出ID
    char1 = '.'
    char2 = '/'
    npos1 = movie_href.rfind(char1)
    npos2 = movie_href.rfind(char2)
    ID = movie_href[npos2 + 1:npos1]
    return ID


head_list = ["ID", "电影名称", "网页", "磁链", "更新时间"]
# domain = "https://m.dytt8.net/index2.htm"  # 电影天堂域名
# url = "https://m.dytt8.net/html/gndy/dyzz/index.html"  # 电影天堂最新电影
# url = "https://m.dytt8.net/html/gndy/dyzz/list_23_1.html"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 '
                  'Safari/537.36',
    'Connection': 'close',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'referer': ''}
requests.DEFAULT_RETRIES = 5  # 设置重试次数为5
data_list = []


def craw_one_page(i):
    global count
    # for i in range(1, 2):
    url = "https://m.dytt8.net/html/gndy/dyzz/list_23_" + str(i) + ".html"
    start = time.time()
    print(f"开始爬取第{i}页,时间:{start}")
    response = requests.get(url, headers=headers)
    time.sleep(0.3)
    response.encoding = 'gb2312'  # 编码格式gb2312
    homepage = response.text  # 主页
    soup = BeautifulSoup(homepage, "lxml")
    movies_list = soup.find_all('a', class_='ulink')  # 取当前页面所有的电影

    for movie in movies_list:
        name = movie.text
        href = "https://m.dytt8.net" + movie['href']
        ID = find_id(href)
        resp = requests.get(href, headers=headers)
        resp.encoding = 'gb2312'
        soup2 = BeautifulSoup(resp.text, "lxml")
        Magnet_URI = soup2.select_one('#Zoom > td > a')['href']
        updated_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        movie_dict = {
            "ID": ID,
            "电影名称": movie.text,
            "网页": href,
            "磁链": Magnet_URI,
            "更新时间": updated_time}
        print(movie_dict)
        count[i - 1] += 1
        data_list.append(movie_dict)
    f = open('test.csv', mode='w', encoding="gb2312", newline="")
    with f:
        w = csv.DictWriter(f, head_list)
        w.writeheader()
        w.writerows(data_list)
    over = time.time()
    print(f"第{i}页爬取完毕,{count[i - 1]}条数据，耗时{(over - start)}")


if __name__ == '__main__':
    Sum = 0
    t1 = threading.Thread(target=craw_one_page, args=(1,))
    t2 = threading.Thread(target=craw_one_page, args=(2,))
    t3 = threading.Thread(target=craw_one_page, args=(3,))
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
    for i in range(len(count)):
        Sum += count[i]
    print(f"总共{Sum}条数据")

#         data_list.append(movie_dict)
# f = open('test.csv', mode='w', encoding="gb2312", newline="")
# with f:
#     w = csv.DictWriter(f, head_list)
#     w.writeheader()
#     w.writerows(data_list)
