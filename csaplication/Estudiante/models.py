from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Estudiante(models.Model):
    #user = models.ForeignKey(User, on_delete = models.SET(-1))
    name = models.CharField(max_length=100, null=False)
    edad = models.IntegerField(null=False)
    sexo = models.CharField(max_length=100, null=False)
    dirección = models.CharField(max_length = 250, null = False) 
    matrícula = models.IntegerField(null=False)
    subject = models.CharField(max_length=100, null=False)
    númerotelefónico = models.IntegerField(null=False)
    fechanacimiento = models.DateField(default = timezone.now)
    delete = models.BooleanField(default = False)
    created = models.DateTimeField(default = timezone.now)
    edited = models.DateTimeField(blank=True, null=True, default=None)

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'Estudiante'

