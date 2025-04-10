from django.shortcuts import render

def homepage(request):
    return render(request, 'index.html')

def login_page(request):
    return render(request, 'login.html')

def signup_page(request):
    return render(request, 'signup.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def architecture_buy(request):
    return render(request, 'architecture_buy.html')

def architecture_sell(request):
    return render(request, 'architecture_sell.html')

def engineering_buy(request):
    return render(request, 'engineering_buy.html')

def engineering_sell(request):
    return render(request, 'engineering_sell.html')

def pharmacy_buy(request):
    return render(request, 'pharmacy_buy.html')

def pharmacy_sell(request):
    return render(request, 'pharmacy_sell.html')
