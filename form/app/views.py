from django.shortcuts import render
from django.http import HttpResponse
from app.forms import RegisterForm, Snippetform


def Register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
    form = RegisterForm()
    return render(request,'register.html',{'form':form})

def snippet_details(request):
    form = Snippetform(request.POST)
    if form.is_valid():
        form.save()
    form = Snippetform()
    return render(request,'register.html',{'form':form})



# Create your views here.
