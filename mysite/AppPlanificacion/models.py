from enum import unique
from django.db import models
from django.contrib.auth.models import User
from django.views import View
from django.http import HttpResponse

# Create your models here.

class Calendario(models.Model):
    id = models.AutoField(primary_key=True)
    anopro = models.IntegerField()
    mespro = models.IntegerField()
    anocon = models.IntegerField()
    mescon = models.IntegerField()
    semcon = models.IntegerField()
    fecini = models.DateField(auto_now_add=False)
    fecfin = models.DateField(auto_now_add=False)

class Plantas(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length= 255,unique=True)
    capacidadoperativa =  models.IntegerField()
    capacidadinstalada =  models.IntegerField()
    user_create = models.TextField(max_length= 255)
    user_update = models.TextField(max_length= 255)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

class Planificaciones(models.Model):
    id = models.AutoField(primary_key=True)
    planta = models.CharField(max_length= 255)
    anocon = models.IntegerField()
    mescon = models.IntegerField()
    semcon = models.IntegerField()

    lunes = models.FloatField()
    lunespp = models.FloatField()
    lunesrend = models.FloatField()
    lunesem = models.FloatField()
    lunestb = models.FloatField()
    lunespppb = models.FloatField()

    martes = models.FloatField()
    martespp = models.FloatField()
    martesrend = models.FloatField()
    martesem = models.FloatField()
    martestb = models.FloatField()
    martespppb = models.FloatField()

    miercoles = models.FloatField()
    miercolespp = models.FloatField()
    miercolesrend = models.FloatField()
    miercolesem = models.FloatField()
    miercolestb = models.FloatField()
    miercolespppb = models.FloatField()

    jueves = models.FloatField()
    juevespp = models.FloatField()
    juevesrend = models.FloatField()
    juevesem = models.FloatField()
    juevestb = models.FloatField()
    juevespppb = models.FloatField()

    viernes = models.FloatField()
    viernespp = models.FloatField()
    viernesrend = models.FloatField()
    viernesem = models.FloatField()
    viernestb = models.FloatField()
    viernespppb = models.FloatField()

    sabado = models.FloatField()
    sabadopp = models.FloatField()
    sabadorend = models.FloatField()
    sabadoem = models.FloatField()
    sabadotb = models.FloatField()
    sabadopppb = models.FloatField()

    total = models.FloatField()
    totalpp = models.FloatField()
    totalrend = models.FloatField()
    totalem = models.FloatField()
    totaltb = models.FloatField()
    totalpppb = models.FloatField()

class DistAves(models.Model):
    id = models.AutoField(primary_key=True)
    id_plan = models.ForeignKey(Planificaciones, on_delete=models.CASCADE)
    agrupacion = models.CharField(max_length= 255)
    status = models.BooleanField()
    familia = models.BooleanField()
    undLunes = models.FloatField()
    undMartes = models.FloatField()
    undMiercoles = models.FloatField()
    undJueves = models.FloatField()
    undViernes = models.FloatField()
    undSabado = models.FloatField()
    undTotal = models.FloatField()

    tonLunes = models.FloatField()
    tonMartes = models.FloatField()
    tonMiercoles = models.FloatField()
    tonJueves = models.FloatField()
    tonViernes = models.FloatField()
    tonSabado = models.FloatField()
    tonTotal = models.FloatField()
    

class DistFamilia(models.Model):
    id = models.AutoField(primary_key=True)
    id_plan = models.ForeignKey(Planificaciones, on_delete=models.CASCADE)
    familia = models.CharField(max_length= 255)
    rendimiento = models.FloatField()
    tonLunes = models.FloatField()
    tonMartes = models.FloatField()
    tonMiercoles = models.FloatField()
    tonJueves = models.FloatField()
    tonViernes = models.FloatField()
    tonSabado = models.FloatField()
    tonTotal = models.FloatField()

class DistComercial(models.Model):
    id = models.AutoField(primary_key=True)
    id_plan = models.ForeignKey(Planificaciones, on_delete=models.CASCADE)
    nombre = models.CharField(max_length= 255)
    ventLunes = models.FloatField()
    ventMartes = models.FloatField()
    ventMiercoles = models.FloatField()
    ventJueves = models.FloatField()
    ventViernes = models.FloatField()
    ventSabado = models.FloatField()
    ventTotal = models.FloatField()

    proLunes = models.FloatField()
    proMartes = models.FloatField()
    proMiercoles = models.FloatField()
    proJueves = models.FloatField()
    proViernes = models.FloatField()
    proSabado = models.FloatField()
    proTotal = models.FloatField()
    tipo = models.IntegerField() # 1 comercial / 2 comercial de familia

class Agrupacion(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length= 255,unique=True)
    status = models.BooleanField()
    familia = models.BooleanField()
    user_create = models.TextField(max_length= 255)
    user_update = models.TextField(max_length= 255)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

class Familia(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length= 255,unique=True)
    status = models.BooleanField()
    rendimiento = models.IntegerField()
    user_create = models.TextField(max_length= 255)
    user_update = models.TextField(max_length= 255)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

