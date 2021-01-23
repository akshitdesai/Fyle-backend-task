from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
schema_view = get_schema_view(
    openapi.Info(
        title="Fyle-Banks API",
        default_version='v1',
        description="Fyle Full Stack Coding Challenge(Assessment Project)\nSubmitted By:- Akshit Desai",
    ),
   public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/', include('api.urls')),
    url(r'', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
