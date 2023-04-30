#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2022/1/24 21:07
# @Author : 不知天文，不知地理
# @File : 13统计学生成绩文件最高分最低分平均分.py
# 输入文件：
# 三列：学号，姓名，成绩
# 列之间用逗号分割，比如“101，小张，88”
# 行之间用\n换行分割
# 输出：最高分，最低分，平均分
def compute_score():#读取文件进行计算
    scores=[]
    with open("student_grade_input",encoding='utf-8') as fin:#读取文件,不设置编码方式会乱码
        fin=fin.readlines()
        for line in fin:#读取了每一行
            line=line[:-1]#这个语法是将最后的换行符去掉
            fields=line.split(",")#逗号分隔
            scores.append(int(fields[-1]))
            max_score = max(scores)
            min_score = min(scores)
            avg_score = round(sum(scores) / len(scores), 2)
    return max_score,min_score,avg_score
print(compute_score())
