from django.shortcuts import render
from .models import BlogPost

def blog(request):
    allBlog = BlogPost.objects.filter().order_by('-created_on')
    return render(request, 'blog.html', {'allBlog': allBlog})

