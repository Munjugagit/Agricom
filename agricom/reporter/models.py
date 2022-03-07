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
    objectid = models.IntegerField()
    area = models.FloatField()
    perimeter = models.FloatField()
    county3_field = models.FloatField()
    county3_id = models.FloatField()
    county = models.CharField(max_length=20)
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)
    
    def __unicode__(self):
        return self.Counties
        
      class Meta:
        verbose_name_plural ="Counties"