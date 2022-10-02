from django.urls import include
from django.urls import re_path, path
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from core.registries import plugin_registry


def health(request):
    return HttpResponse("OK")


urlpatterns = (
    [
        path('admin/', admin.site.urls),
        re_path(r"^api/", include("api.urls", namespace="api")),
        re_path(r"^_health$", health, name="health_check"),
    ]
    + plugin_registry.urls
    + static(settings.MEDIA_URL_PATH, document_root=settings.MEDIA_ROOT)
)
