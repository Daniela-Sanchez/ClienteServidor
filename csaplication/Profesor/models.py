from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



class Profesor(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    apellido = models.CharField(max_length=100, null=False)
    edad = models.IntegerField(null=False)
    sexo = models.CharField(max_length=100, null=False)
    subject = models.CharField(max_length=100, null=False)
    amosExperencia = models.IntegerField(null=False)
    numeroTelefonico = models.IntegerField(null=False)
    fechaNacimiento = models.DateField(default = timezone.now)
    delete = models.BooleanField(default = False)
    created = models.DateTimeField(default = timezone.now)
    edited = models.DateTimeField(blank=True, null=True, default=None)

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'Profesor'
