from django.test import TestCase
from django.contrib.auth.models import User
from api.models import Product, Category, Order

class IntegridadeModelosTest(TestCase):

    def setUp(self):
        # 1. Criamos o utilizador para o Pedido
        self.user = User.objects.create_user(username='kaio_teste', password='123')
        
        # 2. Criamos a Categoria
        self.category = Category.objects.create(title='Periféricos')
        
        # 3. Criamos o Produto e associamos à Categoria
        self.product = Product.objects.create(title='Microfone Redragon', price=300.00)
        self.product.category.add(self.category)

    def test_integridade_category(self):
        """Verifica se a categoria existe"""
        self.assertEqual(self.category.title, 'Periféricos')

    def test_integridade_product(self):
        """Verifica se o produto está ligado à categoria correta"""
        self.assertEqual(self.product.title, 'Microfone Redragon')
        self.assertEqual(self.product.category.first().title, 'Periféricos')

    def test_integridade_order(self):
        """Verifica se o pedido (Order) liga o utilizador ao produto"""
        order = Order.objects.create(user=self.user)
        order.product.add(self.product)
        
        self.assertEqual(order.user.username, 'kaio_teste')
        self.assertEqual(order.product.count(), 1)
        self.assertEqual(order.product.first().title, 'Microfone Redragon')
