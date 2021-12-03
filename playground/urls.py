#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 10:37:32 2021

@author: matthewayala
"""

from django.urls import path
from . import views

# URLconf
urlpatterns = [
    path('', views.say_hello),
    path('', views.home)
    
    ]