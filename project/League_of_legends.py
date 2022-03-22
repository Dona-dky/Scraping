import requests
from bs4 import BeautifulSoup
import pandas as pd
import requests_cache

requests_cache.install_cache('demo_cache')

url = r'https://leagueoflegends.fandom.com/wiki/List_of_champions'


def get_list_of_champions_page():
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')
    return soup


def get_list_of_champions_beginning():
    soup = get_list_of_champions_page()

    data = {}
    #Tout le contenu du site
    all_content = soup.find(class_="mw-parser-output")

    mon_h1 = soup.h1.get_text()
    data['h1'] = mon_h1

    see_also = all_content.findChild(class_="dablink")
    see_also_recup = see_also.get_text()
    data['More'] = see_also_recup

    content_champions = see_also.find_next_sibling().get_text().replace('\n', ' ')
    data['Description'] = content_champions

    toc = soup.find(class_="toc")
    #title_first_board = toc.findChild("h2").get_text()

    #1er tableau -> list toc
    first_board = content_champions.find_next_sibling()

    #titre du 1er tableau
    title_first_board = board.find_next_sibling().get_text()

    #title_first_board = soup.find(class_="toctitle").h2.text
    data['Title_first_board'] = title_first_board

    #first_board = toc.ul.text.replace('\n', ' ')
    #data['first_board'] = first_board

    return data


print(get_list_of_champions_beginning())
