import turtle
number = 3
turtle.seth(0)
for i in range(150):
    turtle.fd(number)
    turtle.right(90)
    turtle.fd(number)
    number = number+1

turtle.done()