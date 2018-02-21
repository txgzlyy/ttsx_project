# coding=utf-8
from django.shortcuts import render
from django.core.paginator import Paginator
from models import *

from haystack.generic_views import SearchView
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
    try:
        order_str = '-id'
        # 默认升序
        desc = req.GET.get('desc','1')
         # 默认第一页
        num = req.GET.get('page',1)
        # 判断排序规则
        order = req.GET.get('order','1')
        if order == '2': # 价格排序
            if desc == '1': # 升序
                order_str = 'gpric'
            else:
                order_str = '-gpric'
        elif order == '3': # 点击量排序
            order_str = 'gclicks'

        id = req.GET.get('id',0)
        goods = GoodsType.objects.get(pk=id)
        goods_info = goods.goodsinfo_set.order_by(order_str)

        paginator = Paginator(goods_info,10)   # 每页15条
        page = paginator.page(num)  # 第 num 页数据

        context = {'title':'商品列表','car_order': 'ok', 'user': '', 'goods': goods,
                   'goods_info':page,'ngoods':goods_info[:2],'order':order,'desc':desc
                   }
        return render(req,'goods/list.html',context)
    except:
        return render(req,'404.html')


def detail(req):
    try:
        if req.GET.get('id'):
            id = req.GET.get('id')
            goods = GoodsInfo.objects.get(pk=id)
            #增加点击量
            goods.gclicks += 1
            goods.save()
            # 推荐商品  找出该商品所在的类型 再去该类型的另外两个商品
            tgoods = goods.gtype.goodsinfo_set.order_by('-id')[:2]
            context = {'title': '商品详情', 'car_order': 'ok', 'user': '', 'goods': goods,"tgoods":tgoods}
            reqest = render(req, 'goods/detail.html', context)
            # 记录最近浏览信息
            id_lists = []
            if req.COOKIES.has_key('glist_id'):
                id_lists = req.COOKIES['glist_id'].split(',')   # 字符串转列表
            # 把重复浏览的 重新拍到前面
            if id in id_lists:
                id_lists.remove(id)
            id_lists.insert(0,id)
            # 如果大于5条  删掉最后一条
            if len(id_lists)>5:
                id_lists.pop()
            glist_id = ','.join(id_lists)  # 列表转字符串
            reqest.set_cookie('glist_id',value=glist_id,max_age=60*60*24*7)

            return reqest
        else:
            return render(req, 'goods/list.html')
    except:
        return render(req, '404.html')


class MySearchView(SearchView):
    def get_context_data(self, *args, **kwargs):
        context = super(MySearchView, self).get_context_data(*args, **kwargs)
        # do something
        context['car_order'] = 'ok'   # 添加自己的上下文
        return context
