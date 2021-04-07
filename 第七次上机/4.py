def c(m: str)->dict:
    x={}
    for i in m:
        if i in x:x[i]+=1
        else: x[i]=1
    max=sorted(x,reverse=True)
    print(max)
if __name__ == "__main__":
    m=input('请输入字符串：')
    c(m)