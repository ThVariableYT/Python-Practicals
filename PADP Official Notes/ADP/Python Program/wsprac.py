import requests
from bs4 import BeautifulSoup

URL="http://learn-javascript.in/"
r=requests.get(URL)
#print(r.content)
soup=BeautifulSoup(r.content, 'html.parser')
#print(soup.prettify())
table=soup.findAll('div',attrs={'class':'filter-list row clearfix'})
for row in table:
    print(row.text)
