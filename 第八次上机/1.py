import turtle 
 
def main():
    #设置窗口信息
    turtle.title('五边形和五角心的绘制')
    turtle.setup(800, 600, 0, 0)
    #设置画笔
    pen = turtle.Turtle()
    pen.color("red")
    pen.width(5)
    #pen.shape("turtle")
    pen.speed(5)
    #读取文件
    date=[]
    file = open("第八次上机\\data.text","r")
    for line in file:
        date.append(list(map(float, line.split(','))))
    #动态绘制
    for i in range(len(date)):
        pen.color((date[i][3],date[i][4],date[i][5]))
        pen.forward(date[i][0])
        if date[i][1]:
            pen.rt(date[i][2])
        else:
            pen.lt(date[i][2])
    pen.goto(0,0)
    turtle.done()
  
if __name__ == '__main__':
    main()