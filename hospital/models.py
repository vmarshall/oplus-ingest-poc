from django.db import models


# Create your models here.

class Facility(models.Model):
    facility_name = models.CharField(max_length=200)
    bin = models.CharField(max_length=200, default='000-0000')
    latitude = models.FloatField()
    longitude = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.facility_name
