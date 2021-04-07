import requests
from bs4 import BeautifulSoup
import re

headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.11 Safari/537.36'}
r = requests.get("https://money.cnn.com/data/markets/dow/",headers=headers)
print(r.status_code)
#soup =BeautifulSoup(r.text,'lxml')
print(r.text)
reg = re.compile('class="wsod_symbol">(.*?)<\/a>.*?<span.*?">(.*?)<\/span>.*?\n.*?class="wsod_stream">(.*?)<\/span>')
ans = re.findall(reg, r.text)
for key in ans[:30]:
    print("%-7s%-20s%-10s" % (key[0],key[1],key[2]))
