# coding=utf-8
from django.shortcuts import render
from models import *
# Create your views here.

def index(req):
    #user = UserInfo.objects.get(id=req.session.get('uid'))

    # 6个分类
    #  3个最红商品
    # 4个最新商品
    goods_info=[]
    goods_type = GoodsType.objects.all()
    for type in goods_type:
        nlist = type.goodsinfo_set.order_by('-id')[0:4]      # type 类里的前四个(id 降序)
        clist = type.goodsinfo_set.order_by('-gclicks')[0:3]  # type 类里的前四个（点击量降序）
        goods_info.append({'type':type,'nlist':nlist,'clist':clist})

    context = {'title':'首页','car_order': 'ok', 'user': '', 'goods': goods_info}
    return render(req,'goods/index.html',context)


def type_list(req):
    goods = []
    goods_info = []
    active = 'id'
    if req.GET.get('id'):
        id = req.GET.get('id')
        goods = GoodsType.objects.get(pk=id)
        if req.GET.get('gpric'):
            goods_info = goods.goodsinfo_set.order_by('-gpric')
            active = 'gpric'
        elif req.GET.get('gclicks'):
            goods_info = goods.goodsinfo_set.order_by('gclicks')
            active = 'gclicks'
        else:
            goods_info = goods.goodsinfo_set.order_by('-id')

    context = {'title':'商品列表','car_order': 'ok', 'user': '', 'goods': goods,
               'goods_info':goods_info,'ngoods':goods_info[:2],'active':active
               }
    return render(req,'goods/list.html',context)


def detail(req):
    if req.GET.get('id'):
        id = req.GET.get('id')
        goods = GoodsInfo.objects.get(pk=id)
        # 推荐商品  找出该商品所在的类型 再去该类型的另外两个商品
        tgoods = GoodsType.objects.get(pk=goods.gtype.id).goodsinfo_set.order_by('-id')[:2]
        context = {'title': '商品详情', 'car_order': 'ok', 'user': '', 'goods': goods,"tgoods":tgoods}
        return render(req, 'goods/detail.html', context)
    else:
        return render(req, 'goods/list.html')
