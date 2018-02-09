#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from models import *
from hashlib import sha1

# Create your views here.

def register(req):
    return render(req,'userInfo/register.html',{'title':'注册'})

def regist(req):
    try:
        user = UserInfo()
        user.user_name = req.POST.get('user_name')
        user.pass_word = req.POST.get('pwd')
        user.emails = req.POST.get('email')
        user.save()
        return HttpResponseRedirect('/user/login/')
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

def login(req):
    return render(req,'userInfo/login.html',{'title':'登录'})

def loging(req):
    user_name = ''
    pass_word = ''
    if req.POST.get('username'):
        user_name = req.POST.get('username')
        pass_word = req.POST.get('pwd')
    context = {'title':'登录','user_name':user_name,'pass_word':pass_word}

    m = sha1()
    m.update(pass_word)
    pass_word = m.hexdigest()
    try:
        mysql_user = UserInfo.objects.get(user_name=user_name)
        #print(mysql_user.pass_word)
        if mysql_user.pass_word == pass_word:
            return HttpResponseRedirect('/user/info/')#HttpResponse('OK')
        else:
            context['upwd_err'] = 1
            return render(req,'userInfo/login.html',context)
    except Exception as e:
        context['uname_err'] = 1
        return render(req, 'userInfo/login.html',context)




def info(req):
    return render(req,'userInfo/user_center_info.html',{'title':'用户中心'})






