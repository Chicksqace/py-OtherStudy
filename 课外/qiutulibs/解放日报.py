#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2021/12/30 15:35
# @Author : 不知天文，不知地理
# @File : 解放日报.py
import requests
import bs4
import os
import datetime
import time
import json
def fetchUrl(url):
    '''
    功能：访问 url 的网页，获取网页内容并返回
    参数：目标网页的 url
    返回：目标网页的 html 内容
    '''
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }
    r = requests.get(url, headers=headers)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    return r.text


def saveFile(content, path, filename):
    '''
    功能：将文章内容 content 保存到本地文件中
    参数：要保存的内容，路径，文件名
    '''
    # 如果没有该文件夹，则自动生成
    if not os.path.exists(path):
        os.makedirs(path)
    # 保存文件
    with open(path + filename, 'w', encoding='utf-8') as f:
        f.write(content)


def download_rmrb(year, month, day, destdir):
    '''
    功能：网站 某年 某月 某日 的新闻内容，并保存在 指定目录下
    参数：年，月，日，文件保存的根目录
    '''
    url = 'https://www.shobserver.com/staticsg/data/journal/' + year + '-' + month + '-' + day + '/navi.json'
    html = fetchUrl(url)
    jsonObj = json.loads(html)

    for page in jsonObj["pages"]:
        pageName = page["pname"]
        pageNo = page["pnumber"]
        print(pageNo, pageName)
        for article in page["articleList"]:
            title = article["title"]
            subtitle = article["subtitle"]
            pid = article["id"]
            url = "https://www.shobserver.com/staticsg/data/journal/" + year + '-' + month + '-' + day + "/" + str(
                pageNo) + "/article/" + str(pid) + ".json"
            print(pid, title, subtitle)

            html = fetchUrl(url)
            cont = json.loads(html)["article"]["content"]
            bsobj = bs4.BeautifulSoup(cont, 'html.parser')
            content = title + subtitle + bsobj.text

            path = destdir + '/' + year + month + day + '/' + str(pageNo) + " " + pageName + "/"
            fileName = year + month + day + '-' + pageNo + '-' + str(pid) + '.txt'
            saveFile(content, path, fileName)


def gen_dates(b_date, days):
    day = datetime.timedelta(days=1)
    for i in range(days):
        yield b_date + day * i


def get_date_list(beginDate, endDate):
    """
    获取日期列表
    :param start: 开始日期
    :param end: 结束日期
    :return: 开始日期和结束日期之间的日期列表
    """

    start = datetime.datetime.strptime(beginDate, "%Y%m%d")
    end = datetime.datetime.strptime(endDate, "%Y%m%d")

    data = []
    for d in gen_dates(start, (end - start).days):
        data.append(d)

    return data


if __name__ == '__main__':
    '''
    主函数：程序入口，提供了两种爬取方式，爬取指定日期的新闻 or 爬取时间段内的新闻
    '''

    # 输入起止日期，爬取之间的新闻
    beginDate = input('请输入开始日期:')
    endDate = input('请输入结束日期:')
    data = get_date_list(beginDate, endDate)

    for d in data:
        year = str(d.year)
        month = str(d.month) if d.month >= 10 else '0' + str(d.month)
        day = str(d.day) if d.day >= 10 else '0' + str(d.day)
        download_rmrb(year, month, day, f'Data/{year}')
        print("爬取完成：" + year + month + day)
        time.sleep(3)
