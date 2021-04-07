def identify(m: list)->bool:
    c=set(m)
    if(len(c)==len(m)):
        return False
    else: return True

if __name__ == "__main__":
    m=[1,2,3,4,4]
    print(identify(m))