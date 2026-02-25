from django.test import TestCase
from django.contrib.auth.models import User
from loja.models import Product, Category, Order

class IntegrityModelTest(TestCase):

    def setUp(self):
        # Cria dados básicos para os testes
        self.user = User.objects.create_user(username='kaio_test', password='123')
        self.category = Category.objects.create(title='Eletrônicos')
        self.product = Product.objects.create(title='Celular', price=1000.00)
        self.product.category.add(self.category)

    def test_integridade_categoria(self):
        self.assertEqual(self.category.title, 'Eletrônicos')

    def test_integridade_produto(self):
        self.assertEqual(self.product.title, 'Celular')
        self.assertEqual(self.product.category.first().title, 'Eletrônicos')

    def test_integridade_pedido(self):
        # Testa o modelo Order conforme solicitado pelo Samir
        order = Order.objects.create(user=self.user)
        order.product.add(self.product)
        self.assertEqual(order.user.username, 'kaio_test')
        self.assertEqual(order.product.count(), 1)
