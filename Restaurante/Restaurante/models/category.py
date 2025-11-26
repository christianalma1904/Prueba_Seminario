# catalog/models/category.py
from django.db import models
from django.urls import reverse

class Category(models.Model):
    codigo = models.CharField(max_length=10, unique=True, verbose_name="Código del Plato")
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    descripcion = models.TextField(verbose_name="Descripción detallada")
    categoria = models.CharField(max_length=50, verbose_name="Categoría (Ej: Entrada, Principal, Postre)")
    precio = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Precio (€)")
    disponible = models.BooleanField(default=True, verbose_name="¿Está disponible hoy?")
    tiempo_preparacion_min = models.IntegerField(verbose_name="Tiempo de preparación (min)")
    calorias = models.IntegerField(blank=True, null=True, verbose_name="Calorías estimadas")
    es_vegetariano = models.BooleanField(default=False, verbose_name="¿Es vegetariano?")
    nivel_picante = models.IntegerField(default=1, verbose_name="Nivel de Picante")

    class Meta:
        verbose_name = "Plato"
        verbose_name_plural = "Platos"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        """Define la URL a la que ir tras crear/actualizar un plato."""
        return reverse('plato_detalle', args=[str(self.id)])

