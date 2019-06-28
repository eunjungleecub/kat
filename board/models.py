from django.db import models

#import user account
import account.models

class Post(models.Model):
    title = models.CharField(max_length=100)
    #import user account
    author = models.CharField(max_length=10)
    created_date = models.DateTimeField('date post created', auto_now_add=True)
    files = models.FileField(upload_to='files')
    content = models.TextField()

    
    def __str__(self):
        return self.titled

    def author(self):
        return self.author


class Comment(models.Model):
    #import user account
    post = models.ForeignKey()
    author = models.CharField(max_length=10)
    content = models.TextField()

class Subcomments(models.Model):


