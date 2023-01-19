"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

admin.site.site_header = "Nepal Geo Api"
admin.site.site_title = "Nepal Geo Api"

schema_view = get_schema_view(
    openapi.Info(
        title="Nepal Geo API",
        default_version="v1",
        description="This is an API providing the list of geo data of Nepal built in Djang by Bibek Khatri",
        contact=openapi.Contact(name="Bibek Khatri",
                                email="bibekkhatri291@gmail.com")
    ),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", schema_view.with_ui("swagger")),
    path("api/geo/", include('geo.urls'))
]
