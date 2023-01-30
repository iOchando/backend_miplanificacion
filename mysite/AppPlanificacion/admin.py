from django.contrib import admin

from .models import Agrupacion, Calendario, DistAves, DistFamilia, DistComercial, Familia, Planificaciones, Plantas

# Register your models here.

admin.site.register(Plantas)
admin.site.register(Planificaciones)
admin.site.register(Calendario)
admin.site.register(Agrupacion)
admin.site.register(Familia)
admin.site.register(DistAves)
admin.site.register(DistFamilia)
admin.site.register(DistComercial)
