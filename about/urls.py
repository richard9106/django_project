"""Import the views and urls path"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.about_me, name='about'),
]
