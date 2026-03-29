from django.test import TestCase
from .models import Product
from .serializers import ProductSerializer

class ProductSerializerTest(TestCase):
    def setUp(self):
        self.product_attributes = {
            'name': 'Teclado Mecânico',
            'description': 'Switch Blue, RGB',
            'price': '250.00'
        }
        self.product = Product.objects.create(**self.product_attributes)
        self.serializer = ProductSerializer(instance=self.product)

    def test_serializer_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'name', 'description', 'price', 'created_at']))

    def test_serializer_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['name'], self.product_attributes['name'])
        self.assertEqual(data['price'], self.product_attributes['price'])
