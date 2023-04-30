#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2022/1/25 20:43
# @Author : 不知天文，不知地理
# @File : 14统计英语文章每个单词的出现次数.py
word_count={}#用字典的方法，value就是单词，key就是次数
fout=[]
with open("student_grade_input",encoding='utf-8') as fin:#导入文件
    for line in fin:
        line=line[:-1]#去除最后行换行符
        words=line.split()#按照空格进行分割，得到单词
        for word in words:#对每个单词来说
            if word not in word_count:#这个单词不在这个字典中
                word_count[word]=0
            word_count[word]+=1
            fout.append(','.join(word_count))
# fout1="".join(fout)
print(fout,end='\n')
print(
    sorted(
    word_count.items(),
    key=lambda  x:x[1],
    reverse=True
)[:10]#python中的欺骗语法，保留出现最多的十个单词
)