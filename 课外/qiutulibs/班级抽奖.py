#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2022/1/8 16:07
# @Author : 不知天文，不知地理
# @File : 班级抽奖.py
import xlrd,random
xlsx=xlrd.open_workbook(r'D:\计算机212\计算机212名单.xls')
#打开所用的execl工作簿xls
table=xlsx.sheet_by_index(0)
#打开所用信息所在的工作表sheet
nrows=table.nrows
#提取工作表所用行数即员工总数
w=[i for i in range(nrows)]
#创建从0到（总数-1）的抽奖列表
for i in range(1,1+nrows//2):
    #只需需要循环总数一半向下取整即可
    x=random.choice(w)
    #随机选取一个x
    w.remove(x)
    #从抽奖列表中删除x
    for j in range(len(w)):
    #从剩余列表中遍历寻找下一个中奖人员
        y=random.choice(w)
        #随机再选取一名y
        if table.cell_value(y,0)!=table.cell_value(x,0):
            #判断两名员工是否是同一单位，这里运用xlrd库里的cell_value(x,y),提取第x行第y列单元格cell的信息
            print('第{}次中奖人员：'.format(i),table.cell_value(x,1),table.cell_value(y, 1))
            w.remove(y)
            #从抽奖列表中删除y
            break
            #满足抽取两人后，结束内层循环，继续大循环