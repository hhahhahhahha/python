import turtle, datetime
def drawGap(): #绘制数码管间隔
    turtle.penup()
    turtle.fd(5)
def drawLine(draw):   #绘制单段数码管
    drawGap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    drawGap()    
    turtle.right(90)
def drawDigit(d): #根据数字绘制七段数码管
    drawLine(True) if d in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,6,8] else drawLine(False)
    turtle.left(90)
    drawLine(True) if d in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if d in [0,1,2,3,4,7,8,9] else drawLine(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)
def drawmingzhi(i):
    drawLine(True) if i in ['h','H','e',"E",'y','Y','g','G'] else drawLine(False)
    drawLine(True) if i in ['h','H','n','N','y','Y','o','O','g','G'] else drawLine(False)
    drawLine(True) if i in ['c',"C",'e','E','y','Y','o','O','g','G'] else drawLine(False)
    drawLine(True) if i in ['c','C','h','H','e','E','n','N','o','O'] else drawLine(False)
    turtle.left(90)
    drawLine(True) if i in ['c','C','h','H','e','E','n','N','y','Y','o','O','g','G'] else drawLine(False)
    drawLine(True) if i in ['c','C','e','E','n','N','o','O','g','G'] else drawLine(False)
    drawLine(True) if i in ['h','H','n','N','y','Y','o','O','g','G'] else drawLine(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)
def drawDate(date):
    turtle.pencolor("red")
    for i in date:
        if i == '-':
            turtle.write('年',font=("Arial", 18, "normal"))
            turtle.fd(40) 
        elif i == '=':
            turtle.write('月',font=("Arial", 18, "normal"))
            turtle.fd(40)
        elif i == '+':
            turtle.write('日',font=("Arial", 18, "normal"))
            turtle.pencolor("green")
            turtle.penup()
            turtle.right(90)
            turtle.fd(160)
            turtle.left(90)
            turtle.fd(-580)
        elif i== '.':
            turtle.penup()
            turtle.right(90)
            turtle.fd(10)
            turtle.write(':',font=("Arial", 18, "normal"))
            turtle.fd(-10)
            turtle.left(90)
            turtle.fd(10)
        elif i== ':':
            turtle.penup()
            turtle.right(90)
            turtle.fd(10)
            turtle.write(':',font=("Arial", 18, "normal"))
            turtle.fd(-10)
            turtle.left(90)
            turtle.fd(10)
        elif i== '*':
            turtle.penup()
            turtle.right(90)
            turtle.fd(40)
            turtle.write('陈勇',font=("Arial", 18, "normal"))
            turtle.left(90)
            turtle.pencolor("black")
        else:
            drawDigit(eval(i))
def main():
    turtle.setup(1200, 750)
    turtle.penup()
    turtle.fd(-350)
    turtle.left(90)
    turtle.fd(200)
    turtle.right(90)
    turtle.pensize(5)
    drawDate(datetime.datetime.now().strftime('%Y-%m=%d+%H.%M:%S*'))
    turtle.penup()
    turtle.right(90)
    turtle.fd(120)
    turtle.left(90)
    turtle.fd(-480)
    for i in 'chen yong':
        drawmingzhi(i)
    turtle.hideturtle()
    turtle.done()
main()    