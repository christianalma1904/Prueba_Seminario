from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Plato(models.Model):
    CATEGORIA_CHOICES = [
        ("ENTRADA", "Entrada"),
        ("PRINCIPAL", "Plato Fuerte"),
        ("POSTRE", "Postre"),
        ("BEBIDA", "Bebida"),
        ("OTRO", "Otro"),
    ]
    
    NIVEL_PICANTE_CHOICES = [
        (0, "No Picante"),
        (1, "Suave"),
        (2, "Medio"),
        (3, "Alto"),
        (4, "Extremo"),
    ]
    
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    categoria = models.CharField(max_length=50, choices=CATEGORIA_CHOICES, default="PRINCIPAL")
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    disponible = models.BooleanField(default=True)
    tiempo_preparacion_min = models.PositiveBigIntegerField(validators=[MinValueValidator(1)])
    calorias = models.PositiveBigIntegerField(validators=[MinValueValidator(0)], blank=True, null=True)
    es_vegetariano = models.BooleanField(default=False)
    nivel_picante = models.IntegerField(choices=NIVEL_PICANTE_CHOICES, default=0,validators=[MinValueValidator(0), MaxValueValidator(4)])

    def __str__(self):
        return f"{self.nombre} ({self.codigo})"