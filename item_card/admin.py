from django.contrib import admin
from .models import *
# Register your models here.

admin.site.site_header = "a2z Shop"


class Item_cardAdmin(admin.ModelAdmin):
    list_display = ('id','img_title','img_img',)

admin.site.register(Item_card,Item_cardAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','id')

admin.site.register(Category,CategoryAdmin)


admin.site.register(Customer)
admin.site.register(Order)
