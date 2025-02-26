from django.contrib import admin
from blogapp.models import BlogPost

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'created_on', 'updated_on')

admin.site.register(BlogPost, BlogAdmin)
