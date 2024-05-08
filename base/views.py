from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import todoList
from .forms import TodoForm

# Create your views here.
def home(request):
    user = User.objects.get(id=request.user.id)
    todo = user.todolist_set.all()

    context = {'user': user, 'todo': todo}
    return render(request, 'base/home.html', context)

def createTodo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():

            todo = form.save(commit=False)
            todo.user = request.user
            todo.done = False
            todo.save()
            return redirect('home')
    else:
        form = TodoForm()
    context = {'form':form}
    return render(request, 'base/todo_form.html', context)

def deleteTodo(request, pk):
    pass