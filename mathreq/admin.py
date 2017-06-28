# -*- coding: utf-8 -*-
from django.contrib import admin
from  .models import MathReq


class MathReqAdmin(admin.ModelAdmin):
    list_display = ('id','title','code','output','input','created','error_msg')

admin.site.register(MathReq, MathReqAdmin)

