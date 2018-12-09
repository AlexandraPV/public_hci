from django.contrib import admin
from django.urls import path , include
from . import views

app_name = 'backet'

urlpatterns = [
    path('add-to-backet/<int:id>/<str:category>/' , views.add_basket , name='add-to-backet')
]
