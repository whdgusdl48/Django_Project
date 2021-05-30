from django.urls import path

from . import views

urlpatterns = [
    path('',views.make_Header,name='header'),
    path('Bugs/',views.Bugs,name='bugs'),
    path('Genie/',views.genie,name='genie'),
]