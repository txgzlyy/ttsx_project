# coding=utf-8
from django.db import models

# Create your models here.

class UserInfo(models.Model):
    user_name = models.CharField(max_length=20)
    pass_word = models.CharField(max_length=40)
    tel_num = models.CharField(max_length=11)
    emails = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    you_bian = models.CharField(max_length=20)