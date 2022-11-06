from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(response):
    return HttpResponse("<h1>Welcome to THE LOG_ger Home Page!</h1>")
def v1(response):
    return HttpResponse("<h1>Welcome to THE LOG_ger V1 Page!</h1>")

