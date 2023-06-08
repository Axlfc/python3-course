from django.urls import include, re_path


from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
]

'''
urlpatterns = [
    re_path(r'^$', home, name='home'),
    re_path(r'^myapp/', include('myapp.urls'),
]
'''