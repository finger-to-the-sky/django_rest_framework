from django.db import models
from uuid import uuid4


class User(models.Model):
    id = models.UUIDField(default=uuid4(), primary_key=True)
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    username = models.CharField(max_length=256, unique=True, null=False)
    email = models.EmailField(unique=True, null=False)
    age = models.IntegerField()


class Project(models.Model):
    name = models.CharField(max_length=32)
    url = models.URLField()
    users = models.ManyToManyField(User)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ToDo(models.Model):
    user = models.ForeignKey(User, models.PROTECT)
    name = models.CharField(max_length=32)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name} -- {self.updated_at}'