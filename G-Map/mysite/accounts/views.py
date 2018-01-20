# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):    
    return render(request, 'accounts/home.html')

def dash(request):    
    return render(request, 'accounts/dashboard.html')

def gmap(request):
    return render(request, 'accounts/myMap.html')