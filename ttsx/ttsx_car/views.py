# coding=utf-8
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from models import *
from ttsx_goods.models import *
from userInfo.user_check import *
from userInfo.models import *
# Create your views here.

@check
def mycar(req):
    goods_list = []
    uid = int(req.session.get('uid'))
    ucart = CarInfo.objects.filter(user_id=uid)
    for item in ucart:
        goodsa = {'goods':GoodsInfo.objects.filter(id=item.goods_id)[0],'cont':item.cont}
        goods_list.append(goodsa)

    context = {'title': '我的购物车', 'position_name':'购物车','goods_lists':goods_list}
    return render(req,'cart.html',context)

@check
def place_order(req):
    goods_list = []
    uid = int(req.session.get('uid'))
    ucart = CarInfo.objects.filter(user_id=uid)
    user = UserInfo.objects.filter(id=uid)[0]
    for item in ucart:
        goodsa = {'goods':GoodsInfo.objects.filter(id=item.goods_id)[0],'cont':item.cont}
        goods_list.append(goodsa)

    context = {'title': '提交订单', 'position_name': '提交订单','goods_lists':goods_list,'user':user}
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
        uid = req.session.get('uid','0')
        gid = int(req.GET.get('id','0'))
        cont = int(req.GET.get('cont','1'))
        carts = CarInfo.objects.filter(user_id=uid,goods_id=gid)
        if len(carts)==1:  # 买过了
            carinfo = carts[0]
            carinfo.cont = cont
            carinfo.save()
        return JsonResponse({'isadd': 1})
    except:
        return JsonResponse({'isadd':0})


def dels(req):
    try:
        uid = req.session.get('uid', '0')
        gid = int(req.GET.get('id', '0'))
        CarInfo.objects.filter(user_id=uid, goods_id=gid).delete()
        return JsonResponse({'isdel': 1})
    except:
        return JsonResponse({'isdel': 0})



















