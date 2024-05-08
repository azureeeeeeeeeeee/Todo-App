from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class todoList(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=400, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField(null=True, default=None)
    # done = models.BooleanField(default=False)
    status = models.CharField(max_length=10, default='Ongoing')

    class Meta:
        ordering = ['deadline', 'created']

    def __str__(self):
        return self.name
    