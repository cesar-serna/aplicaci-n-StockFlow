from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'productos', views.ProductoViewSet, basename='api-productos')

urlpatterns = [
    path('api/', include(router.urls)),
]