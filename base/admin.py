from django.contrib import admin
from .models import products
# Register your models here.


class Productadmin(admin.ModelAdmin):
    list_display=['id','trend','category','name','desc','price','image']


admin.site.register(products,Productadmin)