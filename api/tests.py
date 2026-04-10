from django.test import TestCase
from django.contrib.auth.models import User
from .models import Category, Product, Order
from .serializers import CategorySerializer, ProductSerializer

class TestSerializers(TestCase):
    def setUp(self):
        self.category = Category.objects.create(title='Livros', slug='livros')
        self.product = Product.objects.create(
            name='Clean Code', 
            description='Livro de programação', 
            price=100.00
        )
        self.product.category.add(self.category)
        
    def test_category_serializer(self):
        serializer = CategorySerializer(instance=self.category)
        data = serializer.data
        self.assertEqual(data['title'], 'Livros')
        self.assertEqual(data['slug'], 'livros')

    def test_product_serializer_with_category(self):
        serializer = ProductSerializer(instance=self.product)
        data = serializer.data
        self.assertEqual(data['name'], 'Clean Code')
        # Verifica se a categoria está aninhada corretamente
        self.assertEqual(data['category'][0]['title'], 'Livros')
