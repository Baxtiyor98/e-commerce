from django.urls import path
from .views import index, contact, checkout, cart, blogSingle, search, get_category, add_product,remove_product

urlpatterns = [
    path('',index,name='index'),
    path('search/',search,name='search'),
    path('contact/',contact,name='contact'),
    path('checkout/',checkout,name='checkout'),
    path('cart/',cart,name='cart'),
    path('blog-single/', blogSingle,name='blog-single'),

    path('get_category/', get_category,name='get_category'),
    path('add_product/', add_product,name='add_product'),
    path('remove_product/', remove_product,name='remove_product'),
]