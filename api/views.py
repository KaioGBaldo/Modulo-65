import asyncio
from django.http import JsonResponse
from rest_framework import viewsets
from .models import Product, Category, Order
from .serializers import ProductSerializer, CategorySerializer, OrderSerializer

# ---------------------------------------------------------
# Viewsets para os Modelos (Exigência do DRF / Bookstores)
# ---------------------------------------------------------

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('id')
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('id')
    serializer_class = OrderSerializer


# ---------------------------------------------------------
# View Assíncrona com Contador (Exigência do Último Feedback)
# ---------------------------------------------------------

# Um contador global simples para fins demonstrativos da view
contador_acessos = 0

async def async_counter_view(request):
    """
    View Assíncrona que demonstra conceitos de Non-blocking calls.
    Utiliza asyncio.sleep para não travar a execução do servidor.
    """
    global contador_acessos
    
    # Simula uma operação assíncrona/I-O bound de 1 segundo
    # Sem efetuar uma blocking call convencional
    await asyncio.sleep(1) 
    
    contador_acessos += 1
    
    return JsonResponse({
        "status": "sucesso",
        "mensagem": "Operação assíncrona executada com sucesso!",
        "contador_total_acessos": contador_acessos
    })