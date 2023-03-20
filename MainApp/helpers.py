import requests
from bs4 import BeautifulSoup


def sort(item):
    return item['count']


def calCount(url, word):
    r = requests.get(url, allow_redirects=False)
    soup = BeautifulSoup(r.content.lower(), 'lxml')
    count = soup.body.get_text(strip=True).lower().count(word.lower())
    return count
