from django.db import db

class Product(db.Model):
    name = db.CharField(max_length=100)
    description = db.TextField()
    price = db.DecimalField(max_digits=10, decimal_places=2)
    created_at = db.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
