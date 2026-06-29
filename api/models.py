from django.db import models  # <-- O erro estava aqui

class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2) # Corrigido: decimal_places
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    category = models.ManyToManyField(Category, related_name='products', blank=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    product = models.ManyToManyField(Product)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)