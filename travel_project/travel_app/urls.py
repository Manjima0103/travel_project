from django.urls import path, include

from travel_app import views

urlpatterns = [
    path('', views.demo, name='demo'),
]
