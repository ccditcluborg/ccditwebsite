from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib import messages

from .forms import LoginForm, UserCreationForm

# Create your views here.

def signin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            user = authenticate(request, email=form.cleaned_data['email'], password=form.cleaned_data['password'])

            if user is not None:
                login(request, user)
                messages.info(request, 'Successfully logged in')

                return HttpResponseRedirect('/')
            else:
                messages.error(request, 'Invalid email/password')
                return HttpResponseRedirect('/accounts/signin')
        else:
            return render(request, 'accounts/signin.html', {'form': form})
    else:
        form = LoginForm()

        return render(request, 'accounts/signin.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.info(request, 'Successfully registered')
            return HttpResponseRedirect('/')
        else:
            return render(request, 'accounts/register.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'accounts/register.html', {'form': form})

def signout(request):
    logout(request)
    messages.info(request, 'Successfully logged out')
    return HttpResponseRedirect('/accounts/signin')