from django.db import models

class BlogPost(models.Model):
    category = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100, null=True)
    content = models.TextField()
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

