from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class todoList(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=400, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField(null=True, default=None)
    status = models.CharField(max_length=10, default='Ongoing')
    done = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['deadline', 'created']

    def __str__(self):
        return self.name
    