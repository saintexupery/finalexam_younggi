from django.shortcuts import render, get_object_or_404
from .models import Category, Shop

def index(request):
    category_list = Category.objects.all()
    shop_list = Shop.objects.all()
    return render(request, 'blog/index.html', {
        'category_list':category_list, 'shop_list': shop_list,
    })

def shop_detail(request, pk):
    shop = Shop.objects.get(pk=pk)
    return render(request, 'blog/shop_detail.html', {
        'shop': shop,
    })