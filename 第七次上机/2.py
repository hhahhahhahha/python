def identify(m: list)->bool:
    c=[]
    for i in m:
        if i not in c:
            c.append(i)
        else: return(True)
    return False


if __name__ == "__main__":
    m=[1,2,3,4,4]
    print(identify(m))



