# ----------------------------- Librerias -----------------------------
from rest_framework import routers, serializers, viewsets

from drf_dynamic_fields import DynamicFieldsMixin

# ----------------------------- Modelos -----------------------------
from Profesor.models import Profesor

class ProfesorSerializers(DynamicFieldsMixin,serializers.ModelSerializer):
    class Meta:
        model = Profesor
        fields = ('id','nombre','apellido','edad','sexo','subject','amosExperencia','numeroTelefonico','fechaNacimiento')