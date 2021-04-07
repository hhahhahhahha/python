import turtle
turtle.ht()  #隐藏光标 
turtle.setup(650, 350, 200, 200)   #初始化画布
turtle.penup()    #笔拿起来
turtle.fd(-250)   #向箭头所指方向前进 -250
turtle.pendown()  #放下笔
turtle.pensize(25)  #设置笔触粗细为25
turtle.pencolor("yellow")  #设置笔触颜色
turtle.seth(-40)  #改变海龟的行进方向，但不行进

strcolor = ["red","blue","black","green"]
for i in range(4):
    turtle.pencolor(strcolor[i])
    turtle.circle(40,80) #画圆
    turtle.circle(-40,80)
turtle.pencolor("purple")
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40*2/3)

turtle.done()