from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
from .models import *
from .forms import CreateUserForm


def signin(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account created sucessfully for '+ user)
        return redirect('/login')

    return render(request,'signin.html',{"form":form})

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)
       
        if user is not None:
            login(request,user)
            return redirect('/home')
    context = {}
    return render(request,'login.html',context)

def logoutPage(request):
    logout(request)
    return redirect('/login')


def home(request):
    return render(request,'home.html')