# import libraries

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
    # All the content of the site
    all_content = soup.find(class_="mw-parser-output")

    # h1 of the site
    mon_h1 = soup.h1.get_text()
    data['h1'] = mon_h1

    # See also
    see_also = all_content.findChild(class_="dablink")
    see_also_recup = see_also.get_text()
    data['More'] = see_also_recup

    # Description
    content_champions = see_also.find_next_sibling()
    content_champions_recup = content_champions.get_text().replace('\n', ' ')
    data['Description'] = content_champions_recup

    # 1st tab -> class toc
    first_tab = content_champions.find_next_sibling()

    # Title of 1st tableau
    title_first_tab = first_tab.findChild(class_="toctitle")
    title_first_tab_recup = title_first_tab.h2.get_text()
    data['Title_first_tab'] = title_first_tab_recup

    # Data of tab
    list_tab = title_first_tab.find_next_sibling().text.replace('\n', ' ')
    data['list_tab'] = list_tab

    # Titre Available Champions
    h2_2_tab = first_tab.find_next_sibling()
    h2_2_tab_recup = h2_2_tab.get_text()
    data['h2 2nd tab'] = h2_2_tab_recup

    # 2eme tableau
    table = h2_2_tab.find_next_sibling().find('tbody')
    rows = table.find_all('tr')
    for row in rows:
        #if len(row) > 1:
        columns = row.find_all('th')
        cells = row.find_all('td')
        print(columns)
        print(cells)

        # for rows in table_body('tr'):
        # if len(rows) > 1:
        # column = rows.th.get_text()
        # cells = rows.td.get_text()
        # cells = cells.replace('\t', '').replace('\n', ' ')
        # print(cells)
        # data[column] = cells
        # data['name'] = h2_2_tab

    return data


print(get_list_of_champions_beginning())
