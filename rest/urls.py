from rest_framework import routers

from wagtail.api.v2.router import WagtailAPIRouter

from paginas.viewsets import PaginasViewSet

drf_router = routers.DefaultRouter()
wagtail_router = WagtailAPIRouter('wagtail_api')

urlpatterns = [
]

wagtail_router.register_endpoint(r'paginas', PaginasViewSet)


#quesesto?
# drf_router.include_root_view = True

urlpatterns += drf_router.urls
