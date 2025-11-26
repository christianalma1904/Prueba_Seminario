# catalog/views/category.py
from rest_framework import viewsets, filters
from Restaurante.models import Category
from Restaurante.serializers import CategorySerializer
from Restaurante.permissions import IsAdminOrReadOnly

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ("nombre","categoria","descripcion")
    ordering_fields = ("nombre","precio","tiempo_preparacion_min","calorias")
