import datetime
from time import sleep

from bs4 import BeautifulSoup
import requests


def get_countries_betexplorer():
    try:
        url = "https://www.betexplorer.com/"
        response = requests.get(url)
        html = BeautifulSoup(response.content, 'html.parser')

        article = html.find('article', {'id': 'countrymenu-home'})
        if article is None:
            return

        countries = []
        all_a = article.find_all('a')

        for a in all_a:
            name = a.text
            url = a.attrs['href']
            countries.append({'name': name, 'url': url})

        sorted_countries = sorted(countries, key=lambda item: item['name'])

        for country in sorted_countries:
            print(country)

    except BaseException as e:
        print(e)


get_countries_betexplorer()
print('taskin')
