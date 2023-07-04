from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def helloguys(request):
    return HttpResponse('<h1> This My 2nd project </h1>')