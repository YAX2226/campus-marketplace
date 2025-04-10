from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'price', 'date_posted']
    search_fields = ['title']
    list_filter = ['category']

admin.site.register(Product, ProductAdmin)
