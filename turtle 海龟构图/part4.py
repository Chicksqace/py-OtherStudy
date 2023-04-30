import turtle
import random
a=[1,2,3,4,5,6]#0-5
b="fadsagaggdfgsg"
# print(a[random.randint(0,5)])
print(random.choice(b))##chocie()从中选择一个元素
p=turtle.Turtle()
#画一个五角星
# a=[5,7,9,11]
# star=random.choice(a)
# turtle.bgpic("./turtle海龟构图/2.png")
# turtle.setup(width=200,height=200,startx=0,stary=0)
# for i in range(star):
#     p.forward(200)
#     p.left(180-180/star)
p.forward(1000)
p.goto(0,0)
p.circle(50)
turtle.done()