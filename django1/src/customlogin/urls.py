'''
Created on 2019. 1. 27.

@author: user
'''
from django.urls import path
from .views import *

app_name= 'cl'

urlpatterns = [
    #127.0.0.1:8000/cl/signup/
    path('signup/', signup, name = 'signup'),
    #127.0.0.1:8000/cl/signin/
    path('signin/', signin, name = 'signin'),
    #127.0.0.1:8000/cl/signout/
    path('signout/', signout, name = 'signout'),
    ]