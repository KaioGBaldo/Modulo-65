from django.test import TestCase
from django.contrib.auth.models import User
from .models import Category, Product, Order
from .serializers import CategorySerializer, ProductSerializer, OrderSerializer

class TestSerializers(TestCase):
    def setUp(self):
        # Criando massa de dados para os testes
        self.user = User.objects.create_user(username='testuser', password='password123')
        
        self.category = Category.objects.create(title='Livros', slug='livros', active=True)
        
        self.product = Product.objects.create(
            name='Clean Code', 
            description='Livro de programação', \
            price=100.00,
            active=True
        )
        self.product.category.add(self.category)
        
        self.order = Order.objects.create(user=self.user)
        self.order.product.add(self.product)
        
    def test_category_serializer(self):
        """Valida a serialização do modelo Category"""
        serializer = CategorySerializer(instance=self.category)
        data = serializer.data
        self.assertEqual(data['title'], 'Livros')
        self.assertEqual(data['slug'], 'livros')
        self.assertTrue(data['active'])

    def test_product_serializer_with_category(self):
        """Valida a serialização do Product e o aninhamento de Category (GET)"""
        serializer = ProductSerializer(instance=self.product)
        data = serializer.data
        self.assertEqual(data['name'], 'Clean Code')
        self.assertEqual(data['category'][0]['title'], 'Livros')

    def test_product_serializer_deserialization(self):
        """Valida a criação de um Product enviando o category_id (POST)"""
        data = {
            "name": "Design Patterns",
            "description": "Padrões de projeto",
            "price": "120.00",
            "category_id": [self.category.id],
            "active": True
        }
        serializer = ProductSerializer(data=data)
        self.assertTrue(serializer.is_valid(), serializer.errors)
        new_product = serializer.save()
        self.assertIn(self.category, new_product.category.all())

    def test_order_serializer(self):
        """Valida a serialização do modelo Order e os campos aninhados"""
        serializer = OrderSerializer(instance=self.order)
        data = serializer.data
        self.assertEqual(data['user'], self.user.id)
        self.assertEqual(data['product'][0]['name'], 'Clean Code')

    def test_order_serializer_deserialization(self):
        """Valida a criação de uma Order enviando o product_id"""
        data = {
            "product_id": [self.product.id],
            "user": self.user.id
        }
        serializer = OrderSerializer(data=data)
        self.assertTrue(serializer.is_valid(), serializer.errors)
        new_order = serializer.save()
        self.assertIn(self.product, new_order.product.all())
