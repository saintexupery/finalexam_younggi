from django.contrib import admin
from django.contrib.humanize.templatetags.humanize import intcomma
from .models import Category, Shop

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category', 'created_at']

class ShopAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'created_at']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Shop, ShopAdmin)