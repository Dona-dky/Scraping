import requests
import requests_cache
from bs4 import BeautifulSoup

requests_cache.install_cache('demo_cache')


class TestSiteScraper(object):

    def __init__(self, current_url):
        self.url = current_url
        self.data = dict()
        self.get_products()

    def make_request(self):
        page = requests.get(self.url)
        return page.text

    def make_soup(self):
        return BeautifulSoup(self.make_request(), 'html.parser')

    def get_requested_row(self):
        return self.make_soup().find_all(class_="row", limit=2)[1]

    def get_products(self):
        product_box = self.get_requested_row().find_all(class_=['col-sm-4 col-lg-4 col-md-4'])
        for box in product_box:
            caption = box.find(class_="caption")
            price, name, description = caption(['h4', 'p'])

            ratings = caption.find_next_sibling('div')('p')
            reviews, stars = ratings
            self.store_data(price, name, description, reviews, stars)

    def store_data(self, price, name, description, reviews, stars):
        self.data[name.text.strip()] = {
            "price": price.text,
            "description": description.text,
            "reviews": int(reviews.text[0]),
            "stars": int(stars['data-rating'])
        }

    def get_data(self):
        return self.data


if __name__ == "__main__":
    pages = [
        r'https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops',
        r'https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets',
        r'https://webscraper.io/test-sites/e-commerce/allinone/phones/touch'
    ]

    targets = ['Laptops', 'Tablets', 'Phones']

    data_to_export = {}
    for target, url in zip(targets, pages):
        data_to_export[target] = TestSiteScraper(url).get_data()

    for x, y in data_to_export.items():
        print(f"{x}:{y}")