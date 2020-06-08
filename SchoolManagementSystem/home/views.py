from django.shortcuts import render, HttpResponse
from datetime import datetime


#This render will import index.html file of templates folder



def index(request):
    return render(request,'index.html')


#This function will act as a database Connector


def add_contact_form(request):
    email =
# Create your views here.
