import requests

page = r'https://www.imdb.com/chart/top'
page = requests.get(page)
print(type(page))
print(page)
