from django.db import models

# Create your models here.


class Measure(models.Model):
    #name = models.CharField(max_length=70, blank=False, default='')
    #age = models.IntegerField(blank=False, default=1)
    #active = models.BooleanField(default=False)

    id = modules.IntegerField(
        max_length=8, blank=False, default='')  # "00193422",
    timestamp = modules.IntegerField(
        max_length=8, blank=False, default='')  # ": "1568568375",
    temperature = modules.IntegerField(
        max_length=8, blank=False, default='')  # ": "20.1",
    humidity = modules.IntegerField(
        max_length=8, blank=False, default='')  # ": "32",
    lum_x1 = modules.IntegerField(
        max_length=8, blank=False, default='')  # ": "200",
    lum_x2 = modules.IntegerField(
        max_length=8, blank=False, default='')  # ": "231",
    soil_humidity_x1 = modules.IntegerField(
        max_length=8, blank=False, default='')  # ": "12",
    soil_humidity_x2 = modules.IntegerField(
        max_length=8, blank=False, default='')  # ": "14"

