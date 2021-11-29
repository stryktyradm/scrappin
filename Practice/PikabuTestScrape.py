import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import csv


def write_csv(data):

    pass


def get_community_data(html):

    pass


def get_data(url, headers, payload):

    pass


def main():

    url = 'https://pikabu.ru/ajax/communities_actions.php'

    headers = {
        'path': '/ajax/communities_actions.php',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://pikabu.ru',
        'refer': 'https://pikabu.ru/communities'
    }

    payload = {
        'action': 'get_communities',
        'text': None,
        'filterType': 'all',
        'sort': 'actual',
        'type': 'all',
        'tag': None,
        'page': ''
    }

    get_data(url, headers, payload)


if __name__ == '__main__':
    main()
