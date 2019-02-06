from django.db import models
from datetime import datetime

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=300)
    progress = models.CharField(max_length=100, default='to do')
    priority = models.CharField(max_length=100, default='low')
    created_at = models.DateTimeField(default=datetime.now, blank='True')

    def __str__(self):
        return '{}: {}'.format(self.title, self.description)

