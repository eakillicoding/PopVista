from django.db import models
from django.contrib.auth.models import User


class Label(models.Model):
    name = models.CharField(max_length=100, unique=True)
    owner = models.ForeignKey(User, related_name='labels', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    completion_status = models.BooleanField(default=False)
    owner = models.ForeignKey(User, related_name='tasks', on_delete=models.CASCADE)
    labels = models.ManyToManyField(Label, related_name='tasks')

    def __str__(self):
        return self.title
