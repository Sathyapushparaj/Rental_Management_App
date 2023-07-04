from django.urls import path,include
from .views import sayhello


urlpatterns = [

    path('', sayhello,name='hello world'),
]