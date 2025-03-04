from django.db import models
from tinymce import models as tinymce_models

class BlogPost(models.Model):
    category = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100, null=True)
    content = tinymce_models.HTMLField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='blogImages/', blank=True, null=True)

    def __str__(self):
        return self.title
    

class signInUser(models.Model):
    username = models.CharField(max_length=100)
    emailId = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username
    

class CommentPost(models.Model):
    comment = models.TextField()
    emailId = models.ForeignKey(signInUser, on_delete=models.CASCADE)
    title = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    posted_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.comment[:15]}... by {self.emailId.username}'

