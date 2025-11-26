# catalog/serializers/category.py
from rest_framework import serializers
from Restaurante.models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id","codigo","nombre","descripcion","categoria","precio","disponible","tiempo_preparacion_min","calorias","es_vegetariano","nivel_picante")
        read_only_fields = ("id","created_at","updated_at")
