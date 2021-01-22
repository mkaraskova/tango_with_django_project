from django.urls import path
from about import views

app_name = 'rango'

urlpatterns = [
    path('', about_views.about, name='about'),
]
