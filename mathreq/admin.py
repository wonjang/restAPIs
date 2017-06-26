from django.contrib import admin
from  .models import MathReq


class MathReqAdmin(admin.ModelAdmin):
    list_display = ('id','title','code','output','input','created')

admin.site.register(MathReq, MathReqAdmin)

