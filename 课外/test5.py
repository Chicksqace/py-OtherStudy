#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2022/9/14 22:03
# @Author : 不知天文，不知地理
# @File : test5.py
# bookTitles = [ "红岩","林海雪原", "青春之歌","铁道游击队","钢铁是怎样炼成的"]
# authors = ["罗广斌","曲波", "杨沫","刘知侠","尼古拉·奥斯特洛夫斯基"]
# a=dict(zip(bookTitles,authors))
# print("中国红色经典书籍名与作者名：")
# print(a)
# print("┌────────────────────┬───────────────────┐")
# print("│{0:{2}^12s} │{1:{2}^12s}│".format("书籍名","作者名",chr(12288)))
# l=len(a)
# for i in a.keys():
#   print("┌────────────────────┼───────────────────┐")
#   print("│{0:{2}<12s} │{1:{2}<12s}│".format(i,a[i],chr(12288)))
# print("└────────────────────┴───────────────────┘")
# import prettytable as pt
# import numpy as np
# import json
# fieldName=("商品id","图书名称","出版社","价格")
# bookData = (
#     {"id": "1", "bookName": "资本论（第一卷）", \
#      "publisher": "人民出版社", "Price": "90"},
#     {"id": "2", "bookName": "中华人民共和国简史", \
#      "publisher": "上海人民出版社", "Price": "40"},
#     {"id": "3", "bookName": "百年大党正年轻", \
#      "publisher": "东方出版社", "Price": "68"},
#     {"id": "4", "bookName": "零基础学Python3.0（全彩版）", \
#      "publisher": "吉林大学出版社", "Price": "79.80"},
#     {"id": "5", "bookName": "给Python点颜色 青少年学编程", \
#      "publisher": "人民邮电出版社", "Price": "59.80"},
# )
# table=pt.PrettyTable()
# a=np.asarray(fieldName)
# print(b)
# table.field_names=a
# arr=[]
# for i in bookData:
    # print(i["id"],i["bookName"],i["publisher"],i["Price"])
    # table.add_row([i["id"],i["bookName"],i["publisher"],i["Price"]])
# # align 提供了用户设置对齐的方式，值有 l，r，c 方便代表 左对齐，右对齐和居中 如果不设置，默认居中对齐。
# table.align[a[0]]="l"
# table.align[a[1]]="l"
# table.align[a[2]]="l"
# table.align[a[3]]="l"
# print(table)


with open('result.txt', 'w', encoding='utf-8') as f:
    f.write('整数\t平方\t立方\n')
    while True:
        n = int(input('请输入一个不小于1的整数：'))
        if n < 1:
            break
        f.write(f'{n}\t{n*n}\t{n*n*n}\n')

