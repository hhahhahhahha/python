import random

name=[]
ban=[[],[],[]]
for i in range(1,9):
    m =input("请输入第{}位老师名字".format(i))
    name.append(m)
for i in name:
    k = random.randint(1,3)
    ban[k-1].append(i)
for i in ban:
    print(len(i),end='')
    print(i)