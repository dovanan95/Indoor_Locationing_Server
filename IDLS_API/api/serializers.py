from rest_framework import serializers
from IDLS_API.models import Measurement

class serialMes(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['RSSI', 'BSSID', 'SSID', 'Location_ID']