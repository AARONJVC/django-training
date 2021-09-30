from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.

def welcome(request):
    return  render(request, "website/welcome.html", {"meeting_name": "Krispy Kreme Donut Eating Contest", "meeting_time": "11:30:00", "meeting_date": "05/12/2021"})

def date(request):
    return  HttpResponse("Page served at " + str(datetime.now()))

def personal_info(request):
    return HttpResponse("What i n tarnattion")