from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sayhello(reuest):
    return HttpResponse('<h1> Hai This My First Django Webpage </h1>')