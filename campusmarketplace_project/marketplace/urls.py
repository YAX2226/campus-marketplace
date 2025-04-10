from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('login/', views.login_page, name='login'),
    path('login.html', views.login_page),
    path('signup/', views.signup_page, name='signup'),
    path('signup.html', views.signup_page),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard.html', views.dashboard),
    path('architecture/buy/', views.architecture_buy, name='architecture_buy'),
    path('architecture_buy.html', views.architecture_buy),
    path('architecture/sell/', views.architecture_sell, name='architecture_sell'),
    path('architecture_sell.html', views.architecture_sell),
    path('engineering/buy/', views.engineering_buy, name='engineering_buy'),
    path('engineering_buy.html', views.engineering_buy),
    path('engineering/sell/', views.engineering_sell, name='engineering_sell'),
    path('engineering_sell.html', views.engineering_sell),
    path('pharmacy/buy/', views.pharmacy_buy, name='pharmacy_buy'),
    path('pharmacy_buy.html', views.pharmacy_buy),
    path('pharmacy/sell/', views.pharmacy_sell, name='pharmacy_sell'),
    path('pharmacy_sell.html', views.pharmacy_sell),
]
