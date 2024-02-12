from django.contrib import admin
from .models import About
from django_summernote.admin import SummernoteModelAdmin


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    """create the module to able to eddit as a admin"""
    summernote_fields = ("content",)

# Register your models here.
