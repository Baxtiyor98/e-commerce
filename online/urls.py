from django.urls import path
from .views import index, about, contact, checkout, blog, cart

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('blog/', blog, name='blog'),
    path('checkout/', checkout, name='checkout'),
    path('contact/', contact, name='contact'),
    path('cart/', cart, name='cart'),
]