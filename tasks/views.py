from datetime import date

from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View

from .models import Todo

# Create your views here.


def home(request):
    return render(request, "home.html")


def signup(request):
    
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password = request.POST['password1'], email = request.POST['useremail'])
                user.save()
                login(request, user)
                return redirect('home')
            except: 
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'User already registered. Try Login.'
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error': 'Passwords are differents.'
        })

def signin(request):
    if request.method == 'GET':
        return render(request, "signin.html", {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username = request.POST['username'], password=request.POST['password'])

        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Name or password incorrect. Please verify.'
            })
        else:
            login(request, user)
            return redirect('tasks')

@login_required
def exit(request):
    logout (request)
    return redirect('home')

@method_decorator(login_required, name='dispatch')
class TodoListView(ListView):
    model = Todo

@method_decorator(login_required, name='dispatch')
class TodoCreateView(CreateView):
    model = Todo
    fields = ["title", "deadline"]
    success_url = reverse_lazy("tasks")

@method_decorator(login_required, name='dispatch')
class TodoUpdateView(UpdateView):
    model = Todo
    fields = ['title','deadline']
    success_url = reverse_lazy("tasks")

@method_decorator(login_required, name='dispatch')
class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy("tasks")

@method_decorator(login_required, name='dispatch')
class TodoCompleteView(View):
    def get(self, request, pk):
        Todo.objects.get(pk=pk)
        todo = get_object_or_404(Todo, pk=pk)
        todo.finished_at = date.today()
        todo.save()
        return redirect('tasks')