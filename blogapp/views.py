from django.shortcuts import render
from .models import BlogPost

def blog(request):
    allBlog = BlogPost.objects.filter().order_by('-created_on')
    return render(request, 'blog.html', {'allBlog': allBlog})

def signin(request):
    return render(request, 'signin.html')

def blogDetail(request, blog_id):
    blog = BlogPost.objects.get(id=blog_id)
    otherBlog = BlogPost.objects.exclude(id=blog_id).order_by('-created_on')
    return render(request, 'blogDetail.html', {'blog':blog, 'otherBlog':otherBlog})
