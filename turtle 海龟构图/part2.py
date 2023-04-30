import turtle
import random
p=turtle.Turtle()
turtle.colormode(255)

p.color("red")#用rgb或英文单词都可以
p.speed(5)#设置画笔的速度0——10越往后越快 当括号里面的速度大于10或者小于0.5时，就相当于0（最快）
p.pensize(40)
for i in range(4):
    p.color(random.randint(0,100),random.randint(0,100),random.randint(0,255))
    p.forward(200)
    p.left(90)#画笔的转向
turtle.done()
#print(random.randint(0,10))#输出一个零到十个数
