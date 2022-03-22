import requests
from bs4 import BeautifulSoup
import pandas as pd
import requests_cache

requests_cache.install_cache('demo_cache')

def get_pokedex_page(pokemon_name):
    page = 'http://pokemondb.net/pokedex/' + pokemon_name
    page = requests.get(page).text
    return BeautifulSoup(page, 'html.parser')


def get_pokemon_list_page(url):
    page = requests.get(url).text
    return BeautifulSoup(page, 'html.parser')


def get_cara_pokemon(pokemon_name):
    page = get_pokedex_page(pokemon_name)
    data = {}

    for table in page.find_all('table', {'class': "vitals-table"}, limit=4):
        table_body = table.tbody
        for rows in table_body('tr'):
            if len(rows) > 1:
                column = rows.th.get_text()
                cells = rows.td.get_text()
                cells = cells.replace('\t', '').replace('\n', ' ')
                data[column] = cells
                data['name'] = pokemon_name
    return data


def get_pokemon(soup, limit):
    pokemon = soup.find(class_="hlist hlist-separated").find_all('a', limit=limit)
    return list(map(lambda pokemon: pokemon.get_text(), pokemon))


if __name__ == "__main__":
    path = r'https://en.wikipedia.org/wiki/List_of_generation_I_Pok%C3%A9mon'
    all_pokemon = get_pokemon(get_pokemon_list_page(path), 5)

    data_to_export = []

    for pokemon in all_pokemon:
        data_to_export.append(get_cara_pokemon(pokemon))

    print(pd.DataFrame(data_to_export))