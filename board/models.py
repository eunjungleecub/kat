from django.db import models

#import user account
import account.models

class Post(models.Model):
    title = models.CharField(max_length=100)
    #import user account; @decoration
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
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=10)
    content = models.TextField(max_length=200)
    created_date = models.DateTimeField('date post created', auto_now_add=True)

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')

#    def total_likes(self)

# def like_action(self)