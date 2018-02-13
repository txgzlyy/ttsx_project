#coding=utf-8
from django.shortcuts import redirect
#检查函数
def check(fun):
    def inner_check(req,*args,**kwargs):
        if req.session.get('uid'):
            return fun(req,*args,**kwargs)    #  注意 return 回去
        else:
            return redirect('/user/login/')
    return inner_check



'''
req.get_full_path()  包括参数
req.path   不包括参数
'''