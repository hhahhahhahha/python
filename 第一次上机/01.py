#e1.1TempConvert.py

TempTstr = eval(input("请输入温度值："))
s = input("请输入F或C以此选择温度类型（华氏温度： F，摄氏温度：C）：")
#print(TempTstr)
if s in ['F','f']:
    C = (TempTstr-32)/1.8
    print("转换后的温度{:.2f}C".format(int(C)))
elif s in ['c','C']:
    F =1.8*TempTstr+32
    print("转换后的温度是{:.2f}F".format(int(F)))
else:
    print("输入格式错误")
