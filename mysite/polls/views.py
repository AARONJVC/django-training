# from django.shortcuts import render

from django.http import HttpResponse
from django.template import Context, loader

def index(request):
    template = loader.get_template("polls/index.html")
    return HttpResponse(template.render())

def detail(request, question_id):
    return HttpResponse("You are looking at question %s." % question_id)

def vote(request, question_id):
    return HttpResponse("You are voting on question %s." % question_id)

def results(request, question_id):
    return HttpResponse("You are looking at the results of question %s." % question_id)