from django.contrib import admin
from .models import *



class HouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'created_at')


admin.site.register(House, HouseAdmin)
admin.site.register(Add_place)
