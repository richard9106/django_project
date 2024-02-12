from django.shortcuts import render
from .models import About

# Create your views here.


def about_me(request):
    """ reder the about page """
    about = About.objects.all().order_by('-update_on').first()
    return render(
        request,
        "about/about.html",
        {"about" : about},
    )

