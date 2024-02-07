from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def about(request):
    """About page"""
    return HttpResponse("Hello World! This is the about Page")