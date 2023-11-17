from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect, get_object_or_404

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
            return redirect('home')
        
def exit(request):
    logout(request)
    return redirect(request, 'home.html')