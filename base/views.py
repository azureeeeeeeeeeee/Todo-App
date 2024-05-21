from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth.models import User
from .models import todoList
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import TodoForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Create your views here.
def loginPage(request):
    if request.user.is_authenticated:
        return redirect("home")
    
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'base/login.html')


def registerPage(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        
    return render(request, 'base/register.html', {'form': form})


def logoutPage(request):
    logout(request)
    return redirect('login')


@login_required(login_url='/login')
def home(request):
    user = User.objects.get(id=request.user.id)
    q = request.GET.get('q', '')
    todo = user.todolist_set.all()
    todo = todo.filter(Q(name__icontains=q) | Q(description__icontains=q))

    context = {'user': user, 'todo': todo}
    return render(request, 'base/home.html', context)


@login_required(login_url='/login')
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


@login_required(login_url='/login')
def doneTodo(request, pk):
    todo = todoList.objects.get(id=pk)
    todo.status = 'Success'
    todo.save()
    return redirect('home')


@login_required(login_url='/login')
def failedTodo(request, pk):
    todo = todoList.objects.get(id=pk)
    todo.status = 'Failed'
    todo.save()
    return redirect('home')


@login_required(login_url='/login')
def detailTask(request, pk):
    todo = todoList.objects.get(id=pk)
    context = {'todo': todo}
    return render(request, 'base/detail_item.html', context)


@login_required(login_url='/login')
def editTask(request, pk):
    todo = todoList.objects.get(id=pk)
    if request.method == 'POST':
        todo.name = request.POST.get('name')
        todo.description = request.POST.get('description')
        todo.deadline = request.POST.get('deaedline')
        todo.save()
        return redirect('home')
    context = {'todo':todo}
    return render(request, 'base/edit_todo.html', context)


@login_required(login_url='/login')
def delete(request, pk):
    todo = todoList.objects.get(id=pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': todo})