from django.contrib import admin
from .models import Post, Comments
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """This code will give your admin panel greater functionality and clarity.
    We'll discuss this in more detail soon"""
    list_display = ('title', 'slug', 'status')
    search_fields = ['title']
    list_filter = ('status', 'create_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)
    list_display = ('title', 'slug', 'status', 'create_on')


# admin.site.register(Post)
    

admin.site.register(Comments)
