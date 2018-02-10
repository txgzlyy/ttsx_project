#coding=utf-8
from django.shortcuts import render,redirect
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
    if req.session.get('uname'):
        user_name = req.session.get('uname')
        pass_word = req.session.get('upwd')

        m = sha1()
        m.update(pass_word)
        pass_word_m = m.hexdigest()

        mysql_user = UserInfo.objects.get(user_name=user_name)
        if mysql_user.pass_word == pass_word_m:
            req.session['uname'] = user_name
            req.session['upwd'] = pass_word
            return HttpResponseRedirect('/user/info/')
        else:
            return render(req, 'userInfo/login.html', {'title': '登录'})
    else:
        return render(req, 'userInfo/login.html', {'title': '登录'})


def loging(req):
    user_name = ''
    pass_word = ''
    remeber = False
    if req.POST.get('username'):
        user_name = req.POST.get('username')
        pass_word = req.POST.get('pwd')
        remeber = req.POST.get('remeber')
    context = {'title':'登录','user_name':user_name,'pass_word':pass_word}

    print(remeber)
    m = sha1()
    m.update(pass_word)
    pass_word_m = m.hexdigest()
    try:
        mysql_user = UserInfo.objects.get(user_name=user_name)
        #print(mysql_user.pass_word)
        if mysql_user.pass_word == pass_word_m:
            # 登录成功 如果用户选择记住密码 记录存入sessions
            if remeber=='1':
                req.session['uname'] = user_name
                req.session['upwd'] = pass_word
            return HttpResponseRedirect('/user/info/')#HttpResponse('OK')
        else:
            context['upwd_err'] = 1
            return render(req,'userInfo/login.html',context)
    except Exception as e:
        context['uname_err'] = 1
        return render(req, 'userInfo/login.html',context)




def info(req):
    name = user_name = req.session.get('uname')
    user = UserInfo.objects.get(user_name=name)
    user_info = {}
    user_info['name'] = user.shou_name
    user_info['tel'] = user.tel_num
    user_info['address'] = user.address
    context = {'title':'用户中心',"active":"info",'user':name,'user_info':user_info}
    return render(req,'userInfo/user_center_info.html',context)

def order(req):
    name = user_name = req.session.get('uname')
    context = {'title': '用户中心', "active": "order", 'user': name}
    return render(req,'userInfo/user_center_order.html',context)

def site(req):
    name = req.session.get('uname')
    context = {'title': '用户中心', "active": "address", 'user': name}
    return render(req,'userInfo/user_center_site.html',context)

def siteing(req):
    post = req.POST
    name = req.session.get('uname')
    try:
        user = UserInfo.objects.get(user_name=name)
        user.shou_name = post.get('shou_name')
        user.address = post.get('address')
        user.you_bian = post.get('you_bian')
        user.tel_num = post.get('tel_num')
        user.save()
        return redirect('/user/info/',{"res":True})
    except Exception as e:
        return HttpResponse(e)






