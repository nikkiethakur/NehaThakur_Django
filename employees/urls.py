from django.contrib import admin
from django.urls import path
from employees import views


urlpatterns = [
    path('employees/' , views.vsl ,name = 'home')
   
]
