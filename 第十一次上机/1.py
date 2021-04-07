from bs4.builder import HTML
import requests
from bs4 import BeautifulSoup
from lxml import etree

headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.11 Safari/537.36'}

urls='https://search.jd.com/Search?keyword=python&wq=python&page={}&s=116&click=0'.format(str(2*1-1))
r=requests.get(urls,headers=headers)
print(r.status_code)
print(r.text)
html = etree.HTML(r.text)
#print(html)
html_data = html.xpath('//*[@id="J_pro_12899078"]/i[1]/text()')
print(html_data)