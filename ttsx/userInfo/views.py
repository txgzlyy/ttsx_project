#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from models import *

# Create your views here.

def login(req):
    return render(req,'userInfo/login.html')

def register(req):
    return render(req,'userInfo/register.html')

def info(req):
    return render(req,'userInfo/user_center_info.html')


def loging(req):
    user_name = ''
    pass_word = ''
    if req.POST.get('username'):
        user_name = req.POST.get('username')
        pass_word = req.POST.get('pwd')
    try:
        mysql_user = UserInfo.objects.get(user_name=user_name)
        #print(mysql_user.pass_word)
        if mysql_user.pass_word == pass_word:
            return HttpResponseRedirect('/user/info/')#HttpResponse('OK')
        else:
            return HttpResponse('密码错误')
    except Exception as e:
        return HttpResponse(e)
    #return HttpResponse('OK')


def regist(req):
    try:
        user = UserInfo()
        user.user_name = req.POST.get('user_name')
        user.pass_word = req.POST.get('pwd')
        user.emails = req.POST.get('email')
        user.save()
        return HttpResponseRedirect('/user/info/')
    except Exception as e:
        print(e)
        return JsonResponse({'data':e})

def check_name(req):
    res = False
    user_name = req.POST.get('user_name')
    try:
        mysql_user_name = UserInfo.objects.filter(user_name=user_name)
        if mysql_user_name:
            res = True
        return JsonResponse({'data':res})
    except Exception as e:
        return HttpResponse(e)

