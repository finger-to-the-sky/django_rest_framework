from django.db import models
from uuid import uuid4


class User(models.Model):
    id = models.UUIDField(default=uuid4(), primary_key=True)
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    username = models.CharField(max_length=256, unique=True, null=False)
    email = models.EmailField(unique=True, null=False)
    age = models.IntegerField()
