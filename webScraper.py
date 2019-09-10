from bs4 import BeautifulSoup as bs
import requests
import selenium.webdriver as wd

url ="https://www.screener.in/company/LTTS/"
headers ={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

page = requests.get(url, headers=headers)

soup = bs(page.content, 'html.parser')
## print(soup.prettify())
price = soup.find_all(attrs={'class':'four columns'})
print(price[0])