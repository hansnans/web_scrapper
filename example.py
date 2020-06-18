#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    URL = 'https://webscraper.io/test-sites/e-commerce/allinone'
    plain_html = requests.get(URL).text

    parser = BeautifulSoup(plain_html, 'html.parser')

    elements = parser.find('div', {'class': 'test-site'}).find('div', {'class': 'row'}).find('div', {'class': 'col-md-9'})

    for box in elements.find('div', {'class': 'row'}).find_all('div', {'class': 'caption'}):
        header = box.find('h4', {'class': ''})
        print(header.a['title'])
