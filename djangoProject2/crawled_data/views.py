from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import BoardData
from .clien_crawler import fetch_clien_latest_data, add_items
# Create your views here.

def make_Header(request):
    Music_list = ['Bugs','Genie']
    template = loader.get_template('crawled_data/index.html')
    context = {
        'Music_list' : Music_list
    }
    return HttpResponse(template.render(context,request))


def Bugs(requset):
    music_list = BoardData.objects.order_by('ranking')
    result = add_items(fetch_clien_latest_data())
    template = loader.get_template('crawled_data/Bugs.html')
    context = {
        'Bugs_list' : music_list,
        'refresh' : result
    }
    return HttpResponse(template.render(context,requset))


def genie(request):
    response = '지니 상위랭킹 1~100까지'
    return HttpResponse(response)