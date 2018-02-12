# coding=utf-8
from django.db import models
from tinymce.models import HTMLField
# Create your models here.

class GoodsType(models.Model):
    tname = models.CharField(max_length=20)
    isdelete = models.BooleanField(default=False)
    def __str__(self):
        return self.tname.encode('utf-8')

class GoodsInfo(models.Model):
    gname = models.CharField(max_length=20)
    gimg = models.ImageField(upload_to='goods/')
    gpric = models.DecimalField(max_digits=5, decimal_places=2)  # 最大5位数   2位小数
    gclicks = models.IntegerField(default=0)
    gmete = models.CharField(max_length=20)  # 计量单位
    isdelete = models.BooleanField(default=False)
    gsubtitle = models.CharField(max_length=200)
    gkucun = models.IntegerField(100)
    gcount = HTMLField()  # 详细类容
    gtype = models.ForeignKey('GoodsType')
