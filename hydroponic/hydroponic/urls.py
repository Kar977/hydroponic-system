from django.contrib import admin
from django.urls import path, include

from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny


schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version="1.0.0",
        description="API Documentation of HydroponicApp"
    ),
    public=True,
    permission_classes=(AllowAny, ),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("hydro_api.urls")),
    path('account/', include("accounts.urls")),
    path('api-documentation/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name="swagger-schema"),
    path('api-documentation/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name="redoc-ui")
]
