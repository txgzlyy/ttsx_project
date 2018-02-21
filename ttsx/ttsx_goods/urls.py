# coding=utf-8
from django.conf.urls import url
import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^goods/list/$', views.type_list),
    url(r'^goods/detail/$',views.detail),
    url(r'^search/$', views.MySearchView.as_view(), name='search_view'),
]
