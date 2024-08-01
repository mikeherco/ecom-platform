"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin

from django.urls import path, include, re_path
from rest_framework import routers

from wagtail.admin import urls as wagtail_admin_urls
from wagtail.admin.views.account import LoginView
from wagtail.documents import urls as wagtail_docs_urls

from rest.urls import wagtail_router
from search import views as search_views


urlpatterns = [
    path("admin/", admin.site.urls),

    path("wadmin/login", LoginView.as_view(), name="wagtail_login"),
    path("wadmin/", include(wagtail_admin_urls)),
    path("documents/", include(wagtail_docs_urls)),
    path("search/", search_views.search, name="search"),


    path('rest/auth', include('rest_framework.urls'), name='rest_rest_framework'),
    path('rest/', include(r'rest.urls'), name='rest_urls'),
    path("rest/", wagtail_router.urls)
]
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = urlpatterns + [
    # # For anything not caught by a more specific rule above, hand over to
    # # Wagtail's page serving mechanism. This should be the last pattern in
    # # the list:
    # path("", include(wagtail_urls)),
    # # Alternatively, if you want Wagtail pages to be served from a subpath
    # # of your site, rather than the site root:
    # #    path("pages/", include(wagtail_urls)),
]
