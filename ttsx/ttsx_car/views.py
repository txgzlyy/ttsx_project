# coding=utf-8
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from models import *
from ttsx_goods.models import *
from userInfo.user_check import *
from userInfo.models import *

#import simplejson
# Create your views here.

@check
def mycar(req):
    goods_list = []
    uid = int(req.session.get('uid'))
    ucart = CarInfo.objects.filter(user_id=uid)
    context = {'title': '我的购物车', 'position_name':'购物车','ucart':ucart}
    return render(req,'cart.html',context)

@check
def place_order(req):
    goods_list = []
    uid = int(req.session.get('uid'))
    ucart = CarInfo.objects.filter(user_id=uid)
    user = UserInfo.objects.filter(id=uid)[0]
    context = {'title': '提交订单', 'position_name': '提交订单','ucart':ucart,'user':user}
    return render(req, 'place_order.html', context)


def caradd(req):
    try:
        uid = req.session.get('uid','0')
        gid = int(req.GET.get('id','0'))
        cont = int(req.GET.get('cont','1'))

        carts = CarInfo.objects.filter(user_id=uid,goods_id=gid)
        if len(carts)==1:  # 买过了
            carinfo = carts[0]
            carinfo.cont += cont
            carinfo.save()
        else:
            carinfo = CarInfo()
            carinfo.user_id = uid
            carinfo.goods_id = gid
            carinfo.cont = cont
            carinfo.save()
        return JsonResponse({'isadd': 1})
    except:
        return JsonResponse({'isadd':0})


def carchange(req):
    try:
        get = req.GET.get('infos')
        uid = req.session.get('uid','0')
        info = eval(get)  # 字符串转对象
        for item in info:
            gid = item['id']
            cont = item['cont']
            carts = CarInfo.objects.filter(user_id=uid,goods_id=gid)
            if len(carts)==1:  # 买过了
                carinfo = carts[0]
                carinfo.cont = cont
                carinfo.save()
        return JsonResponse({'ischange': 1})
    except:
        return JsonResponse({'ischange':0})


def dels(req):
    try:
        uid = req.session.get('uid', '0')
        gid = int(req.GET.get('id', '0'))
        CarInfo.objects.filter(user_id=uid, goods_id=gid).delete()
        return JsonResponse({'isdel': 1})
    except:
        return JsonResponse({'isdel': 0})


def cont(req):
    uid = int(req.session.get('uid'))
    ucart = CarInfo.objects.filter(user_id=uid)
    cont = len(ucart)
    return JsonResponse({'cont': cont})















