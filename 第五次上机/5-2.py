def isOdd(n):
    while(n%1!=0):
        print("输入的不是整数数字")
        n=eval(input("请输入要判断的整数数字："))
    if(n%2==0) :
        return(False)
    else :
        return True
if __name__ == '__main__':
    n=eval(input("请输入要判断的整数数字："))
    c=isOdd(n)
    print(c)