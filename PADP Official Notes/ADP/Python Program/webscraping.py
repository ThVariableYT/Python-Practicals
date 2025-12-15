import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
r = requests.get(URL)
print(r.text)
#print(r.content)
soup = BeautifulSoup(r.content, 'html.parser')
results = soup.find(id="ResultsContainer")
print(results.prettify())
#table = soup.findAll('div', attrs = {'id':'ResultsContainer'}) 
job_elements = results.find_all("div", class_="card-content")
for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()
#for row in table:
#    print(row.text.strip())'''
