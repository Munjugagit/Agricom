from django.db import models
from django.contrib.gis.db import models


# Create your models here.
class Incidences(models.Model):
    name = models.TextField()
    location = models.PointField(srid=4326)
    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural ="Incidences"

class Counties(models.Model):
    id_0 = models.BigIntegerField()
    iso = models.CharField(max_length=3)
    name_0 = models.CharField(max_length=75)
    id_1 = models.BigIntegerField()
    name_1 = models.CharField(max_length=75)
    id_2 = models.BigIntegerField()
    name_2 = models.CharField(max_length=75)
    type_2 = models.CharField(max_length=50)
    engtype_2 = models.CharField(max_length=50)
    nl_name_2 = models.TextField(blank=True, null=True)
    varname_2 = models.CharField(max_length=150, null=True)
    geom = models.MultiPolygonField(srid=4326)
    
    def __unicode__(self):
        return self.Counties
        
    class Meta:
        verbose_name_plural ="Counties"