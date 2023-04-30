#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2022/1/1 17:51
# @Author : 不知天文，不知地理
# @File : 简单分析.py
import pygal
line_chart = pygal.Line()
line_chart.title = '各科平时成绩趋势图'
line_chart.x_labels = map(str, range(1, 14))
line_chart.add('PS', [95, 100, 100, 100, 100, 100,100,100,100,100,81,72.5,100,97.5])
line_chart.add('程序基础', [80, 80, 70, 80, 90, 80,70,90,90,80,80,80])
line_chart.add('计算机应用基础', [100, 100, 100, 100, 100, 100,97,98,92,100,100])
line_chart.render_to_file('cj.html')


