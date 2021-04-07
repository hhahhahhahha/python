import requests
import re

def stock_list():
    r = requests.get('http://money.cnn.com/data/dow30/', headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15'})
    search_pattern = re.compile('class="wsod_symbol">(.*?)<\/a>.*?<span.*?">(.*?)<\/span>.*?\n.*?class="wsod_stream">(.*?)<\/span>')
    stock_text = re.findall(search_pattern, r.text)
    return stock_text

stock = stock_list()
for i in range(len(stock)):
    print(stock[i])







