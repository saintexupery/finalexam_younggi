from django.contrib import admin
from django.contrib.humanize.templatetags.humanize import intcomma
from .models import Category

class PostAdmin(admin.ModelAdmin):
    list_display = ['category', 'created_at']

admin.site.register(Category, PostAdmin)