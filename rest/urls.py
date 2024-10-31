from django.urls import path
from rest_framework import routers

from wagtail.api.v2.router import WagtailAPIRouter

from paginas.viewsets import PaginasViewSet, CategoriaViewSet, ConfiguracionSitioViewSet, ClaseColorViewSet

drf_router = routers.DefaultRouter()
wagtail_router = WagtailAPIRouter('wagtail_api')

urlpatterns = []

drf_router.register(r'categorias', CategoriaViewSet, basename='categorias')
drf_router.register(r'clase-color', ClaseColorViewSet, basename='clase-color')
drf_router.register(r'configuracion-sitio', ConfiguracionSitioViewSet, basename='configuracion-sitio')

wagtail_router.register_endpoint(r'paginas', PaginasViewSet)

#quesesto?
# drf_router.include_root_view = True

urlpatterns += drf_router.urls + [
    path("", wagtail_router.urls),
]
