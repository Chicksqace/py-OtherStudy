#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2022/1/23 19:32
# @Author : 不知天文，不知地理
# @File : 11怎样实现学生成绩排序.py
# 学生成绩数据格式：
# 复杂列表，元素是字典或者元组
# 【{'sno':101,'sname':"小张",'sgrade':88},{'sno':102,'sname':"小王",'sgrade':77},{'sno':103,'sname':"小李",'sgrade':99},{'sno':104,'sname':"小赵",'sgrade':66}】
students=[
    {'sno':111,'sname':"小张",'sgrade':88},
    {'sno':202,'sname':"小王",'sgrade':77},
    {'sno':103,'sname':"小李",'sgrade':99},
    {'sno':104,'sname':"小赵",'sgrade':66}]
students_sort=sorted(students,key=lambda x:x["sgrade"],reverse=True)#传入一个 key 参数，它可以接受一个函数，该函数的功能是指定 sorted() 函数按照什么标准进行排序
#students_sort=sorted(students,key=lambda x:x["sno"],reverse=True)
#students_sort=sorted(students,key=lambda x:len(x))
print(students)
print(students_sort)
#print(f"source{students},sort result:{students_sort}")