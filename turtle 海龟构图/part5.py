#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2021/12/11 16:01
# @Author : 陈攀宇
# @File : part5.py
#递归的使用
#递归自己执行自己
#递归必须要有出口
# a=0
# def say():
#     global a# global全局变量使用
#     a+=1
#     if a>100:
#         return
#     print("从前有座山，山上有座庙")
#     say(100)
# say()
import random
import turtle
turtle.bgcolor('pink')
p=turtle.Turtle()
p.speed(0)
turtle.colormode(255)
def circle(radius):
    if radius>200:
        return
    p.pencolor(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    p.circle(radius)
    p.left(2)
    circle(radius+1)
    turtle.pendown()
    turtle.write('爸爸爱你！周宝贝', font=('SimHei', 15, 'bold'))
circle(50)
turtle.done()