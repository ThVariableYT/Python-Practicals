import bs4 as bs
import urllib
import requests
import pandas as pd

sauce = requests.get('https://www.moneycontrol.com/stocksmarketsindia/')
soup = bs.BeautifulSoup(sauce.content, 'html.parser')
date = soup.find_all('span',class_ = 'robo_medium' )
dates = []
for i in date:
  dates.append(i.text)
net_fill_values = soup.find_all('td',class_ = 'tbl_greentxt')
net_fill = []
for i in net_fill_values:
  net_fill.append(i.text)
net_fill = net_fill[:len(dates)]
data_frame = pd.DataFrame({ 'Dates' : dates,'Net fill' : net_fill})
print(data_frame)




