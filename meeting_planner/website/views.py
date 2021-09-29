from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.

def welcome(request):
    return  HttpResponse("Welcome to the thing")

def date(request):
    return  HttpResponse("Page served at " + str(datetime.now()))

def personal_info(request):
    return HttpResponse("What i n tarnattion")