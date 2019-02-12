from django.db import models
from django.contrib import auth


from django.contrib.auth import get_user_model

# Create your models here.
User2 = get_user_model()


class User(auth.models.User, auth.models.PermissionsMixin):

    def __str__(self):
        return '{}'.format(self.username)


class Group(models.Model):
    user = models.ForeignKey(User2, related_name='columns', on_delete='CASCADE')
    group_name = models.CharField(max_length=150)
    group_order = models.IntegerField()


class Task(models.Model):
    user = models.ForeignKey(User2, related_name='tasks', on_delete='CASCADE')
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=300)
    progress = models.CharField(max_length=150)
    priority = models.CharField(max_length=100, default='low')
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}: {}'.format(self.title, self.description)
