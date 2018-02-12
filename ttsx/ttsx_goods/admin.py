from django.contrib import admin
from models import *
# Register your models here.

class GoodsTypeAdmin(admin.ModelAdmin):
    list_display = ['id','tname','isdelete']


admin.site.register(GoodsType,GoodsTypeAdmin)

class GoodsInfoAdmin(admin.ModelAdmin):
    list_display = ['id','gname','gpric','gclicks','gkucun','gtype','isdelete']
    list_per_page = 15
    list_filter = ['gtype']


admin.site.register(GoodsInfo,GoodsInfoAdmin)