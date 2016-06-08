from django.shortcuts import render
from .models import Category, Shop

def index(request):
    category_list = Category.objects.all()
    shop_list = Shop.objects.all()
    return render(request, 'blog/index.html', {
        'category_list':category_list, 'shop_list': shop_list,
    })