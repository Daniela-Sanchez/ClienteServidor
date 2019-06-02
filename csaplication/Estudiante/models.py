from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Estudiante(models.Model):
    profesor=models.ForeignKey(Profesor, on_delete=models.SET(-1))
    name = models.CharField(max_length=100, null=False)
    apellido= models.CharField(max_length=100, null=False)
    edad = models.IntegerField(null=False)
    sexo = models.CharField(max_length=100, null=False)
    direccion = models.CharField(max_length = 250, null = False) 
    matricula = models.IntegerField(null=False)
    subject = models.CharField(max_length=100, null=False)
    númeroTelefonico = models.IntegerField(null=False)
    fechaNacimiento = models.DateField(default = timezone.now)
    materia= models.CharField(max_length=100,null=False)
    created = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'Estudiante'

