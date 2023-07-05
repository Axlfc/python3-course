"""
URL configuration for noseke project.

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
from django.contrib import admin
from django.urls import path
from . import views


def create_path(name): return path(name + '/', getattr(views, name), name=name)


def create_dynamic_path(n, html_tag): return path(f'{n}/<{type(n).__name__}:{html_tag}>', getattr(views, n), name=n)


urlpatterns = [
    path('admin/', admin.site.urls),
]
