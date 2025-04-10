from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('Architecture', 'Architecture'),
        ('Engineering', 'Engineering'),
        ('Pharmacy', 'Pharmacy'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
