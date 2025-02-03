from hydro_api.models import HydroponicSystem
from hydro_api.serializers import HydroponicSystemSerializer
from rest_framework import viewsets, permissions


class HydroponicSystemView(viewsets.ModelViewSet):
    queryset = HydroponicSystem.objects.all()
    serializer_class = HydroponicSystemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

