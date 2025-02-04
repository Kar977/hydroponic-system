from hydro_api.models import HydroponicSystem
from rest_framework import serializers


class HydroponicSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = HydroponicSystem
        fields = ['id', 'owner', 'name', 'description', 'created_at', 'updated_at']
        read_only_fields = ['id', 'owner', 'created_at', 'updated_at']