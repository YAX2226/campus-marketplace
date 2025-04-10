from django.shortcuts import render
from .models import Product
from django.http import JsonResponse


def homepage(request):
    return render(request, 'index.html')

def login_page(request):
    return render(request, 'login.html')

def signup_page(request):
    return render(request, 'signup.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def architecture_buy(request):
    products = Product.objects.filter(category='Architecture')
    return render(request, 'architecture_buy.html', {'products': products})

def architecture_sell(request):
    return render(request, 'architecture_sell.html')

def engineering_buy(request):
    products = Product.objects.filter(category='Engineering')
    return render(request, 'engineering_buy.html', {'products': products})

def engineering_sell(request):
    return render(request, 'engineering_sell.html')

def pharmacy_buy(request):
    products = Product.objects.filter(category='Pharmacy')
    return render(request, 'pharmacy_buy.html', {'products': products})

def pharmacy_sell(request):
    return render(request, 'pharmacy_sell.html')


def product_list(request):
    products = Product.objects.all()
    data = []
    for product in products:
        data.append({
            'name': product.name,
            'quality': product.quality,
            'price': str(product.price),
            'photo1': product.photo1.url if product.photo1 else '',
            'photo2': product.photo2.url if product.photo2 else '',
            'email': product.email,
            'category': product.category
        })
    return JsonResponse(data, safe=False)
