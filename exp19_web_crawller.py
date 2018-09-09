import requests
from bs4 import BeautifulSoup
import certifi

def trade_spider(max_pages):
    page=1
    while page < max_pages:
        url=r"https://www.w3schools.com/html/page"+str(page)+".htm"
        print(url)
        page+=1
        source_code=requests.get(url)
        plain_text=source_code.text
        soup=BeautifulSoup(plain_text)
   
        for link in soup.findAll('a',{'class':'item'}):
            href=link.get('href')
            print(href)

trade_spider(3)
