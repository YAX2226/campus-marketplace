from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    quality = models.CharField(max_length=100, default="Good")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    photo1 = models.ImageField(upload_to='product_photos/', default='product_photos/default.jpg')
    photo2 = models.ImageField(upload_to='product_photos/', default='product_photos/default.jpg')
    email = models.EmailField(default='seller@example.com')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"