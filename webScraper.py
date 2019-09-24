from bs4 import BeautifulSoup as bs
import requests
import selenium.webdriver as wd

url ="https://www.moneycontrol.com/india/stockpricequote/banks-private-sector/yesbank/YB"
headers ={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

page = requests.get(url, headers=headers)

soup = bs(page.content, 'html.parser')
## print(soup.prettify())
a = soup.find_all('div', {'class':'value_txtfl'})
b = soup.find_all('div', {'class':'value_txtfl'})
tag=[]
vl=[]
c=0
for i in a:
    tag[c] =a[c].string
    vl[c] = b[c].string
    c+=1
    print(tag)
print('#########################################################################################################')
print(a)


