from django.db import models
from django.contrib.auth.models import User, UserManager, 

class Admin(UserManager):
    pass

class Member(models.Model):
    username = models.TextField(max_length=191)
    email = models.EmailField(blank=False)
    password = models.PassField(required=True)
    is_staff = models.BooleanField(choices='staff, member')

class UserPermission(models.Model):
    name = 
    content_type =
    codename = 

class Group(models.model):
    name = models.ManyToManyField(to='models.Member')

