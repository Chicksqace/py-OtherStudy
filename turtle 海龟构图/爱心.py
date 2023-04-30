import turtle

def curvemove():#这个函数是为了绘制爱心上方的曲线
  for i in range(200):
    turtle.right(1)
    turtle.forward(1)

turtle.color('pink')
turtle.begin_fill()
turtle.left(140)
turtle.forward(111.65)
curvemove()
turtle.left(120)
curvemove()
turtle.forward(111.65)
turtle.end_fill()

turtle.penup()
turtle.goto(-40, -50)
turtle.pendown()
turtle.write('爸爸爱你！周宝贝',  font = ('SimHei', 15, 'bold'))
turtle.hideturtle()
turtle.done()

