from django.urls import path
from forms import views


urlpatterns = [
    path('', views.exam),
    path('addDetail/', views.addDetail),
    path('subjectForm/', views.subjectForm),
    path('addSubject/',views.addSubject),
]
