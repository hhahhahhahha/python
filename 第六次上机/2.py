def intcham(string):
    m=''#保存数字字符串
    key=[]#保存已存在的数字
    intkey=[]#保存我们所需要的字符串
    for i in string:
        if i!=',':
            m+=i
        else:
            for i in m:
                if int(i) not in key:
                    key.append(int(i))
                else:
                    key=[]
                    m=''
                    break
            if key and max(key)==len(key):
                intkey.append(m)
                key=[]
                m=''
    for i in m:
        if int(i) not in key:
            key.append(int(i))
        else:
            key=[]
            m=''
            break
    if key and max(key)==len(key):
        intkey.append(m)
        key=[]
        m=''
    if intkey:
        for i in intkey:
            print(i)
    else:
        print("not found")
        
        
if __name__ == "__main__":
    key =input("请输入数字字符串(如果有多个请参照123,45,23)：")
    intcham(key)