import requests
from bs4 import BeautifulSoup
import requests_cache

#requests_cache.install_cache('demo_cache')

page = r'http://www.scrapethissite.com/pages/forms/'

page = requests.get(page).text
soup = BeautifulSoup(page, 'html.parser')

table = soup.find(class_="table")
elements = table.findAll('tr')

for element in elements:
    if len(element) > 1:
        an_el = element.get_text()
        #cells = an_el.get_text()
        print(an_el)


#print(table)
#print(elements)
#http://www.scrapethissite.com/pages/forms/?page_num=1


