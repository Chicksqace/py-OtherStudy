#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2021/12/20 14:17
# @Author : 不知天文，不知地理
# @File : 圣诞树.py
import turtle
import random
screen = turtle.Screen()
screen.setup(375, 700)

circle = turtle.Turtle()
circle.shape('circle')
circle.color('pink')
circle.speed('fastest')
circle.up()
square = turtle.Turtle()
square.shape('square')
square.color('green')
square.speed('fastest')
square.up()

circle.goto(0, 280)
circle.stamp()

k = 0
for i in range(1, 13):
    y = 30 * i
    for j in range(i - k):
        x = 30 * j
        square.goto(x, -y + 280)
        square.stamp()
        square.goto(-x, -y + 280)
        square.stamp()

    if i % 4 == 0:
        x = 30 * (j + 1)
        circle.color('pink')
        circle.goto(-x, -y + 280)
        circle.stamp()
        circle.goto(x, -y + 280)
        circle.stamp()
        k += 3

    if i % 4 == 3:
        x = 30 * (j + 1)
        circle.color('yellow')
        circle.goto(-x, -y + 280)
        circle.stamp()
        circle.goto(x, -y + 280)
        circle.stamp()

square.color('brown')
for i in range(13, 17):
    y = 30 * i
    for j in range(2):
        x = 30 * j
        square.goto(x, -y + 280)
        square.stamp()
        square.goto(-x, -y + 280)
        square.stamp()

text = turtle.Turtle()
text.hideturtle()
text.penup()
text.goto(-120, 270)
text.color('pink')
text.write('青春永驻', font=('xingkai', 18, 'bold'))
turtle.done()
