from django.conf.urls import url
import views

urlpatterns = [
    url(r'^info/$',views.mycar),
    url(r'^place/$',views.place_order),
    url(r'^add/$', views.caradd),
    url(r'^del/$', views.dels),
    url(r'^change/$',views.carchange),
    url(r'^cont/$',views.cont),
]