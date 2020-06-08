from django.db import models


class TodoList(models.Model):
    task = models.TextField()

# Create your models here.
