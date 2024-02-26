import requests
from bs4 import BeautifulSoup
import csv
import time
import urllib
import fake_useragent

def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    print(r)
    return r

def get_pages_count(html):
    soup = BeautifulSoup(html, 'html.parser')
    paginationTo = soup.find('div', class_="pagination pagination-container")
    if paginationTo:
        pagination = paginationTo.find_all('a')
        print(pagination)
        print(int(pagination[-2].get_text()))
        return int(pagination[-2].get_text())
    else:
        return 1


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='col-lg-3 col-md-4 col-sm-6 col-xs-6 col-xxs-12 item item-parent catalog-block-view__item js-notice-block item_block')

    catalog = []
    for item in items:
        ImageLargePage = item.find('a').get('href')
        ImageLargePage2 = str(ImageLargePage)[1:]
        PageImageHref = str(HOST) + str(ImageLargePage2)
        html2 = get_html(PageImageHref)

        soup2 = BeautifulSoup(html2.text, 'html.parser')
        items2 = soup2.find('div', class_="product-detail-gallery__item product-detail-gallery__item--middle text-center")

        bb = items2.find('img').get('src')
        if bb:
            bb = items2.find('link').get('href')
        else:
            bb = ''
        items3 = soup2.find('div', class_='tab-content')
        print(items3)
        if items3:
            text = str(items3.get_text)
            print(text)
            text2 = text.replace('<br/>', '')
            text3 = text.replace('</div>', '')





HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'}
HOST = 'https://leonardo.ru/'

def parse():
    URL = 'https://leonardo.ru/ishop/tree_3811885809/'
    html = get_html(URL)
    if html.status_code == 200:
        catalog = []
        pages_count = get_pages_count(html.text)
        for page in range (1, pages_count + 1):
            print(f'Парсинг страницы {page} {pages_count} {URL} ...')
            html = get_html(URL, params={'pages': page})
            get_content(html.text)
            time.sleep(1)


parse()