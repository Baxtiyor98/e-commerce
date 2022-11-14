import json

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Category, Product, Cart, Order_Product
from django.db.models import Q


def index(request):
    category = Category.objects.all()
    cart = Cart.objects.filter(user=request.user).first()
    if cart:
        cart_list = cart.order_product.all()
    return render(request, 'index.html', context={'categories': category,
                                                  'cart_list': cart_list,
                                                  'products': Product.objects.filter(category=category.first().id)
                                                  })


def search(request):
    if request.method == 'POST':
        search = request.POST.get('search')
        products = Product.objects.filter(Q(name__icontains=search) | Q(price__icontains=search))
        return render(request, 'search.html', context={'products': products})


def contact(request):
    return render(request, 'contact.html')


def checkout(request):
    return render(request, 'checkout.html')


def cart(request):
    return render(request, 'cart.html')


def blogSingle(request):
    return render(request, 'blog-single-sidebar.html')


# Create your views here.

# TODO:JavaScript

def get_category(request):
    data = json.loads(request.body)
    products = Product.objects.filter(category_id=data['id'])
    pd = [{"id": p.id, "name": p.name, 'image': p.imageURL, 'price': p.price, 'discount': p.discount_price,
           "category": p.category.name} for p in products]
    response = {'products': pd}
    return JsonResponse(response)


@login_required(login_url='login')
def add_product(request):
    data = json.loads(request.body)
    id = data.get('id')
    product = Product.objects.get(id=int(id))
    cart, cart_created = Cart.objects.get_or_create(user=request.user)
    order, created_order = Order_Product.objects.get_or_create(cart=cart, product=product)
    order_product = Order_Product.objects.filter(cart=cart)

    for p in order_product:
        p.summa
        p.save()

    total_price = cart.total_summa
    if not created_order:
        order.quantity += 1
        order.save()
    return JsonResponse({'order_quantity': order.quantity,'total_price':total_price})

def remove_product(request):
    data = json.loads(request.body)
    id = data.get('id')
    order_product = Order_Product.objects.get(product_id=id).delete()
    return JsonResponse({})
