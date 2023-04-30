import turtle
p=turtle.Turtle()
turtle.colormode(255)
#p.circle(40)#画圆
#弧度
#p.circle(40,180)#第一次参数表示半径，第二个表示弧度
#内切多边行 第一个参数表示半径，第三个参数表示边
#关键字函数
p.circle(60,steps = 3)
#对图形进行上色
p.fillcolor("red")#设置要填充的颜色




#开始上色
p.begin_fill()
#结束上色
p.circle(50)
p.end_fill()
#更改背景色
turtle.bgcolor("blue")
turtle.done()