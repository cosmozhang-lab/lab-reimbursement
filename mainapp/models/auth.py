from django.db import models

class UserRole(models.Model):
    rolename = models.CharField(max_length=128, unique=True)

class User(models.Model):
    username = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=128)
