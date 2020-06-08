from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='dateTime-Home'),
    path('about/',views.About, name='dateTime-About'),
]
