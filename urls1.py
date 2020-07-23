
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.userinfo,name="userinfo"),
    path('userinfo',views.userinfo,name="userinfo"),
    path('show',views.show,name="show"),
    path('check',views.getdata,name="getdata"),

]



