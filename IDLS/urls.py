"""IDLS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from IDLS_API.views import api_handler, api_handler_mobile
from IDLS_API.api.views import mobile_handler
import rest_framework

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^IDLS/API/handler', api_handler, name='api_handler'),
    url(r'^IDLS/API/handler_mobile', api_handler_mobile, name='api_mobile'),
    #path('api-auth', include('rest_framework.urls')),
    url(r'^idls_api/api/mes/mobile_handler', mobile_handler, name='mes_api_mobile')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)