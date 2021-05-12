from django.urls import path , include
from . import views


urlpatterns=[
    # path('',views.signin , name='SignIn'),
    path('',views.loginPage , name='Login'),
    path('index/', views.index , name='Index'),
    path('home/',views.home , name='Home'),
    path('logout/',views.logoutPage , name='Logout'),
    path('help/',views.help , name='Help'),
    path('contact/',views.contact , name='Contact'),
    path('challan/',views.challan , name='Challan'),


]