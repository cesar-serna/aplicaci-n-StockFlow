from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import Producto
from .serializers import ProductoSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    filterset_fields = ['categoria']
    
    search_fields = ['nombre']
    
    ordering_fields = ['precio', 'stock']
    
    