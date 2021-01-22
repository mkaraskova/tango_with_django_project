from django.urls import path
from rango import views
from rango import about_views

app_name = 'rango'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/',about_views.about, name='about'),
]
