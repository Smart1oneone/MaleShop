from django.contrib import admin
from django.urls import path

from goods.views import *

app_name = 'goods'
urlpatterns = [
    path('<slug:category_slug>/', GoodsView.as_view(), name='home'),
    path('search/', GoodsView.as_view(), name='search'),
    path('product/<slug:product_slug>', ProductsView.as_view(), name='product'),

]