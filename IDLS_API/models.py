# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Measurement(models.Model):
    SSID = models.CharField(max_length=250, null=False)
    RSSI = models.FloatField(max_length=250, null=False)
    Time = models.DateTimeField()
    BSSID = models.CharField(max_length=250, null=False)
    Location_ID = models.CharField(max_length=250, null=False)

class Coordination(models.Model):
    Location_ID = models.CharField(max_length=250, null=False)
    x_coordinate = models.FloatField(max_length=250, null=False)
    y_coordinate = models.FloatField(max_length=250, null=False)

class Production(models.Model):
    SSID = models.CharField(max_length=250, null=False)
    RSSI = models.FloatField(max_length=250, null=False)
    Time = models.DateTimeField()
    BSSID = models.CharField(max_length=250, null=False)
    Location_ID = models.CharField(max_length=250, null=False)
    