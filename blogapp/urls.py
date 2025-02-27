from django.contrib import admin
from django.urls import path
from blogapp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.blog, name='blog'),
    path('signin', views.signin, name='signin'),
    path('blogs/<int:blog_id>/', views.blogDetail, name='blogDetail'),
    path('signInNewUser/', views.signInNewUser, name='signInNewUser'),
    path('check_email/', views.checkEmailId, name='check_email'),
    path('loggedin/', views.loggedInUser, name='loggedin')
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

