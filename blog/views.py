from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Shop, Review
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required

def index(request):
    category_list = Category.objects.all()
    return render(request, 'blog/index.html', {
        'category_list':category_list,
    })

def shop_list(request, pk):
    shop_list = Shop.objects.all()
    return render(request, 'blog/category_detail.html', {
        'shop_list': shop_list,
    })

def shop_detail(request, pk):
    shop = get_object_or_404(Shop, pk=pk)
    return render(request, 'blog/shop_detail.html', {
        'shop': shop,
    })

@login_required
def review_new(request, shop_pk):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.shop = get_object_or_404(Shop, pk=shop_pk)
            review.user = request.user
            review.save()
            return redirect('blog:shop_detail', shop_pk)
    else:
        form = ReviewForm()
    return render(request, 'blog/review_form.html', {
        'form': form,
    })

@login_required
def review_edit(request, shop_pk, pk):
    review = get_object_or_404(Review, pk=pk)

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            review.shop = get_object_or_404(Shop, pk=shop_pk)
            review.user = request.user
            review.save()
            return redirect('blog:shop_detail', shop_pk)
    else:
        form = ReviewForm(instance=review)
    return render(request, 'blog/review_form.html', {
        'form': form,
    })
