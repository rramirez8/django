from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList,Item

# Create your views here.

def index(response, id):
    ls = ToDoList.objects.get(id=id)
    lsitem = ls.item_set.get(id=1)
    return HttpResponse("<h1>%s</h1><hr><h1>%s</h1>" %(ls.name, str(lsitem.text)))
