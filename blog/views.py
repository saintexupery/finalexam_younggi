from django.shortcuts import render
from .models import Category, Shop

def index(request):
    category_list = Category.objects.all()
    return render(request, 'blog/index.html', {
        'category_list':category_list,
    })