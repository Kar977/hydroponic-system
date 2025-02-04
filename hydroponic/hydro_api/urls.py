from django.urls import path, include
from hydro_api.views import HydroponicSystemView, MeasurementView
from rest_framework.routers import DefaultRouter

hydro_router = DefaultRouter()
hydro_router.register('systems', HydroponicSystemView)
hydro_router.register('measures', MeasurementView)


urlpatterns = [
    path('', include(hydro_router.urls), name='hydro_api'),
]
