def isNum(n):
    isplural = n[-1]
    first=False
    for i in n:
        if(i<'0' or i>'9'):
            if(i!='.'):
                if(i!='j'and i!='J'):
                    if(i!='+'and i!='-'):
                        return False
                    else:
                        if(n.index(i)!=0):
                            if(isplural!='j'and isplural!='J' or first==True):
                                return False
                            first=True
    return True
if __name__ == "__main__":
    m=input("请输入一个字符串: ")
    n=isNum(m)
    print(n)