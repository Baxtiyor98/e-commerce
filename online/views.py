import json

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Category, Product, Cart, Order_Product
from django.db.models import Q


def index(request):
    category = Category.objects.all()
    try:
        cart = Cart.objects.filter(user=request.user).first()
        orders = cart.order_product.all()

        for i in orders:
            i.summa

        if cart:
            cart_list = cart.order_product.all()
            total_price = cart.total_summa
        return render(request, 'index.html', context={'categories': category,
                                                      'cart_list': cart_list,
                                                      'products': Product.objects.filter(category=category.first().id),
                                                      'total_price': total_price,
                                                      })
    except:
        return render(request, 'index.html', context={'categories': category,
                                                      'products': Product.objects.filter(category=category.first().id),
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
    cart, cart_created = Cart.objects.get_or_create(user=request.user)
    orders = cart.order_product.all()

    for i in orders:
        i.summa

    if cart:
        cart_list = cart.order_product.all()
        total_price = cart.total_summa

    return render(request, 'cart.html', context={'cart_list': cart_list, 'total_price': total_price, })


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


@login_required(login_url='log_in')
def add_product(request):
    data = json.loads(request.body)
    id = data.get('id')
    product = Product.objects.get(id=int(id))
    cart, cart_created = Cart.objects.get_or_create(user=request.user)

    if cart_created:
        cart.product.add(product)
        Order_Product.objects.create(cart=cart, product=product)
    else:
        try:
            order_product = Order_Product.objects.get(cart=cart, product=product)
            order_product.add
        except:
            order_product = Order_Product.objects.create(cart=cart, product=product)
        cart.product.add(product)

    for i in cart.order_product.all():
        i.summa

    data = [{
        "id": i.product.id,
        "name": i.product.name,
        "image": i.product.imageURL,
        "price": i.product.discount_price,
        "quantity": i.quantity,
    } for i in cart.order_product.all()]

    return JsonResponse({'data': data,
                         'count': len(cart.order_product.values_list('product', flat=True)),
                         "total_price": cart.total_summa,
                         })


def remove_product(request):
    data = json.loads(request.body)
    id = data.get('id')
    cart = Cart.objects.get(user=request.user)
    try:
        order_product = Order_Product.objects.get(cart=cart, product_id=id)
        order_product.delete()
        cart.product.remove(Product.objects.get(id=id))

        for i in cart.order_product.all():
            i.summa
        return JsonResponse({'count': len(cart.order_product.values_list('product', flat=True)),
                             'total_price': cart.total_summa,
                             'success': True,
                             })
    except:
        return JsonResponse({'count': len(cart.order_product.values_list('product', flat=True)),
                             'total_price': cart.total_summa,
                             'success': False,
                             })
