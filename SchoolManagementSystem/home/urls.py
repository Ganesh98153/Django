from django.test import TestCase

#create your tests hers.

from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
]
