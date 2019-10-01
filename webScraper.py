from bs4 import BeautifulSoup as bs
import requests
import selenium.webdriver as wd

url ="https://www.moneycontrol.com/india/stockpricequote/banks-private-sector/yesbank/YB"
headers ={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

page = requests.get(url, headers=headers)

soup = bs(page.content, 'html.parser')
for b in soup.find_all(id ="standalone_valuation"):  ##Get into main group

    for a in soup.find_all('div',class_='value_txtfl'): ##Locate the item
        print(a.text)
        c = soup.find('div',class_='value_txtfr')
        print(c.text)







