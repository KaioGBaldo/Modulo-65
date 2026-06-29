from rest_framework import serializers
from .models import Product, Category, Order

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'slug', 'description', 'active']

class ProductSerializer(serializers.ModelSerializer):
    # Mostra os detalhes da categoria no GET, mas permite enviar apenas o ID no POST
    category = CategorySerializer(read_only=True, many=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), write_only=True, many=True, source='category'
    )

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'category', 'category_id', 'active']

class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True, many=True)
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), write_only=True, many=True, source='product'
    )

    class Meta:
        model = Order
        fields = ['id', 'product', 'product_id', 'user', 'created_at']
