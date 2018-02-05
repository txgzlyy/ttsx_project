# coding = utf-8
from django.shortcuts import render
from models import *

# Create your views here.

def login(req):
    return render(req,'userInfo/login.html')
