import turtle

while True:
    turtle.fd(200)
    turtle.left(120)
    if abs(turtle.pos())<1:
        break
turtle.penup()
turtle.seth(90)
turtle.fd(100)
turtle.pendown()
turtle.seth(0)
for i in range(3):
    turtle.fd(200)
    turtle.right(120)
    
turtle.done()