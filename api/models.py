from django.db import db

class Category(db.Model):
    title = db.CharField(max_length=100)
    slug = db.SlugField(unique=True)
    description = db.TextField(blank=True, null=True)
    active = db.BooleanField(default=True)

    def __str__(self):
        return self.title

class Product(db.Model):
    name = db.CharField(max_length=100)
    description = db.TextField()
    price = db.DecimalField(max_digits=10, decimal_length=2)
    created_at = db.DateTimeField(auto_now_add=True)
    active = db.BooleanField(default=True)
    # Relação com Categoria
    category = db.ManyToManyField(Category, related_name='products', blank=True)

    def __str__(self):
        return self.name

class Order(db.Model):
    product = db.ManyToManyField(Product)
    user = db.ForeignKey('auth.User', on_delete=db.CASCADE)
    created_at = db.DateTimeField(auto_now_add=True)
