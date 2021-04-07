import turtle

while True:
    turtle.penup()
    turtle.fd(50)
    turtle.pendown()
    turtle.fd(100)
    turtle.penup()
    turtle.fd(50)
    turtle.left(90)
    if abs(turtle.pos())<1:
        break
turtle.done()