from bs4 import BeautifulSoup as bs
import requests
ticker ='INFY'
stockParam ={"MarketCap":0, "BookVal":0, "PEratio":0, "Div_Yield":0,"ROCE":0, "ROE":0,"PriceToBook":0, "PEG":0, "DebtToEquity":0}
headers ={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
stockURL ="https://www.screener.in/company/"+ ticker+"/consolidated/"
page = requests.get(stockURL, headers=headers)
soup = bs(page.content, 'html.parser')
line = [] ## Declare a list to hold all the lines of the scrapped data

for params in soup.find_all(class_='four columns'): ##get first set of the parameters listed in the page(Screener.in lists parametrs in 2 sets)
    paramsText = params.get_text()
    paramLines = paramsText.split("\n")
    for i in paramLines:
        # if i.strip() != "":
        line.append(i.strip())

print(line)









