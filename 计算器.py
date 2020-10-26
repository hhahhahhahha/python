from tkinter import *
from tkinter.font import names
class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()
        self.hi = None
        self.i=0
    def initWidgets(self):
        self.show= Label(relief=SUNKEN, font=('Courier New', 24),width=23, bg='white', anchor=W)
        self.show.pack(side=TOP,pady=10)
        p = Frame(self.master,background='black')
        p.pack(side=TOP)
        names=('(',')','%','/','9','8','7','*','6','5','4','-','1','2','3','+','AC','0','.','=')
        for i in range(len(names)):
            b = Button(p, text=names[i], font=('Verdana', 20), width=5)
            b.grid(row=i // 4, column=i % 4)
            b.bind('<Button-1>',self.click)
            if(b['text']=='AC'): b.bind('<Button-1>',self.clear)
    def click(self,event):
        if(event.widget['text'] in ('0', '1', '2', '3','4', '5', '6', '7', '8', '9', '.')):
            if self.i == 0 :
                self.show['text'] = ''
            self.show['text'] = self.show['text'] + event.widget['text']
            self.i+=1
            print(self.i)
        elif(event.widget['text'] in ('+', '-', '*', '/', '%', '(',')')):
            self.show['text'] = self.show['text'] + event.widget['text']
        elif(event.widget['text'] =='='and self.show['text'] is not None):
            self.hi = self.show['text']
            # 其实这一步可以不要，主要作用是在调试时可以在后台看输入的数据
            print(self.hi)
            # 使用eval函数计算表达式的值
            self.show['text'] = str(eval(self.hi))
            self.hi = self.show['text']
            # 其实这一步可以不要，主要作用是在调试时可以在后台看输入的数据
            print(self.hi)
            self.i= 0
    def clear(self,event):
        self.show['text']=''
        self.hi=None
 
root = Tk()
root.title("简单科学计算器")
App(root)
root.mainloop()