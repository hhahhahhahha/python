
def countchar(string)->list :
    m=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for i in string:
        if 'A'<=i<='Z':
            chr(ord('i')+32)
        if('a'<=i<='z'):
            m[ord(i)-ord('a')]+=1
    return m
if __name__ == "__main__":
    key =input("请输入字符串:")
    print(countchar(key))