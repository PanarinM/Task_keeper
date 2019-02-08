from django.db import models
from datetime import datetime
from django.conf import settings

from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()


class Group(models.Model):
    # user = models.ForeignKey(User, related_name='tasks', on_delete='CASCADE')
    group_name = models.CharField(max_length=150, unique=True)


class Task(models.Model):
    # user = models.ForeignKey(User, related_name='tasks', on_delete='CASCADE')
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=300)
    progress = models.CharField(max_length=150)
    priority = models.CharField(max_length=100, default='low')
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}: {}'.format(self.title, self.description)

