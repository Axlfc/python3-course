from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('greet/', views.greet, name="greet"),
    path('bye/', views.bye, name="bye"),
    path('adult/<int:age>/', views.adult, name="adult")
]
