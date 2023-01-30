from rest_framework import serializers
from .models import *

class PlantasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plantas
        fields = '__all__'  

class CalendarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calendario
        fields = '__all__'

class PlanificacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planificaciones
        fields = '__all__'  

class AgrupacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agrupacion
        fields = '__all__'  

class FamiliaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Familia
        fields = '__all__'  

class DistAvesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DistAves
        fields = '__all__'  

class DistFamiliaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DistFamilia
        fields = '__all__'  

class DistComercialSerializer(serializers.ModelSerializer):
    class Meta:
        model = DistComercial
        fields = '__all__'  