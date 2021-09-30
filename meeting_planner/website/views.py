from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

from meetings.models import Meeting

# Create your views here.

def welcome(request):
    return  render(request, "website/welcome.html", {"meetings": Meeting.objects.all(), "count": Meeting.objects.count()})

def date(request):
    return  HttpResponse("Page served at " + str(datetime.now()))

def personal_info(request):
    return HttpResponse("What i n tarnattion")
