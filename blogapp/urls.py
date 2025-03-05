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
    path('loggedin/', views.loggedInUser, name='loggedin'),
    path('signout/', views.signOut, name='signout'),
    path('postComment', views.postComment, name='postComment'),
    path('search/', views.search, name='search'),
    path('allBlogs/', views.allBlogs, name='allBlogs'),
    path('archives/<int:year>/', views.archive_by_year, name='archive_by_year'),
    path('archives/<int:year>/<str:month>/', views.archive_by_month, name='archive_by_month'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

