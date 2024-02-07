"""Importing httpresponse for the views"""

from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    """Home page"""
    if request.method == "GET":
        return HttpResponse("You must POSTed samething")
    elif request.method == "POST":
        return HttpResponse(request.method)
