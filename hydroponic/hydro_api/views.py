from hydro_api.models import HydroponicSystem, Measurement
from hydro_api.serializers import HydroponicSystemSerializer, MeasurementSerializer
from rest_framework import viewsets, permissions


class HydroponicSystemView(viewsets.ModelViewSet):
    queryset = HydroponicSystem.objects.all()
    serializer_class = HydroponicSystemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class MeasurementView(viewsets.ModelViewSet):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
    permission_classes = [permissions.IsAuthenticated]