from django.urls import path
from forms import views


urlpatterns = [
    path('', views.exam),
    path('subject/', views.subject),
    path('addDetail/', views.addDetail),
]
