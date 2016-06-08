from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pk>\d+)/$', views.shop_detail, name='shop_detail'),
    url(r'^(?P<shop_pk>\d+)/review/new/$', views.review_new, name='review_new'),
    url(r'^(?P<shop_pk>\d+)/review/(?P<pk>\d+)/edit/$', views.review_edit, name='review_edit'),
    url(r'^(?P<pk>\d+)/category_detail/$', views.shop_list, name='category_detail'),
]