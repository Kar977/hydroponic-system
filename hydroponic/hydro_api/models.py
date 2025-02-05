from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class HydroponicSystem(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Measurement(models.Model):
    system = models.ForeignKey(HydroponicSystem, on_delete=models.CASCADE)
    ph = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(14)])
    water_temperature = models.DecimalField(max_digits=5, decimal_places=2)
    tds = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Measurement of {self.system}"