data = open("二次上机\Hamlet.txt","r")
content= data.read()

words = content.split(" ")
nword = []
#print(words)
for i in words:
    if (nword.count(i)==0):
        nword.append(i)
number=['',0,'',0,'',0,'',0,'',0,'',0,'',0,'',0,'',0,'',0]
#for i in nworld:
 #   iwords= i
    #print(iwords)
  #  m = words.count(i)
   # for i in range(0,20,2):
    #    if(m>i): 
     #       number.insert(i,m)        
      #      number.insert(i-1,iwords)
       #     del number[-1:-2]
print(number)
