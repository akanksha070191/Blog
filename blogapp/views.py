from django.shortcuts import render,redirect
from .models import BlogPost, signInUser
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.hashers import check_password, make_password
import re

def blog(request):
    allBlog = BlogPost.objects.filter().order_by('-created_on')[:4]
    return render(request, 'blog.html', {'allBlog': allBlog})

def signin(request):
    return render(request, 'signin.html')

def blogDetail(request, blog_id):
    blog = BlogPost.objects.get(id=blog_id)
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
    return render(request, 'blogDetail.html', {'blog':blog, 'otherBlog':otherBlog, 'username': username, 'formattedContent':formatted_content})

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

def signOut(request):
    request.session.flush()
    return redirect('blog')

