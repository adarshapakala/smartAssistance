from bs4 import BeautifulSoup as bs
import requests
import selenium.webdriver as wd

url ="https://www.moneycontrol.com/india/stockpricequote/banks-private-sector/yesbank/YB"
headers ={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

page = requests.get(url, headers=headers)

soup = bs(page.content, 'html.parser')
## print(soup.prettify())
for lists in soup.find_all('ul', {'class':'clearfix val_listinner'}):
    for col in soup.find_all('li', {'class':'clearfix'}):
        for row in soup.find_all('div',{'class':'value_txtfl'}):
            row1=str(row)
            a=row1.find('Market Cap')
            if a > 0:
                val = soup.find('div',{'class':'value_txtfr'})
                print(soup.name.string)




    # for cell2 in row.find_all(text=True):
    #     print(cell2)
    # for cell in row.find(['b']):
    #     print(cell)
