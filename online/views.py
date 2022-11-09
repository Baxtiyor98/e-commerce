import json

from django.http import JsonResponse
from django.shortcuts import render

from online.models import Category, Product


# Create your views here.
def index(request):
    categories = Category.objects.all()
    return render(request, 'index.html', context={"categories": categories,
                                                  "products": Product.objects.filter(
                                                      category_id=categories.first().id)})


def blog(request):
    return render(request, 'blog-single-sidebar.html')


def cart(request):
    return render(request, 'cart.html')


def checkout(request):
    return render(request, 'checkout.html')


def contact(request):
    return render(request, 'contact.html')

# TODO: JS PART

def order_category(request):
    print(1111111111111111)
    data = json.loads(request.body)
    print(data)
    response = {
        "message":"salom"
    }
    return JsonResponse(response)
