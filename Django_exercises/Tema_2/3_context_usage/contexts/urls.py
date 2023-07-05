from django.contrib import admin
from django.urls import path
from . import views
import inspect

def create_path(name): return path(name + '/', getattr(views, name), name=name)


def create_dynamic_path(n, html_tag): return path(f'{n}/<{type(n).__name__}:{html_tag}>', getattr(views, n), name=n)


urlpatterns = [
    path('admin/', admin.site.urls),
    create_path('simple'),
    create_dynamic_path('dynamic', 'name')
]
