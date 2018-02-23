# coding=utf-8
from django.db import models
from userInfo.models import UserInfo
from ttsx_goods.models import GoodsInfo
# Create your models here.

class OrderMain(models.Model):
    order_id = models.CharField(max_length=20,primary_key=True) #201802231515+uid
    user = models.ForeignKey(UserInfo)
    set_time = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=8,decimal_places=2,default=0)
    order_state = models.BooleanField(default=False)

class OrderDetail(models.Model):
    order = models.ForeignKey(OrderMain)
    goods = models.ForeignKey(GoodsInfo)
    cont = models.IntegerField()
    pric = models.DecimalField(max_digits=5,decimal_places=2)