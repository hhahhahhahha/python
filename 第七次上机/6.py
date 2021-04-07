import jieba
excludes = {"什么","一个","我们","那里","你们","如今","说道","姑娘","说到","老太太","怎么","奶奶","两个",
            "知道","起来","这里","出来","他们","众人","自己","一面","太太","只见","没有","不是","不知",
            "这个","听见","这样","进来","咱们","告诉","就是","东西","袭人","回来","只是","大家","只得"}
txt = open("第七次上机\红楼梦.txt", "r", encoding='utf-8').read()
words  = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    elif word == "贾宝玉" or word == "孔明曰":
        rword = "宝玉"
    #elif word == "关公" or word == "云长":
     #   rword = "关羽"
    #elif word == "玄德" or word == "玄德曰":
     #   rword = "刘备"
    #elif word == "孟德" or word == "丞相":
     #   rword = "曹操"
    else:
        rword = word
    counts[rword] = counts.get(rword,0) + 1
for word in excludes:
    if word in counts: del(counts[word])
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True) 
for i in range(20):
    word, count = items[i]
    print ("{0:<10}{1:>5}".format(word, count))