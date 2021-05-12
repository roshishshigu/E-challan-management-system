from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from Collab_Project import models
from .models import Challan, Help, Home


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)
        
        if user is not None:
            if user.is_active:
                login(request,user)
                return redirect('/index')
    context = {}
    return render(request,'login.html',context)

def logoutPage(request):
    logout(request)
    return redirect('/')

@login_required(login_url="/")
def home(request):

    if request.method == "POST":
        name = request.POST['Name']
        place = request.POST['Place']
        lisencenumber = request.POST['LisenceNumber']
        vehiclenumber = request.POST['VehicleNumber']
        vehicletype = request.POST['VehicleType']
        createdby = request.POST['TrafficName']
        ins = models.Challan(name=name, place=place, lisencenumber=lisencenumber, vehiclenumber=vehiclenumber, vehicletype=vehicletype, createdby=createdby)
        ins.save()
  
    return render(request,'home.html' )

@login_required(login_url='/')
def index(request):
    data3 = Home.objects.all()
    return render(request,'index.html',{"Home":data3})

@login_required(login_url='/')
def help(request):
    data2 = Help.objects.all()
    return render(request,'help.html',{"Help":data2})

@login_required(login_url='/')
def contact(request):
    if request.method == "POST":
        username = request.POST['contactname']
        email = request.POST['contactemail']
        message = request.POST['contactmessage']
        ins2 = models.Queries(Name=username, Email=email, Message=message)
        ins2.save()

    return render(request,'contact.html')

@login_required(login_url='/')
def challan(request):
    data=Challan.objects.filter(createdby=request.user)
    return render(request,'challans.html',{"messages":data})

