"""mobileonlineshopping URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from .views import registration,signout,signin,home,adminpage,add_mobile,viewMobile,edit_mobile,delete_mobile,search_mobile,sort_mobile,buyer_details,editorder,cancelorder,viewOrder

urlpatterns = [

    path('registration',registration,name='registration'),
    path("signin",signin,name="signin"),
    path("signout",signout,name="signout"),
    path("",home,name="home"),
    path('admin',adminpage,name="admin"),
    path('add',add_mobile,name="add"),
    path('view/<int:id>',viewMobile,name='view'),
    path('edit/<int:id>',edit_mobile,name='edit'),
    path('delete/<int:id>',delete_mobile,name='delete'),
    path('search',search_mobile,name='search'),
    path('sort',sort_mobile,name='sort'),
    path('buyer/<int:id>',buyer_details,name="buyer"),
    path("vieworder",viewOrder,name='vieworder'),
    path('editorder/<int:id>',editorder,name="editorder"),
    path('cancelorder/<int:id>',cancelorder,name="cancelorder"),

]
