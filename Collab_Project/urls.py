from django.urls import path , include
from . import views

urlpatterns=[
    path('',views.signin , name='SignIn'),
    path('login/',views.loginPage , name='Login'),
    path('home/',views.home , name='Home'),
    path('logout/',views.logoutPage , name='Logout'),

]