from django.urls import path, include
from hydro_api.views import HydroponicSystemView
from rest_framework.routers import DefaultRouter

hydro_system_router = DefaultRouter()
hydro_system_router.register(r'hydro-systems', HydroponicSystemView)


urlpatterns = [
    path('', include(hydro_system_router.urls), name='hydro_system'),
]