"""eshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path , include
from . import views

urlpatterns = [
    path('' , views.test),
    path('laptops' , views.laptops_view ,  name='laptops'),
    path('phones' , views.phones_view ,  name='phones'),
    path('laptop-info/<int:pk>/', views.LaptopDetailView.as_view(), name='laptop-detail'),
    path('search', views.search, name='search'),
    path('source-detail-item/<int:id>', views.source_detail_item, name='source_detail_item'),
]
