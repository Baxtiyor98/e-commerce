from django.urls import path
from .views import index, contact, checkout, blog, cart, order_category

urlpatterns = [
    path('', index, name='index'),
    path('blog/', blog, name='blog'),
    path('checkout/', checkout, name='checkout'),
    path('contact/', contact, name='contact'),
    path('cart/', cart, name='cart'),

    path('order_category/', order_category, name='order_category'),
]