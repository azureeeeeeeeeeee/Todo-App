from django.forms import ModelForm
from .models import todoList
from django.contrib.auth.models import User

class TodoForm(ModelForm):
    class Meta:
        model = todoList
        fields = '__all__'
        exclude = ['user', 'done']