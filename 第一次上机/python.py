import turtle
turtle.ht()  #隐藏光标 
turtle.setup(650, 350, 200, 200)   #初始化画布
turtle.penup()    #笔拿起来
turtle.fd(-250)   #向箭头所指方向前进 -250
turtle.pendown()  #放下笔
turtle.pensize(25)  #设置笔触粗细为25
turtle.seth(-40)  #改变海龟的行进方向，但不行进

for i in range(4):
    turtle.pencolor("yellow")
    turtle.circle(40,80) #画圆
    turtle.pencolor("black")
    turtle.circle(-40,80)

turtle.pencolor("yellow")  #设置笔触颜色
turtle.circle(-40,80)

turtle.seth(-140)
turtle.fd(10)

for i in range(4):
    turtle.pencolor("green")
    turtle.circle(-40,80)
    turtle.pencolor("red")
    turtle.circle(40,80) #画圆

turtle.circle(20,140)
turtle.seth(0)
turtle.pencolor("blue")  #设置笔触颜色
turtle.fd(40*2/3)

turtle.done()


