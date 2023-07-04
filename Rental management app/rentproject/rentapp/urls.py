
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='main'),
    path('register', views.register, name='register'),
    path('loginpage', views.loginpage, name='loginpage'),
    path('logout', views.logoutpage, name='logout'),
    path('Appartments',views.appartment,name='Appartments'),

    path('search', views.searchBar, name='search'),

    path('dialpad', views.dialpadpage, name='dialpad'),


    path('products/<str:pk>/',views.productdetails,name='products'),
    path('about', views.aboutpage, name='about'),

]