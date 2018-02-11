# coding=utf-8
from django.shortcuts import render

# Create your views here.

def index(req):
    #user = UserInfo.objects.get(id=req.session.get('uid'))
    return render(req,'index.html',{'car_order':'ok','user':''})