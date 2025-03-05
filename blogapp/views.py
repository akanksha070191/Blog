from django.shortcuts import render,redirect, get_object_or_404
from .models import BlogPost, signInUser, CommentPost
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.hashers import check_password, make_password
import re
from blogapp.templatetags import get_dict
from django.core.paginator import Paginator

def blog(request):
    allBlog = BlogPost.objects.filter().order_by('-created_on')[:4]
    categoryList = BlogPost.objects.values('category').distinct()
    category_dict = {}

    for category in categoryList:
        blogCategory = BlogPost.objects.filter(category=category['category']).order_by('-created_on')[:2]
        titles = [{'id': blog.id, 'title': blog.title, 'author': blog.author, 'created_on':blog.created_on} for blog in blogCategory]  
        if titles:
            category_dict[category['category']] = titles
    return render(request, 'blog.html', {'allBlog': allBlog, 'category_dict': category_dict})

def signin(request):
    return render(request, 'signin.html')

def blogDetail(request, blog_id):
    blog = BlogPost.objects.get(id=blog_id)
    comment = CommentPost.objects.filter(title=blog.id, parent=None).order_by('-posted_time')
    replies = CommentPost.objects.filter(title=blog.id).order_by('-posted_time').exclude(parent=None)
    replyDict = {}
    for reply in replies:
        if reply.parent.id not in replyDict.keys():
            replyDict[reply.parent.id]=[reply]
        else:
            replyDict[reply.parent.id].append(reply)
    print('reply Dict:', replyDict)


    otherBlog = BlogPost.objects.exclude(id=blog_id).order_by('-created_on')[:3]

    sentences = re.split(r'(\. )', blog.content)  
    paragraph_size = 3 
    paragraphs = []
    temp_paragraph = ""

    for i, sentence in enumerate(sentences):
        temp_paragraph += sentence
        if (i + 1) % (paragraph_size * 2) == 0:
            paragraphs.append(temp_paragraph.strip())
            temp_paragraph = ""

    if temp_paragraph:
        paragraphs.append(temp_paragraph.strip())

    formatted_content = "\n\n".join(paragraphs)
     
    username = request.session.get('username')
    return render(request, 'blogDetail.html', {'blog':blog, 'otherBlog':otherBlog, 'username': username, 'formattedContent':formatted_content,
                                                'comments':comment,
                                                'count': comment.count(),
                                                'replyDict': replyDict})

def signInNewUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('useremail')
        password = request.POST.get('userpassword')

        hashPassword = make_password(password)

        user = signInUser(username=username, emailId=email, password=hashPassword)
        user.save()
        messages.success(request, 'Account Created!!')
        return redirect('signin')
    
    return render(request, 'signin.html')

def checkEmailId(request):
    email = request.GET.get('email', None)
    useremail = signInUser.objects.filter(emailId=email).exists()
    if(useremail):
        return JsonResponse({'exists':True})
    else:
        return JsonResponse({'exists':False})

def loggedInUser(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        print('email', email)
        userData = signInUser.objects.filter(emailId=email).first()
        
        if(userData):
            if check_password(password, userData.password): 
                request.session['username']=userData.username
                return redirect('blog')
            else:
                return render(request, 'signin.html', {'error': 'Invalid password'})  
        else:
            return render(request, 'signin.html', {'error': 'Email not registered'})  

    return redirect('blog')

def postComment(request):
    if request.method == "POST":
        comment = request.POST.get('comment')
        username = request.POST.get('user_name')
        blogId = request.POST.get('blog_id')
        parentId = request.POST.get('parentId')

        if not username:
            messages.error(request, 'You must be logged in to comment.')
            return redirect('signin')
        


        # Get BlogPost instance
        blog = get_object_or_404(BlogPost, id=blogId)

        # Get signInUser instance using username
        user = get_object_or_404(signInUser, username=username)
        print('emailId:', user.emailId)

        if parentId == "":
            userComment = CommentPost(comment=comment, emailId=user, title=blog)
            userComment.save()
            messages.success(request, 'Comment Posted!!')
        else:
            parent = CommentPost.objects.get(id=parentId)
            userComment = CommentPost(comment=comment, emailId=user, title=blog, parent=parent)
            userComment.save()
            messages.success(request, 'Reply Posted!!')

        return redirect('blogDetail', blog_id=blogId)

def search(request):
    query = request.GET.get('query', '')
    searchBlogList = BlogPost.objects.filter(title__icontains=query).order_by('-created_on') if query else BlogPost.objects.all().order_by('-created_on')
    allPosts = BlogPost.objects.filter(content__icontains=query).order_by('-created_on')
    authorPost = BlogPost.objects.filter(author__icontains=query).order_by('-created_on')
    unionBlog = searchBlogList.union(allPosts)
    searchBlog = unionBlog.union(authorPost)

    return render(request, 'search.html', {'searchBlog': searchBlog, 'query': query})

def allBlogs(request):
    allPost = BlogPost.objects.all().order_by('-created_on')
    paginator = Paginator(allPost, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'allBlogs.html', {'allPost': allPost, 'page_obj': page_obj})

def signOut(request):
    request.session.flush()
    return redirect('blog')



