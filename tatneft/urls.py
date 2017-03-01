# -*- coding: utf-8 -*-

"""tatneft URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from tatneft import settings
from tatneft.views import bid, add_bid, designer, add_designer, technologist, add_technologist
from django.views.i18n import javascript_catalog

urlpatterns = [
    url(r'^admin/jsi18n/', javascript_catalog),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^$', bid, name='bid'),
    url(r'^add_bid/', add_bid, name='add_bid'),
    url(r'^designer/', designer, name='designer'),
    url(r'^add_designer/', add_designer, name='add_designer'),
    url(r'^technologist/', technologist, name='technologist'),
    url(r'^add_technologist/', add_technologist, name='add_technologist'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
