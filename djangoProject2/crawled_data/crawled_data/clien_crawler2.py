import os
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup

os.environ.setdefault('DJANGO_SETTINGS_MODULE','djangoProject2.settings')
import django

django.setup()
from crawled_data.models import BoardData2
def fetch_clien_latest_data2():
    result = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    url = 'https://www.genie.co.kr/chart/top200'
    response = requests.get(url,headers=headers)

    html = response.text
    soup = BeautifulSoup(html,'html.parser')

    list_items = soup.find_all('table')[0]
    list_items_2 = list_items.find_all('tr')

    list_items_2 = list_items_2[1:]
    for item in list_items_2:
        title = item.find_all('td')[4].find('a',class_="title ellipsis").text.strip()
        rank = item.find_all('td')[1].text.strip().replace('\n','')
        rank = rank.split(' ')
        ranks = rank[0]
        increase = rank[-1]
        print(increase)
        imgurl = item.find_all('td')[2].find('a').find('img').attrs['src']
        artist = item.find_all('td')[4].find('a',class_="artist ellipsis").text.strip()

        img_obj = {
            'title' : title,
            'rank' : ranks,
            'increase' : increase,
            'imgurl' : imgurl,
            'artist' : artist,
        }

        result.append(img_obj)

    return result
result = fetch_clien_latest_data2()
#
def add_items2(result):
    last_inserted_items = BoardData2.objects.last()
    if last_inserted_items is None:
        last_inserted_id = ""
    else:
        BoardData2.objects.all().delete()
    item_to_insert_db = []

    for item in result:
        item_to_insert_db.append(item)

    for item in item_to_insert_db:

        BoardData2(title = item['title'],
                  ranking = item['rank'],
                  imgurl=  item['imgurl'],
                increase= item['increase'],
            artist = item['artist']).save()

    return item_to_insert_db
#
add_items2(result)