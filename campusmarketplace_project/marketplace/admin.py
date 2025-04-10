from django.contrib import admin
from .models import Product, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quality', 'email', 'category')
    list_filter = ('category', 'quality')
    search_fields = ('name', 'email')
    readonly_fields = ('photo1_preview', 'photo2_preview')

    def photo1_preview(self, obj):
        if obj.photo1:
            return f'<img src="{obj.photo1.url}" style="height: 100px;" />'
        return "No Image"
    photo1_preview.allow_tags = True
    photo1_preview.short_description = "Photo 1 Preview"

    def photo2_preview(self, obj):
        if obj.photo2:
            return f'<img src="{obj.photo2.url}" style="height: 100px;" />'
        return "No Image"
    photo2_preview.allow_tags = True
    photo2_preview.short_description = "Photo 2 Preview"
