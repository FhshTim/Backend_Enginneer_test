# Part2_1
import requests
from bs4 import BeautifulSoup

#url = 'https://www.ptt.cc/bbs/Spurs/index.html'
url = input("Please put the url:")

def crawler_ptt(url):
    for round in range(3):
        res = requests.get(url)
        soup = BeautifulSoup(res.text,'html.parser')    
        articles_all = soup.select('div.r-ent')
        next_page = soup.select('div.btn-group-paging a')
        next_url = 'https://www.ptt.cc'+next_page[1]['href']
        
        url = next_url
        for each_po in articles_all:
            print("日期:"+each_po.select('div.date')[0].text,"作者:"+each_po.select('div.author')[0].text,"標題:"+each_po.select('div.title a')[0].text)

crawler_ptt(url)

