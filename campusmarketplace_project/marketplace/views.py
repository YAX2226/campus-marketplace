from django.shortcuts import render
from .models import Product,Category
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
    try:
        category = Category.objects.get(name='architecture')
        products = Product.objects.filter(category=category)
    except Category.DoesNotExist:
        products = []  # or handle error
    return render(request, 'architecture_buy.html', {'products': products})

def architecture_sell(request):
    return render(request, 'architecture_sell.html')

def engineering_buy(request):
    try:
        category = Category.objects.get(name='engineering')
        products = Product.objects.filter(category=category)
    except Category.DoesNotExist:
        products = []  # or handle error
    return render(request, 'engineering_buy.html', {'products': products})

def engineering_sell(request):
    return render(request, 'engineering_sell.html')

def pharmacy_buy(request):
    try:
        category = Category.objects.get(name='pharmacy')
        products = Product.objects.filter(category=category)
    except Category.DoesNotExist:
        products = []  # or handle error
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
            'category': product.category.name
        })
    return JsonResponse(data, safe=False)
