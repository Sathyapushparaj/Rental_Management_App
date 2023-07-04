from django.urls import path, include
from .views import helloguys

urlpatterns = [
    path('',helloguys,name='two world'),
]