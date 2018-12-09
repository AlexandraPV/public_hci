from django.shortcuts import render
from django.http import HttpResponse
from category.models import Category , Laptop
from .models import Backet
# Create your views here.


def add_basket(request , id , category):
    list_category  = list(Category.objects.all())
    current_elem  = None
    category_front = None
    for  elem in list_category:
        if str(elem) == "Ноутбук":
           current_elem = Laptop.objects.get(id=id)
    Backet.objects.add(current_elem)
    # print(current_elem)
    return HttpResponse('asdasd')