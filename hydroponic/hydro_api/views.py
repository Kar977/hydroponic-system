from django_filters import NumberFilter, DateTimeFilter
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from hydro_api.models import HydroponicSystem, Measurement
from hydro_api.serializers import HydroponicSystemSerializer, MeasurementSerializer
from rest_framework import viewsets, permissions, filters
from rest_framework.pagination import PageNumberPagination


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class MeasurementFilter(FilterSet):
    ph_min = NumberFilter(field_name="ph", lookup_expr="lte")
    ph_max = NumberFilter(field_name="ph", lookup_expr="gte")
    water_temperature_min = NumberFilter(field_name="water_temperature", lookup_expr="lte")
    water_temperature_max = NumberFilter(field_name="water_temperature", lookup_expr="gte")
    tds_min = NumberFilter(field_name="tds", lookup_expr="lte")
    tds_max = NumberFilter(field_name="tds", lookup_expr="gte")

    class Meta:
        model = Measurement
        fields = ['ph_min', 'ph_max', 'water_temperature_min', 'water_temperature_max', 'tds_min', 'tds_max']


class HydroponicSystemFilter(FilterSet):
    created_at_min = DateTimeFilter(field_name="created_at", lookup_expr="lte")
    created_at_max = DateTimeFilter(field_name="created_at", lookup_expr="gte")
    updated_at_min = DateTimeFilter(field_name="updated_at", lookup_expr="lte")
    updated_at_max = DateTimeFilter(field_name="updated_at", lookup_expr="gte")

    class Meta:
        model = HydroponicSystem
        fields = ['created_at_min', 'created_at_max', 'updated_at_min', 'updated_at_max']


class HydroponicSystemView(viewsets.ModelViewSet):
    queryset = HydroponicSystem.objects.all()
    serializer_class = HydroponicSystemSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = HydroponicSystemFilter
    ordering_fields = ['name', 'created_at']

    def get_queryset(self):
        return HydroponicSystem.objects.filter(owner=self.request.user)


class MeasurementView(viewsets.ModelViewSet):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    #filterset_fields = ['ph', 'water_temperature', 'tds']
    filterset_class = MeasurementFilter
    ordering_fields = ['ph', 'water_temperature', 'tds']

    def get_queryset(self):
        return Measurement.objects.filter(system__owner=self.request.user)
