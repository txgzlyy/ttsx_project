# coding=utf-8
from django.db import models
from ttsx_goods.models import GoodsInfo
from userInfo.models import UserInfo
# Create your models here.

class CarInfo(models.Model):
    '''谁买了多少个什么'''
    user = models.ForeignKey(UserInfo)
    goods = models.ForeignKey(GoodsInfo)
    cont = models.IntegerField(default=0)
    isplace = models.BooleanField(default=False)