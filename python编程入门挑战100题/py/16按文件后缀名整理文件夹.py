#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2022/1/28 16:47
# @Author : 不知天文，不知地理
# @File : 16按文件后缀名整理文件夹.py
# 小知识：怎样获取文件的后缀名？
# import os
# os.path.splitext("/path/to/aaa.mp3")
# 输出:('/path/to/aaa','mp3')
# 小知识：怎样移动文件
# import shutil
# shutil.move("aaa.txt","dir/bbb.foo")
import os
import shutil
dir="D:/pythonProject/python编程入门挑战100题/"
for file in os.listdir(dir):
    #print(file)
    ext=os.path.splitext(file)[1]
    ext=ext[1:]
    if not os.path.isdir(f"{dir}/{ext}"):#如果目标不存在
        os.mkdir(f"{dir}/{ext}")#没有就创建目录
    source_path=f"{dir}/{file}"
    target_path=f"{dir}/{ext}/{file}"
    shutil.move(source_path,target_path)
    print(file,ext)
