from django.contrib import admin
from blogapp.models import BlogPost, signInUser


class BlogAdmin(admin.ModelAdmin):
    list_display = ('category', 'author', 'title', 'content', 'created_on', 'updated_on')

admin.site.register(BlogPost, BlogAdmin)
admin.site.register(signInUser)
