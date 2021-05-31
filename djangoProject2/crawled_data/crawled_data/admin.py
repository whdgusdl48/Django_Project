from django.contrib import admin

# Register your models here.
from crawled_data.models import BoardData,BoardData2

admin.site.register(BoardData)
admin.site.register(BoardData2)