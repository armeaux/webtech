from django.db import models
from django.utils import timezone


class Task(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    due_date = models.DateTimeField(blank=True, null=True)
    category = models.CharField(max_length=100, default='default')
    priority = models.CharField(max_length=50, default='middle')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title