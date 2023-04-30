#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2022/1/1 22:23
# @Author : 不知天文，不知地理
# @File : turtle星星.py
import turtle
import random
turtle.colormode(255)
turtle.pensize(5)
for i in range(5):
    turtle.begin_fill()
    for i in range(5):
        turtle.pencolor(20, 30, 50)
        turtle.fillcolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        turtle.forward(200)
        turtle.right(144)
    turtle.end_fill()
turtle.mainloop()
