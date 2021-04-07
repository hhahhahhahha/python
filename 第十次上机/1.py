import requests
from bs4 import BeautifulSoup
import re

pattern_s=re.compile('<span class="user-stars allstar(.*) rating')
s=0
pattern=[]
p=[]
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.11 Safari/537.36'}
for i in range(3):
    urls='https://book.douban.com/subject/33424487/comments/?status={}'.format(str(i*20))
    r=requests.get(urls,headers=headers)
    print(r.status_code)
    soup =BeautifulSoup(r.text,'lxml')
    pattern.extend(soup.find_all('span','short'))
    p.extend(re.findall(pattern_s,r.text))
for item in pattern[:50]:
    print(item.string)
for i in p[:50]:
    print(i)
    s+=int(i)
print(s/50)
