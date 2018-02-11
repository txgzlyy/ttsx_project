# coding=utf-8

from django.conf.urls import url
import views

urlpatterns = [
    url(r'^login/$',views.login),
    url(r'^loging/$',views.loging),
    url(r'^register/$',views.register),
    url(r'^check_name/$',views.check_name),
    url(r'^regist/$',views.regist),

    url(r'^$',views.info),
    url(r'^order/$',views.order),
    url(r'^site/$',views.site),
    url(r'^siteing/$',views.siteing),


]