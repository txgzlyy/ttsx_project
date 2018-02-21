# coding=utf-8


def check(req,lists):   # 在lists列表中就返回False
    for item in lists:
        if item == req.path:
            return False
    return True

class urlMiddleware(object):
    def process_view(self,req, view_func, view_args, view_kwargs):
        lists = ['/user/login/','/user/loging/','/user/logout/','/car/add/','/user/islogin/',
                 '/user/register/','/user/regist/','/user/check_name/']

        if check(req,lists):
            req.session['path'] = req.get_full_path()






