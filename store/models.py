from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    CATEGORY_CHOICE = [
        ('electronics' , 'Electronics'),
        ('clothing' , 'Clothing'),
        ('book' , 'Book'),
        ('home' , 'Home'),
        ('cosmetics' , 'Cosmetics'),
        ('accessories' , 'Accessories'),
        ('kitchen' , 'Kitchen'),
        ('furniture' , 'Furniture')
    ]
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image_url = models.URLField( blank=True, null=True)
    category = models.CharField(max_length=50 , choices=CATEGORY_CHOICE , default='home')

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    shipping_address = models.TextField()
    total_price = models.DecimalField(max_digits=10 , decimal_places=2)
    
    def __str__(self):
        return f"Order {self.id} by {self.user.username}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"



class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name