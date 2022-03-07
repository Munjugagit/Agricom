from django.contrib import admin
from .models import Incidences, Counties
from django.contrib.gis import admin
from leaflet.admin import LeafletGeoAdmin

# Register your models here.

class IncidencesAdmin(LeafletGeoAdmin):
    # pass
   list_display =('name','location')

class CountiesAdmin(LeafletGeoAdmin):
    # pass
   list_display =('county3_field','county3_id')

admin.site.register(Incidences, IncidencesAdmin)
admin.site.register(Counties, CountiesAdmin)