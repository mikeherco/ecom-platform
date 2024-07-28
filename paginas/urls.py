from wagtail.api.v2.views import PagesAPIViewSet
from ecom.urls import api_router


api_router.register_endpoint('pages', PagesAPIViewSet)

