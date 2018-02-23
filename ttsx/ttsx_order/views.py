# coding=utf-8
from django.shortcuts import render,redirect
from django.db import transaction
from datetime import datetime
from models import *
from ttsx_car.models import CarInfo
# Create your views here.
'''
1,创建主表
2，接受购物车请求
3，查询请求的购物车信息
4，判断库存
5，如果库存足够
  5.1，创建订单详细表
  5.2，修改库存
  5.3，计算总金额
  5.4，在购物车删除已经提交的商品信息
6，库存补足，放弃之前的保存并返回购物车
'''
@transaction.atomic
def order(req):
    ok = True
    sid = transaction.savepoint()
    try:
        uid = int(req.session.get('uid'))
        #1
        time_str = datetime.now().strftime('%Y%m%d%H&M%S')
        main = OrderMain()
        main.order_id = '%s%s'%(time_str,uid)
        main.user_id = uid
        main.order_state = 1
        main.save()
        #2   isplace=1 表示购物车中已经创建在订单中的商品
        print(11)
        ucart = CarInfo.objects.filter(user_id=uid, isplace=1)
        #3
        for cart in ucart:
            #4
            if cart.goods.gkucun>=cart.cont:
                #5.1
                order = OrderDetail()
                order.order = main
                order.goods = cart.goods
                order.cont = cart.cont
                order.pric = cart.goods.gpric
                order.save()
                #5.2
                cart.goods.gkucun -= cart.cont
                cart.goods.save()
                #5.3
                main.total += order.cont*order.pric
                main.save()
                #5.4
                cart.delete()
            else:
                ok = False

        if ok:
            transaction.savepoint_commit(sid)
            return redirect('/user/order/')
        else:
            transaction.savepoint_rollback(sid)
            return redirect('/car/info/')
    except:
        transaction.savepoint_rollback(sid)
        return redirect('/car/info/')


















