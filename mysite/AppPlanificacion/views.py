from django.db.models import Sum
from django.shortcuts import render

from .consultasSqlServer import *

from .consultasOracle import *
from .models import *
from django.contrib.auth.models import User
from rest_framework import viewsets, generics, request
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from django_filters import rest_framework as filters
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, mixins, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.utils import json
from django.http import JsonResponse, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.core import serializers
from multiprocessing import Process
from rest_framework.response import Response
import datetime
from .serializers import *
from django.views import View
import xlwt
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders

class PlantasViewSet(viewsets.ModelViewSet):
    queryset = Plantas.objects.all()
    serializer_class = PlantasSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('nombre','id', 'capacidadoperativa', 'capacidadinstalada')

class PlanificacionesViewSet(viewsets.ModelViewSet):
    model = Planificaciones
    queryset = Planificaciones.objects.all()
    serializer_class = PlanificacionesSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('planta','anocon','mescon','semcon')

class CalendarioViewSet(viewsets.ModelViewSet):
    queryset = Calendario.objects.all()
    serializer_class = CalendarioSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('anocon','mescon','semcon')

class AgrupacionViewSet(viewsets.ModelViewSet):
    queryset = Agrupacion.objects.all()
    serializer_class = AgrupacionSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('nombre','id', 'status','familia')

class FamiliaViewSet(viewsets.ModelViewSet):
    queryset = Familia.objects.all()
    serializer_class = FamiliaSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('nombre','id', 'status',)

class DistAvesViewSet(viewsets.ModelViewSet):
    queryset = DistAves.objects.all()
    serializer_class = DistAvesSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('agrupacion','id', 'id_plan', 'familia')

class DistFamiliaViewSet(viewsets.ModelViewSet):
    queryset = DistFamilia.objects.all()
    serializer_class = DistFamiliaSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('familia','id', 'id_plan',)

class DistComercialViewSet(viewsets.ModelViewSet):
    queryset = DistComercial.objects.all()
    serializer_class = DistComercialSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('nombre','id', 'id_plan',)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def ListT_RGIP001(request):
    Arreglo = T_RGIP001()
    return JsonResponse(Arreglo, safe=False)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def GuardarDistAves(request):
    try:
        data = json.loads(request.body)
        result = FunGuardarDistAves(data)
        if result is False:
            return Response({'value': 'Error al guardar la cuenta'}, status=status.HTTP_404_NOT_FOUND)     

        return JsonResponse(result, safe=False)
    except Exception as e:
        return Response({'value': 'Error al guardar la cuenta'}, status=status.HTTP_404_NOT_FOUND)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def GuardarDistFamilia(request):
    try:
        data = json.loads(request.body)
        result = FunGuardarDistFamilia(data)
        if result is False:
            return Response({'value': 'Error al guardar la cuenta'}, status=status.HTTP_404_NOT_FOUND)     

        return JsonResponse(result, safe=False)
    except Exception as e:
        return Response({'value': 'Error al guardar la cuenta'}, status=status.HTTP_404_NOT_FOUND)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def GuardarDistComercial(request):
    try:
        data = json.loads(request.body)
        result = FunGuardarDistComercial(data)
        if result is False:
            return Response({'value': 'Error al guardar la cuenta'}, status=status.HTTP_404_NOT_FOUND)     

        return JsonResponse(result, safe=False)
    except Exception as e:
        return Response({'value': 'Error al guardar la cuenta'}, status=status.HTTP_404_NOT_FOUND)


@api_view(["POST"])
@csrf_exempt
def get_id(request):
    data = json.loads(request.body)
    try:
        uid = User.objects.get(username=data['username'])
        return JsonResponse({'id': uid.id}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        print(e)
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def EditarDistAves(request):
    try:
        data = json.loads(request.body)
        result = FunEditarDistAves(data)
        if result is False:
            return Response({'value': 'Error al editar la cuenta'}, status=status.HTTP_404_NOT_FOUND)     

        return JsonResponse(result, safe=False)
    except Exception as e:
        return Response({'value': 'Error al editar la cuenta'}, status=status.HTTP_404_NOT_FOUND)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def EditarDistFamilia(request):
    try:
        data = json.loads(request.body)
        result = FunEditarDistFamilia(data)
        if result is False:
            return Response({'value': 'Error al editar la cuenta'}, status=status.HTTP_404_NOT_FOUND)     

        return JsonResponse(result, safe=False)
    except Exception as e:
        return Response({'value': 'Error al editar la cuenta'}, status=status.HTTP_404_NOT_FOUND)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def EditarDistComercial(request):
    try:
        data = json.loads(request.body)
        result = FunEditarDistComercial(data)
        if result is False:
            return Response({'value': 'Error al editar la cuenta'}, status=status.HTTP_404_NOT_FOUND)     

        return JsonResponse(result, safe=False)
    except Exception as e:
        return Response({'value': 'Error al editar la cuenta'}, status=status.HTTP_404_NOT_FOUND)


class ReportPdfView(View):
    def get(self, request, *args, **kwargs):
        template = get_template('report-pdf.html')
        context = {'title': 'primer pdf'}
        html = template.render(context)
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="report.pdf"'

        pisa_status = pisa.CreatePDF(
            html, dest=response)
        # if error then show some funy view
        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def vista_xls(request, id):
    response=HttpResponse(content_type='application/ms-excel')
    for k in Planificaciones.objects.filter(id=id).values():
        response['Content-Disposition']='attachment; filename="Proyección de producción Semana"' + str(k['semcon']) + '".xls"'
    excel_wb=xlwt.Workbook(encoding='utf-8')
    excel_ws=excel_wb.add_sheet('Styling Data') # ws es Work Sheet
    i=1
    excel_ws.col(0).width = 800
    excel_ws.col(1).width = 14000
    excel_ws.col(2).width = 4000
    excel_ws.col(3).width = 4000
    excel_ws.col(4).width = 4000
    excel_ws.col(5).width = 4000
    excel_ws.col(6).width = 4000
    excel_ws.col(7).width = 4000
    excel_ws.col(8).width = 4000
    for m in Planificaciones.objects.filter(id=id).values():
        estilo1 = xlwt.easyxf('font: height 220; font: bold 1')
        estilo = xlwt.easyxf('font: height 220; font: bold 1; pattern: pattern solid, fore-colour gray25, back_color orange;border: left thin,right thin,top thin,bottom thin')
        estilo2 = xlwt.easyxf('font: height 220; font: bold 1; pattern: pattern solid, fore-colour teal;border: left thin,right thin,top thin,bottom thin')
        estilo3 = xlwt.easyxf('font: height 220; border: left thin,right thin,top thin,bottom thin')
        estilo4 = xlwt.easyxf('font: height 220; font: bold 1; border: left thin,right thin,top thin,bottom thin')
        
        excel_ws.write(i,1,'SEMANA CONTABLE: ' + str(m['semcon']) + ',  MES: ' + str(m['mescon']) + ',  AÑO: ' + str(m['anocon']),estilo1)
        i=i+2
        excel_ws.write(i,1,'PLANIFICACIÓN DE PLANTA: ' + str(m['planta']),estilo2)
        excel_ws.write(i,2,'LUNES',estilo)
        excel_ws.write(i,3,'MARTES',estilo)
        excel_ws.write(i,4,'MIERCOLES',estilo)
        excel_ws.write(i,5,'JUEVES',estilo)
        excel_ws.write(i,6,'VIERNES',estilo)
        excel_ws.write(i,7,'SABADO',estilo)
        excel_ws.write(i,8,'TOTAL',estilo)
        i=i+1
        excel_ws.write(i,1,'Unidades',estilo3)
        excel_ws.write(i,2, m['lunes'],estilo3)
        excel_ws.write(i,3, m['martes'],estilo3)
        excel_ws.write(i,4, m['miercoles'],estilo3)
        excel_ws.write(i,5, m['jueves'],estilo3)
        excel_ws.write(i,6, m['viernes'],estilo3)
        excel_ws.write(i,7, m['sabado'],estilo3)
        excel_ws.write(i,8, m['total'],estilo3)
        i=i+1
        excel_ws.write(i,1,'Peso Promedio PV',estilo3)
        excel_ws.write(i,2, m['lunespp'],estilo3)
        excel_ws.write(i,3, m['martespp'],estilo3)
        excel_ws.write(i,4, m['miercolespp'],estilo3)
        excel_ws.write(i,5, m['juevespp'],estilo3)
        excel_ws.write(i,6, m['viernespp'],estilo3)
        excel_ws.write(i,7, m['sabadopp'],estilo3)
        excel_ws.write(i,8, m['totalpp'],estilo3)
        i=i+1
        excel_ws.write(i,1,'Entradas a Matadero (Kg)',estilo3)
        excel_ws.write(i,2, m['lunesem'],estilo3)
        excel_ws.write(i,3, m['martesem'],estilo3)
        excel_ws.write(i,4, m['miercolesem'],estilo3)
        excel_ws.write(i,5, m['juevesem'],estilo3)
        excel_ws.write(i,6, m['viernesem'],estilo3)
        excel_ws.write(i,7, m['sabadoem'],estilo3)
        excel_ws.write(i,8, m['totalem'],estilo3)
        i=i+1
        excel_ws.write(i,1,'% Rend. Bruto',estilo3)
        excel_ws.write(i,2, m['lunesrend'],estilo3)
        excel_ws.write(i,3, m['martesrend'],estilo3)
        excel_ws.write(i,4, m['miercolesrend'],estilo3)
        excel_ws.write(i,5, m['juevesrend'],estilo3)
        excel_ws.write(i,6, m['viernesrend'],estilo3)
        excel_ws.write(i,7, m['sabadorend'],estilo3)
        excel_ws.write(i,8, m['totalrend'],estilo3)
        i=i+1
        excel_ws.write(i,1,'Kg Beneficiadas',estilo3)
        excel_ws.write(i,2, m['lunestb'],estilo3)
        excel_ws.write(i,3, m['martestb'],estilo3)
        excel_ws.write(i,4, m['miercolestb'],estilo3)
        excel_ws.write(i,5, m['juevestb'],estilo3)
        excel_ws.write(i,6, m['viernestb'],estilo3)
        excel_ws.write(i,7, m['sabadotb'],estilo3)
        excel_ws.write(i,8, m['totaltb'],estilo3)
        i=i+1
        excel_ws.write(i,1,'Peso Promedio PB',estilo3)
        excel_ws.write(i,2, m['lunespppb'],estilo3)
        excel_ws.write(i,3, m['martespppb'],estilo3)
        excel_ws.write(i,4, m['miercolespppb'],estilo3)
        excel_ws.write(i,5, m['juevespppb'],estilo3)
        excel_ws.write(i,6, m['viernespppb'],estilo3)
        excel_ws.write(i,7, m['sabadopppb'],estilo3)
        excel_ws.write(i,8, m['totalpppb'],estilo3)
        i=i+2
        excel_ws.write(i,1,'Distribucion de unidades beneficiadas por Planta',estilo2)
        excel_ws.write(i,2,'LUNES',estilo)
        excel_ws.write(i,3,'MARTES',estilo)
        excel_ws.write(i,4,'MIERCOLES',estilo)
        excel_ws.write(i,5,'JUEVES',estilo)
        excel_ws.write(i,6,'VIERNES',estilo)
        excel_ws.write(i,7,'SABADO',estilo)
        excel_ws.write(i,8,'TOTAL',estilo)
        for p in DistAves.objects.filter(id_plan=id, familia=False).values():
            i=i+1
            excel_ws.write(i,1,str(p['agrupacion']) + ' (Unidades)',estilo3)
            excel_ws.write(i,2, p['undLunes'],estilo3)
            excel_ws.write(i,3, p['undMartes'],estilo3)
            excel_ws.write(i,4, p['undMiercoles'],estilo3)
            excel_ws.write(i,5, p['undJueves'],estilo3)
            excel_ws.write(i,6, p['undViernes'],estilo3)
            excel_ws.write(i,7, p['undSabado'],estilo3)
            excel_ws.write(i,8, p['undTotal'],estilo3)
            i=i+1
            excel_ws.write(i,1,str(p['agrupacion']) + ' (Kg)',estilo3)
            excel_ws.write(i,2, p['tonLunes'],estilo3)
            excel_ws.write(i,3, p['tonMartes'],estilo3)
            excel_ws.write(i,4, p['tonMiercoles'],estilo3)
            excel_ws.write(i,5, p['tonJueves'],estilo3)
            excel_ws.write(i,6, p['tonViernes'],estilo3)
            excel_ws.write(i,7, p['tonSabado'],estilo3)
            excel_ws.write(i,8, p['tonTotal'],estilo3)
            i=i+1
        
        for p in DistAves.objects.filter(id_plan=id, familia=True).values():
            i=i+2
            excel_ws.write(i,1,str(p['agrupacion']) + ' (Unidades)',estilo4)
            excel_ws.write(i,2, p['undLunes'],estilo3)
            excel_ws.write(i,3, p['undMartes'],estilo3)
            excel_ws.write(i,4, p['undMiercoles'],estilo3)
            excel_ws.write(i,5, p['undJueves'],estilo3)
            excel_ws.write(i,6, p['undViernes'],estilo3)
            excel_ws.write(i,7, p['undSabado'],estilo3)
            excel_ws.write(i,8, p['undTotal'],estilo3)
            i=i+1
            excel_ws.write(i,1,str(p['agrupacion']) + ' (Kg)',estilo4)
            excel_ws.write(i,2, p['tonLunes'],estilo3)
            excel_ws.write(i,3, p['tonMartes'],estilo3)
            excel_ws.write(i,4, p['tonMiercoles'],estilo3)
            excel_ws.write(i,5, p['tonJueves'],estilo3)
            excel_ws.write(i,6, p['tonViernes'],estilo3)
            excel_ws.write(i,7, p['tonSabado'],estilo3)
            excel_ws.write(i,8, p['tonTotal'],estilo3)
            i=i+1
        for p in DistFamilia.objects.filter(id_plan=id).values():
            i=i+1
            excel_ws.write(i,1,str(p['familia']) + ' (Rendimiento)',estilo3)
            excel_ws.write(i,2, p['rendimiento'],estilo3)
            excel_ws.write(i,3, p['rendimiento'],estilo3)
            excel_ws.write(i,4, p['rendimiento'],estilo3)
            excel_ws.write(i,5, p['rendimiento'],estilo3)
            excel_ws.write(i,6, p['rendimiento'],estilo3)
            excel_ws.write(i,7, p['rendimiento'],estilo3)
            excel_ws.write(i,8, p['rendimiento'],estilo3)
            i=i+1
            excel_ws.write(i,1,str(p['familia']) + ' (Kg)',estilo3)
            excel_ws.write(i,2, p['tonLunes'],estilo3)
            excel_ws.write(i,3, p['tonMartes'],estilo3)
            excel_ws.write(i,4, p['tonMiercoles'],estilo3)
            excel_ws.write(i,5, p['tonJueves'],estilo3)
            excel_ws.write(i,6, p['tonViernes'],estilo3)
            excel_ws.write(i,7, p['tonSabado'],estilo3)
            excel_ws.write(i,8, p['tonTotal'],estilo3)
            i=i+1
        i=i+1
        excel_ws.write(i,1,'Distribucion comercial de unidades beneficiadas',estilo2)
        excel_ws.write(i,2,'LUNES',estilo)
        excel_ws.write(i,3,'MARTES',estilo)
        excel_ws.write(i,4,'MIERCOLES',estilo)
        excel_ws.write(i,5,'JUEVES',estilo)
        excel_ws.write(i,6,'VIERNES',estilo)
        excel_ws.write(i,7,'SABADO',estilo)
        excel_ws.write(i,8,'TOTAL',estilo)

        for p in DistComercial.objects.filter(id_plan=id).values():
            i=i+1
            excel_ws.write(i,1,str(p['nombre']) + ' para Ventas (Kg)',estilo3)
            excel_ws.write(i,2, p['ventLunes'],estilo3)
            excel_ws.write(i,3, p['ventMartes'],estilo3)
            excel_ws.write(i,4, p['ventMiercoles'],estilo3)
            excel_ws.write(i,5, p['ventJueves'],estilo3)
            excel_ws.write(i,6, p['ventViernes'],estilo3)
            excel_ws.write(i,7, p['ventSabado'],estilo3)
            excel_ws.write(i,8, p['ventTotal'],estilo3)
            i=i+1
            excel_ws.write(i,1,str(p['nombre']) + ' para Procesado (Kg)',estilo3)
            excel_ws.write(i,2, p['proLunes'],estilo3)
            excel_ws.write(i,3, p['proMartes'],estilo3)
            excel_ws.write(i,4, p['proMiercoles'],estilo3)
            excel_ws.write(i,5, p['proJueves'],estilo3)
            excel_ws.write(i,6, p['proViernes'],estilo3)
            excel_ws.write(i,7, p['proSabado'],estilo3)
            excel_ws.write(i,8, p['proTotal'],estilo3)
            i=i+1
        
    excel_wb.save(response)
    return response