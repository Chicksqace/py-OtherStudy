#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2021/12/23 22:27
# @Author : 陈攀宇
# @File : 小红书.py
import requests


def fetchUrl(url):
    '''
    发起网络请求，获取网页源码
    '''
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9 ',
        'cookie': 'xhsTrackerId=7f614f8a-cff7-4651-c6e5-500de3d000c2; timestamp2=20211223af2e43d32af43ba0cb9f7ec3; timestamp2.sig=3Zycpd_xGHFr5x2tBXsM8Hjd5quRwvTqL0LiML3rkYY; extra_exp_ids=puarranchiv2_exp1,commentshow_exp1,gif_exp1,ques_clt2',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4098.3 Safari/537.36',
        'referer': 'https://www.xiaohongshu.com/explore',
    }

    r = requests.get(url, headers=headers)
    return r.text


def parsing_link(html):
    '''
    解析html文本，提取无水印图片的 url
    '''

    beginPos = html.find('imageList') + 11
    endPos = html.find(',"cover"')
    imageList = eval(html[beginPos: endPos])

    for i in imageList:
        picUrl = f"https://ci.xiaohongshu.com/{i['traceId']}"
        yield picUrl, i['traceId']


def download(url, filename):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4098.3 Safari/537.36',
    }

    with open(f'{filename}.jpg', 'wb') as v:
        try:
            r = requests.get(url, headers=headers)
            v.write(r.content)
        except Exception as e:
            print('图片下载错误！')


if __name__ == '__main__':
    original_link = 'https://www.xiaohongshu.com/discovery/item/61c18047000000002103e294'
    html = fetchUrl(original_link)
    for url, traceId in parsing_link(html):
        print(f"download image {url}")
        download(url, traceId)
    print("Finished!")