from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('plantas', views.PlantasViewSet)
router.register('distaves', views.DistAvesViewSet)
router.register('distfamilia', views.DistFamiliaViewSet)
router.register('distcomercial', views.DistComercialViewSet)
router.register('agrupacion', views.AgrupacionViewSet)
router.register('familia', views.FamiliaViewSet)
router.register('planificaciones', views.PlanificacionesViewSet)
router.register('calendario', views.CalendarioViewSet)
#router.register('createpdf', views.ReportPdfView)

urlpatterns = [
    path('', include(router.urls)),
    path('get_id/',views.get_id),
    path('listtrgip001/',views.ListT_RGIP001),
    path('guardardistaves/',views.GuardarDistAves),
    path('guardardistfamilia/',views.GuardarDistFamilia),
    path('guardardistcomercial/',views.GuardarDistComercial),
    path('editardistaves/',views.EditarDistAves),
    path('editardistfamilia/',views.EditarDistFamilia),
    path('editardistcomercial/',views.EditarDistComercial),
    path('report-pdf/', views.ReportPdfView.as_view()),
    path('report-excel/<int:id>', views.vista_xls),
]