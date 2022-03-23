from leaflet.admin import LeafletGeoAdmin
from django.contrib import admin
from .models import Incidences, Counties
from django.contrib.gis import admin


# Register your models here.

class IncidencesAdmin(LeafletGeoAdmin):
    # pass
   list_display =('name','location')

class CountiesAdmin(LeafletGeoAdmin):
    # pass
   list_display =('id_2','name_2')

admin.site.register(Incidences, IncidencesAdmin)
admin.site.register(Counties, CountiesAdmin)
