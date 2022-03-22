import requests
from bs4 import BeautifulSoup
import requests_cache

# Do the same with https://stacker.com/stories/1587/100-best-movies-all-time

requests_cache.install_cache('demo_cache')


class ImdbScraper(object):

    def __init__(self, url):
        self. url = url
        self.data = {}

    def get_request(self):
        return requests.get(self.url).text

    def get_soup(self):
        return BeautifulSoup(self.get_request(), 'html.parser')

    def get_top_imdb(self):
        table = self.get_soup().find('tbody')
        rows = table.find_all('tr')
        for row in rows:
            columns = row.find_all('td', limit=3)
            save = []
            for cell in columns[1:]:
                title_info = list(map(lambda data: data.get_text().strip(), cell))
                save.append(list(filter(lambda data: data, title_info)))
            self.data[f'{" ".join(save[0])}'] = save[1][0]

        return self.data


if __name__ == "__main__":

    solution = ImdbScraper(r'https://www.imdb.com/chart/top/').get_top_imdb()
    for title, rating in solution.items():
        print(f"{title}: {rating}")
