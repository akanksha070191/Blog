from django.contrib import admin
from blogapp.models import BlogPost, signInUser, CommentPost


class BlogAdmin(admin.ModelAdmin):
    list_display = ('category', 'author', 'title', 'content', 'created_on', 'updated_on')
    search_fields = ('category' ,)

admin.site.register(BlogPost, BlogAdmin)
admin.site.register(signInUser)
admin.site.register(CommentPost)
