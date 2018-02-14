"""snugasabuginacouch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include

from apps.list_manager.forms import LanguageForm


def index_view(request):
    return render(request, 'index.html', {'language_form': LanguageForm()})


list_manager_patterns = ([
                             url('', include('apps.list_manager.urls')),
                         ], 'list_manager')

urlpatterns = [
    url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('admin/', admin.site.urls),
    url(r'^', include(list_manager_patterns)),
    url(r'^$', index_view, name='index'),
    url(r'^i18n/', include('django.conf.urls.i18n'), name='i18n'),
]
