#coding=utf-8
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from models import *
from hashlib import sha1
import datetime
from user_check import *

from ttsx_goods.models import *
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
    user_name = req.COOKIES.get('uname',' ')
    return render(req, 'userInfo/login.html', {'title': '登录','user_name':user_name})

def loging(req):
    user_name = req.POST.get('username','')
    pass_word = req.POST.get('pwd','')
    remeber = req.POST.get('remeber',False)
    context = {'title':'登录','user_name':user_name,'pass_word':pass_word}
    m = sha1()
    m.update(pass_word)
    pass_word_m = m.hexdigest()
    try:
        mysql_user = UserInfo.objects.get(user_name=user_name)
        if mysql_user.pass_word == pass_word_m:
            # 登录成功  记录存入sessions
            req.session['uid'] = mysql_user.id
            req.session['uname'] = user_name
            #如果用户选择记住用户名 写入cookie
            #print(req.session.get('path'))
            if req.session.get('path'):
                response = redirect(req.session.get('path'))
            else:
                response = redirect('/user/')
            if remeber=='1':
                response.set_cookie('uname',value=user_name,expires=datetime.datetime.now()+datetime.timedelta(days = 7))
            else:
                response.set_cookie('uname',value='',max_age=-1)
            return response
        else:
            context['upwd_err'] = 1
            return render(req,'userInfo/login.html',context)
    except Exception as e:
        context['uname_err'] = 1
        return render(req, 'userInfo/login.html',context)

def islogin(req):
    res = 0
    if req.session.has_key('uid'):
        res = 1
    return JsonResponse({'data':res})

def logout(req):
    req.session.flush()
    return redirect('/user/login/')

@check
def info(req):
    user = UserInfo.objects.get(id=req.session.get('uid'))
    # 最近浏览
    newgoods = []
    id_lists = req.COOKIES['glist_id'].split(',')
    for id in id_lists:
        newgoods.append(GoodsInfo.objects.filter(id=id)[0])
    context = {'title': '用户中心', "active": "info", 'user': user,'position_name':'用户中心','newgoods':newgoods}
    return render(req, 'userInfo/user_center_info.html', context)

@check
def order(req):
    user = UserInfo.objects.get(id=req.session.get('uid'))
    context = {'title': '用户中心', "active": "order", 'user': user,'position_name':'用户中心'}
    return render(req,'userInfo/user_center_order.html',context)

@check
def site(req):
    user = UserInfo.objects.get(id=req.session.get('uid'))
    if req.method == 'POST':
        post = req.POST
        user.shou_name = post.get('shou_name')
        user.address = post.get('address')
        user.you_bian = post.get('you_bian')
        user.tel_num = post.get('tel_num')
        user.save()
    context = {'title': '用户中心', "active": "address", 'user': user,'position_name':'用户中心'}
    return render(req,'userInfo/user_center_site.html',context)









