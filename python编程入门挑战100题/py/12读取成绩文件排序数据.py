#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2022/1/24 17:16
# @Author : 不知天文，不知地理
# @File : 12读取成绩文件排序数据.py
# 输入文件：
# 三列：学号，姓名，成绩
# 列之间用逗号分割，比如“101，小张,88”
# 行之间用\n换行分割
# 处理：
# 读取文件，按成绩倒序排序
# 输出：
# 排序后的三列数据
def read_file():
    result=[]
    with open("./student_grade_input",encoding="utf-8") as fin:#读取文件,不设置编码方式会乱码
        for line in fin:#读取了每一行
            line=line[:-1]#这个语法是将最后的换行符去掉
            result.append(line.split(","))#逗号分隔
    return result



#读取文件
datas=read_file()
print("read_file datas:",datas)
#排序数据
#datas=sort_grades(datas)
#写出文件
#write_file(datas)