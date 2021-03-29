# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Measurement(models.Model):
    SSID = models.CharField(max_length=250, null=False)
    RSSI = models.FloatField(max_length=250, null=False)
    BSSID = models.CharField(max_length=250, null=False)
    Location_ID = models.CharField(max_length=250, null=False)

    