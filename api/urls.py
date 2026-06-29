from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CategoryViewSet, OrderViewSet, async_counter_view

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'order', OrderViewSet)

urlpatterns = [
    path('contador/', async_counter_view, name='async_contador'), # Rota exigida no último feedback
    path('', include(router.urls)),
]
