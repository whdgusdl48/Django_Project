import os
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup

os.environ.setdefault('DJANGO_SETTINGS_MODULE','djangoProject2.settings')
import django

django.setup()
from crawled_data.models import BoardData
def fetch_clien_latest_data():
    result = []

    url = 'https://music.bugs.co.kr/chart/track/realtime/total?wl_ref=M_contents_03_01'
    response = requests.get(url)

    html = response.text
    soup = BeautifulSoup(html,'html.parser')

    list_items = soup.find_all('table')[0]
    list_items_2 = list_items.find_all('tr')
    list_items_2 = list_items_2[1:]
    for item in list_items_2:
        title = item.find('th').find('p',class_="title").find('a').text
        rank = item.find_all('td')[1].find('div',class_='ranking').find('strong').text
        imgurl = item.find_all('td')[2].find('a').find('img').attrs['src']
        artist = item.find_all('td')[4].find('p').find('a').text

        img_obj = {
            'title' : title,
            'rank' : rank,
            'imgurl' : imgurl,
            'artist' : artist,
        }

        result.append(img_obj)

    return result
result = fetch_clien_latest_data()

def add_items(result):
    last_inserted_items = BoardData.objects.last()
    if last_inserted_items is None:
        last_inserted_id = ""
    else:
        BoardData.objects.all().delete()
    item_to_insert_db = []

    for item in result:
        item_to_insert_db.append(item)

    for item in item_to_insert_db:

        BoardData(title = item['title'],
                  ranking = item['rank'],
                  imgurl=  item['imgurl'],
            artist = item['artist']).save()

    return item_to_insert_db

add_items(result)