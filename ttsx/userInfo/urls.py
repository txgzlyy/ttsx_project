# coding=utf-8

from django.conf.urls import url
import views

urlpatterns = [
    url(r'^login/$',views.login),
    url(r'^register/$',views.register),
    url(r'^info/$',views.info),

    url(r'^loging/$',views.loging),
    url(r'^check_name/$',views.check_name),
    url(r'^regist/$',views.regist),
]