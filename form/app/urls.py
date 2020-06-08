from django.urls import path
from app import views    #It takes around 2 days to find this code error name: views is not define

urlpatterns = [
    path('', views.Register),
    path('snippet', views.snippet_details),
]


