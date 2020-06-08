from django.shortcuts import render
from django.http import HttpResponse

def Home(request):
    
    return render(request,'dateTime/Home.html')
    
def About(request):
	return render(request,'dateTime/About.html')
